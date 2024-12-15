# Django Configuracao de Projeto (Simples)

# Configuracoes Iniciais

## Ambiente Virtual Linux/Windows

# Lembrando… Precisa ter Python instalado no seu ambiente.

# Criar o ambiente virtual Linux/Windows

# Windows
python -m venv .venv
source .venv/Scripts/activate  # Ativar ambiente

# Instalar os pacotes necessarios
pip install django
pip install pillow

# Criar o arquivo requirements.txt
pip freeze > requirements.txt

# Criando o Projeto

# "core" é nome do seu projeto e quando colocamos um "." depois do nome do projeto significa que é para criar os arquivos na raiz da pasta.
# Assim não cria subpasta do projeto.
django-admin startproject core .

# Testar a aplicacao
python manage.py runserver

# Configurar Settings e Arquivos Static

# Vamos configurar nossos arquivos static

# No arquivo settings.py:
import os

# base_dir config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Internationalization
# Se quiser deixar em PT BR
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# No arquivo myapp/urls.py:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Adicionar
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Adicionar

# Criando Aplicativo

# Vamos criar nosso aplicativo no Django.
# Para criar a aplicacao no Django rode comando abaixo.
# "locaverso" é nome do seu App mas pode ser qualquer 1.
python manage.py startapp locaverso

# Agora precisamos registrar nossa aplicacao no INSTALLED_APPS localizado em settings.py.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'locaverso',
]

# Template Base e Bootstrap Configuracao

# Bootstrap configuracao
# Doc: https://getbootstrap.com/docs/5.2/getting-started/introduction/

# Com Base na documentacao para utilizar os recursos Bootstrap basta adicionar as tags de CSS e JS. No HTML da Pagina Base.

# HTML do template base (base.html):
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Aplicacao Django</title>

    <!-- CSS do Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>
<body>

    <!-- Conteudo principal -->
    {% block content %}
    {% endblock %}

    <!-- JS do Bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
</body>
</html>
# Django_Projeto_Locaverso
# Django_Projeto_Locaverso
# Django_Projeto_Locaverso
# Django_Projeto_Locaverso
# Django_Projeto_Locaverso
