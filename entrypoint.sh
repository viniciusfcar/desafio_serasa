#!/bin/sh

python src/manage.py makemigrations # Gera arquivos de migração
python src/manage.py migrate  # Aplica as migrações
exec "$@"  # Executa o comando final
