import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Spell

CORS(app, resources={r'/*': {'origins': '*'}})

def add_spells_to_book(spells, level, spellbook):
    spellbook.append({ 'level': level, 'spells': [sp.serialize() for sp in spells] })

@app.route('/spells', methods=['GET'])
def spells():
    class_filter = request.args.get('filter').lower()
    try:
        spellbook = []
        if (class_filter == 'all'):
            for i in range(0,10):
                spells = Spell.query.filter(Spell.level == i).all()
                add_spells_to_book(spells, i, spellbook)
        else:
            for i in range(0,10):
                spells = Spell.query.filter(getattr(Spell, class_filter) == True, Spell.level == i).all()
                add_spells_to_book(spells, i, spellbook)
        return jsonify(spellbook)
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run()