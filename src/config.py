import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
# Esta lógica de búsqueda de .env está bien, la podemos mantener
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if not os.path.exists(dotenv_path):
    # Esto es útil si ejecutas el script desde dentro de la carpeta src, por ejemplo.
    # Para GitHub Actions, el .env se creará en la raíz, por lo que el primer path debería funcionar.
    alternate_dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    if os.path.exists(alternate_dotenv_path):
        dotenv_path = alternate_dotenv_path
    # Podríamos incluso añadir una comprobación para la raíz si CWD es la raíz
    elif os.path.exists('.env'): # Si .env está en el directorio de trabajo actual
        dotenv_path = '.env'


load_dotenv(dotenv_path=dotenv_path)


# Credenciales de la API de Twitter
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# -------------------- INICIO DE LA SECCIÓN MODIFICADA --------------------
# Rutas a los archivos de datos
# Asumimos que el script se ejecuta desde la raíz del proyecto o que src/ es un subdirectorio
# Esto es más robusto para GitHub Actions donde el CWD suele ser la raíz del repo
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # Obtiene la ruta raíz del proyecto

PROMPTS_FILE_PATH = os.path.join(BASE_DIR, 'data', 'prompts.txt')
USED_PROMPTS_FILE_PATH = os.path.join(BASE_DIR, 'data', 'used_prompts.txt')

# Configuración de logs
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE_PATH = os.path.join(LOGS_DIR, 'bot.log')

# Asegurarse de que el directorio de logs exista
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
# -------------------- FIN DE LA SECCIÓN MODIFICADA --------------------

# Validación básica de credenciales (opcional pero recomendado)
if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    # En GitHub Actions, esto podría fallar si los secrets no están bien configurados.
    # Podríamos querer un logging más explícito aquí en lugar de solo raise ValueError.
    # Por ahora, lo mantenemos así.
    # print("ERROR: Una o más credenciales de Twitter no están configuradas. Verifica tus secretos/variables de entorno.")
    raise ValueError(
        "Una o más credenciales de Twitter no están configuradas. "
        "Verifica tu archivo .env o los secrets de GitHub Actions."
    )