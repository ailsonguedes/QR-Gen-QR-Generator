from flask import Flask, render_template, request
from flasgger import Swagger
from flask_cors import CORS
from api.route.qrgen import qrgen_api


def create_app():
    """
    Cria e configura a aplicação Flask.

    - Registra o blueprint `qrgen_api` com prefixo `/api` (rotas do gerador de QR).
    - Inicializa o Swagger (documentação automática).
    - Define a rota raiz `/` que renderiza o template `index.html`.

    Retorna a instância do app pronta para ser usada pelo servidor ou testes.
    """
    app = Flask(__name__)

    # Configuração mínima para o Swagger (pode ser estendida)
    app.config['SWAGGER'] = {
        'title': 'QR Gen API (FLASK)',
    }
    swagger = Swagger(app)

    ## Inicializa outras configurações a partir do arquivo `config.py`
    # (por exemplo: chaves, variáveis de ambiente, configurações de produção etc.)
    app.config.from_pyfile('config.py')

    # Isso funciona como um "catch-all"
    CORS(app)

    # registra o blueprint com prefixo '/api' -> rota completa: '/api/qrgen'
    # Blueprints são uma forma de organizar rotas em módulos (boa prática)
    app.register_blueprint(qrgen_api, url_prefix='/api')

    # Rota principal do site (GET): renderiza o template index.html
    @app.route('/', methods=['GET'])
    def index():
        # Retorna a página HTML com um formulário simples para gerar QR
        return render_template('index.html')

    return app

app = create_app()

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
