from flask import Flask, request, redirect, render_template, url_for
import random
import string

app = Flask(__name__)

# Armazenamento em memória
url_mapping = {}

# Gera um código curto aleatório
def gerar_codigo(tamanho=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

@app.route('/', methods=['GET', 'POST'])
def index():
    url_encurtada = None

    if request.method == 'POST':
        url_original = request.form.get('url')
        if url_original:
            codigo = gerar_codigo()
            while codigo in url_mapping:
                codigo = gerar_codigo()
            url_mapping[codigo] = url_original
            url_encurtada = request.host_url + codigo

    return render_template('index.html', url_encurtada=url_encurtada)

@app.route('/<codigo>')
def redirecionar(codigo):
    url_original = url_mapping.get(codigo)
    if url_original:
        return redirect(url_original)
    return "URL não encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)
