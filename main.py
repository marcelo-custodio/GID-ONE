from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
from cryptography.hazmat.primitives import hashes
import os

# função responsável pelo resumo criptogáfico
def resumo_criptografico(path):
    digest = hashes.Hash(hashes.SHA256())
    f = open(path, 'rb')
    digest.update(f.read())
    f.close()
    return digest.finalize()

# definição do endpoint /api/file, responsável por responder com o resumo criptográfico de um arquivo
class Summary(Resource):
    # Teste de disponibilidade do endpoint
    def get(self):
        return jsonify({"healthcheck": "health"})

    # Parse das entradas da interface e geração da resposta da API
    def post(self):
        file = request.files['file']
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        summary = resumo_criptografico(path)
        os.remove(path)
        return jsonify({"filename": filename, "summary": summary.hex()})

# instanciação da API
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp_files'
api = Api(app)

# definição/disponibilização do endpoint / responsável pela interface gráfica
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# disponibilização do endpoint /api/file
api.add_resource(Summary, '/api/file')

# disponibilização da API
if __name__ == '__main__':
    app.run(debug=True)