#!/usr/bin/env bash
# Interrompe em caso de erro
set -o errexit

# Instala as dependências
pip install -r requirements.txt

# Reúne os arquivos do Swagger
python manage.py collectstatic --no-input

# Cria as tabelas no banco de dados da nuvem
python manage.py migrate
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminsenha')
    print('Superusuario criado com sucesso!')
else:
    print('Superusuario ja existe.')
"