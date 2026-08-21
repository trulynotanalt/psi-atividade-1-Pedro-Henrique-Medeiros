from flask import Flask, request, render_template, url_for
from flask import redirect
import models

app = Flask(__name__)

app.secret_key = "romerito"

@app.route('/', methods=['GET', 'POST'])
def livraria():
    return render_template('livraria.html', livros=models.buscar_livros(), resenhas=models.resenhas_do_livro)


@app.route('/livro/<int:livro_id>')
def method_name():
    pass

@app.route('/login')
def login():
    return render_template('login.html')


