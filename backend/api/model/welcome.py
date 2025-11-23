"""
Compatibilidade com nome antigo `WelcomeModel`.

Este arquivo apenas reexporta a classe nova `QrgenModel` definida em
`api.model.qrgen` para evitar que importações antigas que usem
`from api.model.welcome import WelcomeModel` quebrem.
"""

from api.model.qrgen import QrgenModel as WelcomeModel
