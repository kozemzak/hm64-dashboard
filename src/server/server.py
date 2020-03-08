from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from GameState import GameState
from os import path
import constants

app = Flask(__name__)
CORS(app)
game_state = GameState.from_rom_constants()

@app.route('/')
def index():
    return jsonify(game_state.get_features())

@app.route('/meta')
def meta():
    return jsonify({
        'npcs': constants.NPCS,
        'girls': constants.GIRLS,
        'rivals': constants.RIVALS,
    })

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        path.join(app.root_path, 'static'),
        'favicon.ico', 
        mimetype = 'image/vnd.microsoft.icon'
    )

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 3000)
