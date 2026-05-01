import os

from dotenv import load_dotenv

load_dotenv()

# -- Настройка адресов
WEB_CLIENT_HOST='localhost'
WEB_CLIENT_PORT=8080
SERVER_HOST = 'localhost'
SERVER_PORT = 18861


# -- Настройка адресов для клиента / продакшена
PUBLIC_URL='http://localhost:8080'
APP_NAME = 'Vivid RPG'

MODULE_LOG_FILE = 'vivid.log'
SERVER_LOG_FILE = 'server.log'

load_dotenv()

globals().update(os.environ)