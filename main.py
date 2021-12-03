from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
from cryptography.hazmat.primitives import hashes
import os

def resumo_criptografico(path):
    digest = hashes.Hash(hashes.SHA256())
    f = open(path, 'rb')
    digest.update(f.read())
    f.close()
    return digest.finalize()

class Summary(Resource):
    def get(self):
        return jsonify({"healthcheck": "health"})

    def post(self):
        file = request.files['file']
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        summary = resumo_criptografico(path)
        os.remove(path)
        return jsonify({"filename": filename, "summary": summary.hex()})

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp_files'
api = Api(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

api.add_resource(Summary, '/api/file')

if __name__ == '__main__':
    app.run(debug=True)