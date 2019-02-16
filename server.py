from flask import Flask, request, jsonify
from flask_cors import CORS
import PoS
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        f = request.files['subtitles']
        name = './sample.vtt'
        f.save(name)
        return jsonify(PoS.parse_vtt(name))
