from flask_marshmallow import Schema
from marshmallow.fields import Str


class QrgenSchema(Schema):
    """
    Schema (Marshmallow) para serializar o modelo `QrgenModel`.

    Define os campos que serão expostos quando convertermos o modelo
    para JSON. Aqui só há um campo `message` para manter o exemplo simples.
    """

    class Meta:
        # Campos que serão incluídos no JSON serializado
        fields = ["message"]

    message = Str()
