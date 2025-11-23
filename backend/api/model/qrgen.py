class QrgenModel:
    """
    Modelo simples que representa a mensagem de boas-vindas.

    Mantive este modelo minimalista para compatibilidade com o schema usado
    em documentações ou retornos JSON. O objetivo aqui é ter uma classe de
    exemplo que pode ser serializada para JSON.
    """

    def __init__(self):
        # Mensagem padrão — você pode alterar para algo relacionado ao gerador de QR
        self.message = "Hello World!"
