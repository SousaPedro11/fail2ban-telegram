# Fail2ban Telegram RestAPI

Rest API feita em Flask para notificar via Telegram os eventos do Fail2ban.

## Requisitos
* Aplicação com arquitetura REST
* Receber uma requisição do tipo POST
* Utilizar um bot para comunicar com o Telegram
* Notificar no grupo o evento de acordo com o formato de entrada definido
* Executar em container Docker

## Tecnologias e Recursos
* Python 3.8
* pip 20.0.2
* Flask 1.1
* python-dotenv 0.12.0
* Flask-HTTPAuth 3.3.0
* Flask-RESTful 0.3.8
* python-telegram-bot 12.4.2
* requests 2.23.0
* pytest 5.4.1
* gunicorn 20.0.4
