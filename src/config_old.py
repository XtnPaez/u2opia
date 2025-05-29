import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
# Asegúrate de que el archivo .env esté en el directorio raíz del proyecto
# o dos niveles arriba si ejecutas desde src/
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if not os.path.exists(dotenv_path):
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env') # Para cuando se corre desde otro sitio

load_dotenv(dotenv_path=dotenv_path)

# Credenciales de la API de Twitter
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Rutas a los archivos de datos
PROMPTS_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'prompts.txt')
USED_PROMPTS_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'used_prompts.txt')

# Configuración de logs
LOGS_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
LOG_FILE_PATH = os.path.join(LOGS_DIR, 'bot.log')

# Asegurarse de que el directorio de logs exista
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Validación básica de credenciales (opcional pero recomendado)
if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    raise ValueError(
        "Una o más credenciales de Twitter no están configuradas. "
        "Verifica tu archivo .env y src/config.py"
    )