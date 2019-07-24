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
            user = User.query.filter(User.email == data['sub']).first()

            if not user:
                raise RuntimeError('User not found')
            
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401
    
    return _verify

@app.route('/register', methods=['POST'])
def register():
    data = json.loads(request.get_json())
    email = data['email']
    password = data['password']
    
    try:
        user = User.query.filter(User.email == email).first()

        if user:
            return jsonify({ 'message': 'Email already in use' }), 409
        
        new_user = User(email, password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({ 'message': 'User successfully created' }), 200
    except Exception as e:
        return str(e)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.authenticate(**data)
    
    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401
    
    token = jwt.encode({
        'sub': user.email,
        'user': user.id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, current_app.config['SECRET_KEY'])

    return jsonify({ 'token': token.decode('UTF-8') })

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

@app.route('/create-spellbook', methods=['POST'])
@token_required
def create_spellbook():
    data = json.loads(request.get_json())
    book_name = data['book_name']
    creator_id = data['creator_id']

    try:
        spellbook = Spellbook.query.filter(
            Spellbook.name == book_name,
            Spellbook.creator_id == creator_id
        ).first()

        if spellbook:
            return jsonify({ 'message': 'Name already in use' }), 422
        
        new_spellbook = Spellbook(book_name, creator_id)
        db.session.add(new_spellbook)
        db.session.commit()
        return jsonify(new_spellbook.serialize()), 201
    except Exception as e:
        return str(e)

@app.route('/delete-spellbook', methods=['POST'])
@token_required
def delete_spellbook():
    data = json.loads(request.get_json())
    book_id = data['book_id']
    creator_id = data['creator_id']

    try:
        spellbook = Spellbook.query.filter(
            Spellbook.id == book_id,
            Spellbook.creator_id == creator_id
        ).first()

        if not spellbook:
            return jsonify({ 'message': 'Spellbook not found' }), 422
        
        Spellbook.query.filter(Spellbook.id == book_id).delete()
        db.session.commit()
        return jsonify({ 'message': '{} deleted'.format(book_name) })
    except Exception as e:
        return str(e)

@app.route('/get-spellbook', methods=['GET'])
@token_required
def get_spellbook():
    data = json.loads(request.get_json())
    book_id = data['id']
    creator_id = data['creator_id']

    try:
        spellbook = Spellbook.query.filter(
            Spellbook.id == book_id,
            Spellbook.creator_id == creator_id
        ).first()

        if not spellbook:
            return jsonify({ 'message': 'Spellbook not found' }), 422
        
        spell_list = []
        grouped_spells = [[] for i in range(0,10)]

        # get spells by id and group them by level
        for spell_id in spellbook.get_spells():
            spell = Spell.query.filter(Spell.id == spell_id).first()
            grouped_spells[spell.level].append(spell)
        
        # build spell list to return
        for i in range(0,10):
            add_spells_to_list(grouped_spells[i], i, spell_list)
        
        return jsonify(spell_list)
    except Exception as e:
        return str(e)

@app.route('/add-to-spellbook', methods=['POST'])
@token_required
def add_to_spellbook():
    #TODO
    return

@app.route('/remove-from-spellbook', methods=['POST'])
@token_required
def remove_from_spellbook():
    #TODO
    return

if __name__ == '__main__':
    app.run()