"""
Roteiro de rotas para geração de QR codes.

Este arquivo contém a rota que recebe um texto via POST e devolve uma imagem PNG
com o QR code correspondente. Está comentado com explicações em português
para facilitar o estudo de quem está começando.
"""

from http import HTTPStatus
from flask import Blueprint, request, send_file, jsonify
from flasgger import swag_from
from api.model.qrgen import QrgenModel
from api.schema.qrgen import QrgenSchema
from io import BytesIO

import qrcode


# Nome da variável do blueprint exposta ao aplicativo
# O usuário pediu especificamente que o nome fosse `qrgen_api`.
qrgen_api = Blueprint('qrgen_api', __name__)

@qrgen_api.route('/qrgen', methods=['POST'])
@swag_from({
    # Informação básica para o Swagger: exemplo de resposta 200 e o schema usado
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Gera um QR code a partir de texto e retorna imagem PNG',
            'schema': QrgenSchema
        }
    }
})
def qrgen():
    """
    Endpoint que gera um QR code e devolve a imagem PNG.

    Passo a passo (fluxo do POST):
    1. Lê o campo de formulário `data` enviado pelo cliente.
    2. Valida que `data` não está vazio; se estiver, retorna 400 com mensagem.
    3. Usa a biblioteca `qrcode` para criar uma imagem do QR.
    4. Armazena a imagem em memória (`BytesIO`) para não criar arquivos no disco.
    5. Retorna a imagem com `send_file` e cabeçalhos apropriados.

    Observações para iniciantes:
    - `request.form` lê dados enviados como `x-www-form-urlencoded` ou `form-data`.
    - `BytesIO` funciona como um arquivo em memória; útil para enviar binários.
    - `send_file` cuida dos cabeçalhos HTTP (Content-Type, Content-Disposition).
    """

    # Lê o campo 'data' do formulário
    data = request.form.get('data')

    # Validação simples: se não houver dados, retorna erro 400
    if not data:
        return jsonify({"error": "field 'data' is required"}), HTTPStatus.BAD_REQUEST

    # Configura o gerador de QR code
    qr = qrcode.QRCode(
        version=1,  # controla o tamanho do QR (1 é pequeno)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # tamanho de cada quadradinho
        border=4,     # borda ao redor do QR
    )

    # Adiciona o texto ao QR e gera a imagem
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Usa BytesIO para manter a imagem em memória
    qr_code_io = BytesIO()
    img.save(qr_code_io)
    qr_code_io.seek(0)

    # Retorna a imagem como arquivo PNG para download
    return send_file(
        qr_code_io,
        mimetype='image/png',
        as_attachment=True,
        download_name='qrcode.png',
    )


# Nota: se desejar manter um endpoint GET que devolva um JSON simples (por exemplo
# para documentação ou para testes automáticos), você poderia adicionar outro
# route aqui. No entanto o objetivo atual é ter apenas o POST que devolve a imagem.
