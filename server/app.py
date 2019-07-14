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

@app.route('/spells', methods=['GET'])
def spells():
    col_name = request.args.get('filter').lower()
    try:
        spellbook = []
        for i in range(0,10):
            spells = Spell.query.filter(getattr(Spell, col_name) == True, Spell.level == i).all()
            spellbook.append({ 'level': i, 'spells': [sp.serialize() for sp in spells] })
        return jsonify(spellbook)
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run()