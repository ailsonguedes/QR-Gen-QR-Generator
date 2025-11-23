# Usa uma imagem base Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependência do Pipenv
COPY Pipfile Pipfile.lock /app/

# Instala o Pipenv e as dependências
RUN pip install pipenv && pipenv install --system --dev

# Copia o restante do código
COPY . /app

# Expõe a porta que o Flask vai usar (ex: 5000)
EXPOSE 5000

# Comando para rodar o Flask
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
# Alternativa simples para desenvolvimento: CMD ["python", "app.py"]
