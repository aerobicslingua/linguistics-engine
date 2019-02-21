from flask import Flask, request, jsonify
from flask_cors import CORS
import logic 
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
url = 'http://127.0.0.1:3000/query/%s'

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
        return jsonify(logic.parse_translate_vtt(url, name))
