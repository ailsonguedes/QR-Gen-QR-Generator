from app import create_app

app = create_app()
# Fazer com que exceções dentro do app de teste propaguem para aqui
app.testing = True

client = app.test_client()

try:
    resp = client.post('/api/qrgen', data={'data': 'teste'})
    print('STATUS:', resp.status_code)
    print('HEADERS:', dict(resp.headers))
    print('CONTENT-LENGTH:', len(resp.data))
    # mostrar os primeiros bytes para confirmar que é imagem
    print('FIRST-BYTES:', resp.data[:20])
except Exception as e:
    import traceback
    traceback.print_exc()
    print('EXCEPTION:', e)
