"""
Testes unitários para o endpoint `/api/qrgen`.

Este arquivo usa o módulo `unittest` da stdlib e o test client do Flask
para exercitar a rota sem precisar subir o servidor HTTP.

Cada teste contém comentários em português explicando o objetivo e o que
estamos verificando — útil para estudo passo a passo.
"""

from unittest import TestCase
from app import create_app
import io


class TestQrgen(TestCase):
    """TestCase com dois cenários básicos:
    - test_qrgen_post_returns_png: envia texto e espera uma imagem PNG de resposta
    - test_qrgen_missing_data_returns_400: envia sem campo `data` e espera 400
    """

    def setUp(self):
        # Cria a aplicação em modo de teste e obtém o test_client
        # O test_client permite simular requisições HTTP internas
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_qrgen_post_returns_png(self):
        """
        Envia um POST válido para `/api/qrgen` com o campo form 'data'.

        Verificações:
        - status code 200
        - header Content-Type igual a 'image/png'
        - corpo não vazio (tem bytes de imagem)
        """

        resp = self.client.post('/api/qrgen', data={'data': 'teste unitario'})

        # A rota devolve imagem; garantimos o status
        self.assertEqual(resp.status_code, 200)

        # Verifica o tipo de conteúdo
        self.assertIn('image/png', resp.headers.get('Content-Type', ''))

        # Conteúdo deve existir e começar com bytes característicos de PNG
        self.assertGreater(len(resp.data), 0)
        # PNG files start with the following 8 bytes
        self.assertTrue(resp.data.startswith(b'\x89PNG\r\n\x1a\n'))

    def test_qrgen_missing_data_returns_400(self):
        """
        Envia um POST sem o campo `data` e espera que a API retorne 400 com JSON explicando o erro.

        Isso valida o tratamento de entrada (input validation) do endpoint.
        """

        resp = self.client.post('/api/qrgen', data={})

        # Esperamos erro de cliente
        self.assertEqual(resp.status_code, 400)

        # A resposta é JSON com a chave 'error'
        json_data = resp.get_json()
        self.assertIsInstance(json_data, dict)
        self.assertIn('error', json_data)
