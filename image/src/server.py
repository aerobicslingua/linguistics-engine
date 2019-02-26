from flask import Flask, request, jsonify
from flask_cors import CORS
import logic 
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
url = 'http://%s/query/%s'

@app.route('/')
def linguistics():
    return 'Hello, Linguistics engine works!'

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        f = request.files['subtitles']
        name = './sample.vtt'
        f.save(name)
        return jsonify(logic.parse_translate_vtt(url, name))
