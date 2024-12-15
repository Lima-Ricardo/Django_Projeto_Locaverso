Django - Configuração de Projeto (Simples)
Este guia ajuda a configurar um projeto Django básico, incluindo a criação do ambiente virtual, instalação das dependências, configuração do banco de dados, arquivos estáticos e integração com o Bootstrap.

Configurações Iniciais
Requisitos
Certifique-se de que o Python está instalado em seu ambiente.

Criar o Ambiente Virtual (Linux/Windows)

Windows
python -m venv .venv
source .venv/Scripts/activate  # Ativar ambiente

Linux
python3 -m venv .venv
source .venv/bin/activate  # Ativar ambiente

Instalar Dependências
Instale os pacotes necessários para o projeto:
pip install -r requirements.txt

caso haja algum erro abra o arquivo requiriments.txt olhe para ver o nome do pacote e faça o seguinte:
pip install <nome do pacote>


======================================================================================


Criando o Projeto Django

django-admin startproject core .

O parâmetro . indica que os arquivos do projeto serão criados na raiz da pasta, sem criar uma subpasta.

Testar a Aplicação
Para testar se o projeto foi criado corretamente, execute o servidor local:

python manage.py runserver

Acesse o servidor local através de http://127.0.0.1:8000 no seu navegador.

Configurar Arquivos Estáticos e Media
No arquivo settings.py:

import os

# Configurações de diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Arquivos de mídia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True



No arquivo urls.py:

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Configuração para arquivos estáticos e de mídia
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Criando um Aplicativo Django
Agora, vamos criar um aplicativo Django chamado locaverso. Você pode substituir o nome por qualquer outro, se desejar.

python manage.py startapp locaverso

Registrar o Aplicativo em settings.py
Abra o arquivo settings.py e adicione o aplicativo recém-criado à lista INSTALLED_APPS:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'locaverso',  # Adicionar o app recém-criado
]

Configuração do Template Base e Integração com Bootstrap
Configuração do Bootstrap
Para integrar o Bootstrap ao seu projeto, basta incluir os links para o CSS e o JS do Bootstrap no arquivo HTML base.

Exemplo de base.html:

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Aplicação Django</title>

    <!-- CSS do Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>
<body>

    <!-- Conteúdo principal -->
    {% block content %}
    {% endblock %}

    <!-- JS do Bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
</body>
</html>


Com isso, o Bootstrap será integrado ao seu projeto e você poderá usar seus componentes e estilos de maneira fácil e rápida.



