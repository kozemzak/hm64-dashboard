from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from GameState import GameState
from os import path
from utils import handle_args

app = Flask(__name__)
CORS(app)
args = handle_args()
game_state = GameState.from_rom_name(args.rom_name)

@app.route('/')
def index():
    return jsonify(game_state.get_group_features('all'))

@app.route('/<group>')
def category(group):
    return jsonify(game_state.get_group_features(group))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        path.join(app.root_path, 'static'),
        'favicon.ico', 
        mimetype = 'image/vnd.microsoft.icon'
    )

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 3000)
