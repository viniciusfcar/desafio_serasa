# Use uma imagem base oficial de Python
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /usr/src/app

# Copia o arquivo requirements.txt e instala dependências do sistema e Python
COPY ./requirements.txt /usr/src/app/
RUN apt-get update && apt-get install -y libpq-dev gcc \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia o script de entrada e dá permissão de execução
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Copia todos os arquivos do projeto
COPY . .

# Define o entrypoint
ENTRYPOINT ["./entrypoint.sh"]
