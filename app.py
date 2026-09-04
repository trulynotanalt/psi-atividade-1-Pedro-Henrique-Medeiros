from flask import Flask, request, render_template, url_for
from flask import redirect

import models
from models import buscar_livro, resenhas_do_livro, buscar_livros
app = Flask(__name__)

app.secret_key = "romerito"

@app.route('/')
def index():
    q = request.args.get('q','')
    livros = models.buscar_livros(q)
    return render_template('index.html', livros=livros, q=q)


@app.route('/livro/<int:livro_id>')
def detalhe(livro_id):
    livro = models.buscar_livro(livro_id)

    resenhas = models.resenhas_do_livro(livro_id)
    return render_template('livro.html', livro=livro, resenhas=resenhas)

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        

    return render_template('login.html')


