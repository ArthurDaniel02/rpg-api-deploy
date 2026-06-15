#!/usr/bin/env bash
# Interrompe em caso de erro
set -o errexit

# Instala as dependências
pip install -r requirements.txt

# Reúne os arquivos do Swagger
python manage.py collectstatic --no-input

# Cria as tabelas no banco de dados da nuvem
python manage.py migrate