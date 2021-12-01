import re
from flask import Flask, flash, render_template, request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from cryptography.hazmat.primitives import hashes
from datetime import datetime as dt
import os

def resumo_criptografico(path):
    digest = hashes.Hash(hashes.SHA256())
    f = open(path, 'rb')
    digest.update(f.read())
    f.close()
    return digest.finalize()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumo.db'
app.config['UPLOAD_FOLDER'] = '/temp_files'
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    name = db.Column(db.Text, nullable=False, default='')
    summary = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Sem arquivos selecionados')
            return render_template('index.html')
        
        for file in request.files:
            filename = secure_filename(file)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # TO_DO resumo criptografico
            return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)