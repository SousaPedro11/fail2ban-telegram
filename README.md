# Fail2ban Telegram RestAPI

Rest API feita em Flask para notificar via Telegram os eventos do Fail2ban.

## Requisitos
* Aplicação com arquitetura REST
* Receber uma requisição do tipo POST
* Utilizar um bot para comunicar com o Telegram
* Notificar no grupo o evento de acordo com o formato de entrada definido
* Executar em container Docker

## Tecnologias e Recursos
* [Python 3.8.2](https://www.python.org/)
* [pip 20.0.2](https://pip.pypa.io/en/stable/)
* [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
* [python-dotenv 0.12.0](https://github.com/theskumar/python-dotenv)
* [Flask-HTTPAuth 3.3.0](https://flask-httpauth.readthedocs.io/en/latest/)
* [Flask-RESTful 0.3.8](https://flask-restful.readthedocs.io/en/latest/)
* [python-telegram-bot 12.4.2](https://python-telegram-bot.readthedocs.io/en/stable/)
* [requests 2.23.0](https://requests.readthedocs.io/en/master/)
* [pytest 5.4.1](https://docs.pytest.org/en/latest/contents.html)
* [gunicorn 20.0.4](https://gunicorn.org/)

## Preparação do Ambiente
### Criar os arquivos contendo as variáveis de ambitente
* Copiar os templates de arquivos:
```shell script
cp flaskenv_example .flaskenv && cp env_example .env
```
* Substituir os valores correspondentes às variáveis

### Para executar em localhost na própria máquina
* Instale o Python 3
* Instale o pip
* Atualize o pip
* Instale o openssl-dev
* Crie o ambiente virtual com:
```shell script
python -m venv venv
```
* Ative o ambiente virtual:
```shell script
source ./venv/bin/activate
```
* Instale os pacotes necessários com o pip:
```shell script
pip install -r requirements.txt
```

### Em Docker
* Instale o Docker e Docker-compose
* Crie a imagem a partir do DOCKERFILE (dockerfile_fail2ban_iec):
```shell script
docker build -f ./dockerfile_fail2ban_iec -t fail2ban:alpine .
```

## Executar a aplicação
### Na própria máquina pelo terminal
* Sem o servidor WSGI
```shell script
flask run
```
ou
```shell script
python -m flask run
```

* Com o servidor WSGI
```shell script
gunicorn --workers=5 --bind=0.0.0.0:5000 --access-logfile - --error-logfile - 'fail2ban:create_app()'
```
ou execute o *startup.sh* (deve estar habilitado para execução)
```shell script
./startup.sh
```
### Em docker (após criada a imagem)
```shell script
docker run --name fail2ban-telegram -p 5000:5000 --restart=unless-stopped -d fail2ban:alpine
```
### Em docker-compose
* Para criar e executar a aplicalçao
```shell script
docker-compose -f fail2ban_iec.yml up --build -d --remove-orphans
```
* Para derrubar e remover container + imagem
```shell script
docker-compose -f fail2ban_iec.yml down --rmi all -v --remove-orphans
```
