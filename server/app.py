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

@app.route("/getall")
def get_all():
    try:
        spells=Spell.query.all()
        return jsonify([e.serialize() for e in spells])
    except Exception as e:
	    return(str(e))

@app.route('/spells', methods=['GET'])
def spells():
    filter = request.args.get('filter')
    spell_list = [
        {
            "level": 'Cantrips',
            "spells": []
        },
        {
            "level": 'Level 2',
            "spells": []
        }
    ]
    return jsonify(spell_list)

if __name__ == '__main__':
    app.run()