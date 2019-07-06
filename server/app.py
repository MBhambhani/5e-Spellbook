from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

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