
# Este arquivo foi mantido para compatibilidade com importações antigas.
# Agora a implementação real está em `api.route.qrgen`.
from api.route.qrgen import qrgen_api

# Expõe `home_api` para não quebrar código que ainda importe esse nome.
home_api = qrgen_api

