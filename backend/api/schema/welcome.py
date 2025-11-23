"""
Compatibilidade com nome antigo `WelcomeSchema`.

Reexporta `QrgenSchema` de `api.schema.qrgen` para não quebrar importações
existentes que ainda usem o nome antigo.
"""

from api.schema.qrgen import QrgenSchema as WelcomeSchema