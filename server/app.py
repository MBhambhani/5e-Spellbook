import os
import json
import jwt
from flask import Flask, jsonify, request, current_app
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app, resources={r'/*': {'origins': '*'}})

from models import User, Spell, Spellbook

def add_spells_to_list(spells, level, spell_list):
    spell_list.append({ 'level': level, 'spells': [sp.serialize() for sp in spells] })

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registration and/or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401
        
        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter(User.id == data['sub']).first()

            if not user:
                raise RuntimeError('User not found')
            
            return f(user.id, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401
    return _verify

@app.route('/spells', methods=['GET'])
def get_spells():
    class_filter = request.args.get('filter').lower()

    try:
        spell_list = []

        if (class_filter == 'all'):
            for i in range(0,10):
                spells = Spell.query.filter(Spell.level == i).all()
                add_spells_to_list(spells, i, spell_list)
        else:
            for i in range(0,10):
                spells = Spell.query.filter(getattr(Spell, class_filter) == True, Spell.level == i).all()
                add_spells_to_list(spells, i, spell_list)
        return jsonify(spell_list)
    except Exception as e:
        return str(e)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    try:
        user = User.query.filter(User.username == username).first()

        if user:
            return jsonify({ 'message': 'Username already in use' }), 409
        
        new_user = User(username, password, datetime.utcnow())
        db.session.add(new_user)
        db.session.commit()
        return jsonify({ 'message': 'User successfully created' }), 200
    except Exception as e:
        return str(e)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    try:
        user = User.authenticate(**data)
        if not user:
            return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401
        
        user.last_login = datetime.utcnow()
        db.session.commit()

        token = jwt.encode({
            'sub': user.id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=1)
        }, current_app.config['SECRET_KEY'])

        return jsonify({
            'token': token.decode('UTF-8'),
            'user_id': user.id,
            'message': 'Logged in as {0}'.format(user.username)
        })
    except Exception as e:
        return str(e)

@app.route('/create-spellbook', methods=['POST'])
@token_required
def create_spellbook(user_id):
    data = request.get_json()
    book_name = data.get('book_name')

    try:
        spellbook = Spellbook.query.filter(
            Spellbook.name == book_name,
            Spellbook.creator_id == user_id
        ).first()

        if spellbook:
            return jsonify({ 'message': 'Name already in use' }), 422
        
        new_spellbook = Spellbook(book_name, user_id)
        db.session.add(new_spellbook)
        db.session.commit()
        return jsonify(new_spellbook.serialize()), 201
    except Exception as e:
        return str(e)

@app.route('/delete-spellbook', methods=['POST'])
@token_required
def delete_spellbook(user_id):
    data = request.get_json()
    book_name = data.get('book_name')

    try:
        spellbook = Spellbook.query.filter(
            Spellbook.name == book_name,
            Spellbook.creator_id == user_id
        ).first()

        if not spellbook:
            return jsonify({ 'message': 'Spellbook not found' }), 422
        
        Spellbook.query.filter(Spellbook.name == book_name).delete()
        db.session.commit()
        return jsonify({ 'message': '{} deleted'.format(book_name) })
    except Exception as e:
        return str(e)

@app.route('/get-user-spellbooks', methods=['GET'])
@token_required
def get_user_spellbooks(user_id):
    try:
        spellbooks = Spellbook.query.filter(Spellbook.creator_id == user_id).all()
        book_names = [spellbook.name for spellbook in spellbooks]
        return jsonify(book_names)
    except Exception as e:
        return str(e)

@app.route('/get-spellbook', methods=['GET'])
@token_required
def get_spellbook(user_id):
    book_name = request.args.get('name')

    try:
        spellbook = Spellbook.query.filter(
            Spellbook.name == book_name,
            Spellbook.creator_id == user_id
        ).first()

        if not spellbook:
            return jsonify({ 'message': 'Spellbook not found' }), 422
        
        spell_list = []
        grouped_spells = [[] for i in range(0,10)]
        spells = spellbook.get_spells()

        # get spells by id and group them by level
        for spell_id in spells:
            spell = Spell.query.filter(Spell.id == int(spell_id)).first()
            grouped_spells[spell.level].append(spell)
        
        # build spell list to return
        for i in range(0,10):
            add_spells_to_list(grouped_spells[i], i, spell_list)
        
        return jsonify(spell_list)
    except Exception as e:
        return str(e)

@app.route('/add-to-spellbook', methods=['POST'])
@token_required
def add_to_spellbook(user_id):
    data = request.get_json()
    book_name = data.get('book_name')
    spell_id = data.get('spell_id')

    try:
        spellbook = Spellbook.query.filter(
            Spellbook.name == book_name,
            Spellbook.creator_id == user_id
        ).first()
        spell = Spell.query.filter_by(id=spell_id).first()

        if not spellbook:
            return jsonify({ 'message': 'Spellbook not found' }), 422

        if not spell:
            return jsonify({ 'message': 'Spell not found' }), 422

        spellbook.add_spell(str(spell_id))
        db.session.commit()
        return jsonify({ 'message': '{0} added to {1}'.format(spell.name, spellbook.name) })
    except Exception as e:
        return str(e)

@app.route('/remove-from-spellbook', methods=['POST'])
@token_required
def remove_from_spellbook():
    #TODO
    return

if __name__ == '__main__':
    app.run()