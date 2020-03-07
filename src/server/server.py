from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from GameState import GameState
from os import path

app = Flask(__name__)
CORS(app)
game_state = GameState.from_rom_constants()

@app.route('/')
def index():
    return jsonify(game_state.get_features())

@app.route('/npcs')
def npcs():
    return jsonify(['baby', 'bartender', 'basil', 'carpenter_axe', 'carpenter_master', 'carpenter_saw', 'doug', 'ellen', 'fisherman', 'gotz', 'gotz_wife', 'gourmet', 'kappa', 'kent', 'lillia', 'may', 'mayor', 'mayor_wife', 'midwife', 'old_man', 'old_woman', 'pastor', 'potion_master', 'rick', 'saibara', 'shipper', 'sprite_1', 'sprite_2', 'sprite_3', 'stu'])

@app.route('/girls')
def girls():
    return jsonify(['ann', 'elli', 'karen', 'maria', 'popuri'])

@app.route('/rivals')
def rivals():
    return jsonify(['cliff', 'gray', 'harris', 'jeff', 'kai'])

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        path.join(app.root_path, 'static'),
        'favicon.ico', 
        mimetype = 'image/vnd.microsoft.icon'
    )

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 3000)
