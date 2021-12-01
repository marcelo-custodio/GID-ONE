from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from cryptography.hazmat.primitives import hashes
import os

def resumo_criptografico(path):
    digest = hashes.Hash(hashes.SHA256())
    f = open(path, 'rb')
    digest.update(f.read())
    f.close()
    return digest.finalize()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp_files'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(path)
        file.save(path)
        summary = resumo_criptografico(path)
        print(summary)
        os.remove(path)
        return render_template('index.html', resumo = summary.hex(), nome=filename)
    else:
        return render_template('index.html', resumo='', nome='')

if __name__ == '__main__':
    app.run(debug=True)