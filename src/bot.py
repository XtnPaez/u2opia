import tweepy
import random
import os
import logging
from config import (
    API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
    PROMPTS_FILE_PATH, USED_PROMPTS_FILE_PATH, LOG_FILE_PATH
)

# --- Configuración de Logging ---
# Intenta establecer la codificación para la salida estándar si es posible
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    # Esto podría fallar en versiones antiguas de Python o ciertos entornos
    pass # No es crítico para la funcionalidad del bot, solo para la visualización en consola

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, encoding='utf-8'), # Añadir encoding aquí
        logging.StreamHandler()
    ]
)

# --- Funciones de Manejo de Prompts ---

def load_prompts(filepath):
    """Carga todos los prompts desde un archivo."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            prompts = [line.strip() for line in f if line.strip()]
        if not prompts:
            logging.warning(f"El archivo de prompts '{filepath}' está vacío o no contiene prompts válidos.")
            return []
        return prompts
    except FileNotFoundError:
        logging.error(f"Archivo de prompts no encontrado: {filepath}")
        return []
    except Exception as e:
        logging.error(f"Error al cargar prompts desde '{filepath}': {e}")
        return []

def load_used_prompts(filepath):
    """Carga los prompts ya utilizados desde un archivo."""
    if not os.path.exists(filepath):
        return set() # Si el archivo no existe, no hay prompts usados
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            used_prompts = {line.strip() for line in f if line.strip()}
        return used_prompts
    except Exception as e:
        logging.error(f"Error al cargar prompts usados desde '{filepath}': {e}")
        return set() # En caso de error, mejor asumir que no hay usados para no bloquear

def save_used_prompt(prompt, filepath):
    """Guarda un prompt en el archivo de prompts utilizados."""
    try:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(prompt + '\n')
    except Exception as e:
        logging.error(f"Error al guardar prompt usado en '{filepath}': {e}")

def get_random_available_prompt():
    """
    Obtiene un prompt aleatorio que no haya sido utilizado.
    Si todos los prompts han sido utilizados, devuelve None y un mensaje.
    Si se han usado todos, opcionalmente podría resetear la lista de usados.
    """
    all_prompts = load_prompts(PROMPTS_FILE_PATH)
    if not all_prompts:
        logging.error("No hay prompts disponibles en el archivo principal.")
        return None

    used_prompts = load_used_prompts(USED_PROMPTS_FILE_PATH)
    
    available_prompts = [p for p in all_prompts if p not in used_prompts]

    if not available_prompts:
        logging.warning("Todos los prompts han sido utilizados.")
        # Opcional: Resetear la lista de prompts usados si se desea ciclar
        # logging.info("Reseteando la lista de prompts usados.")
        # open(USED_PROMPTS_FILE_PATH, 'w').close() # Borra el contenido
        # available_prompts = all_prompts # Volver a usar todos
        # if not available_prompts: # Doble check por si all_prompts estaba vacío
        #     return None
        return None # Por ahora, simplemente no devuelve nada si se acabaron

    return random.choice(available_prompts)

# --- Funciones de Twitter ---

def get_twitter_client():
    """Autentica y devuelve un cliente de Twitter API v2."""
    try:
        client = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )
        # Probar autenticación (opcional, pero bueno para verificar)
        # me = client.get_me()
        # logging.info(f"Autenticado en Twitter como: @{me.data.username}")
        return client
    except tweepy.TweepyException as e:
        logging.error(f"Error de autenticación con Twitter: {e}")
        return None
    except Exception as e:
        logging.error(f"Error inesperado al crear cliente de Twitter: {e}")
        return None


def post_tweet(client, text_to_tweet):
    """Publica un tuit."""
    if not client:
        logging.error("Cliente de Twitter no inicializado. No se puede tuitear.")
        return False
    if not text_to_tweet or len(text_to_tweet) > 280:
        logging.error(f"Texto del tuit inválido o demasiado largo: '{text_to_tweet}'")
        return False
    
    try:
        response = client.create_tweet(text=text_to_tweet)
        logging.info(f"Tuit publicado exitosamente! ID: {response.data['id']}")
        # print(f"Tweet ID: {response.data['id']}")
        # print(f"Tweet text: {response.data['text']}")
        return True
    except tweepy.Forbidden as e:
        # Error 403: Puede ser por contenido duplicado, entre otros.
        logging.error(f"Error Forbidden (403) al tuitear: {e}. ¿Contenido duplicado o permisos insuficientes?")
        if "duplicate content" in str(e).lower():
            logging.warning("El error parece ser por contenido duplicado. Revisa tus prompts.")
        return False
    except tweepy.TooManyRequests as e:
        # Error 429: Rate limit
        logging.error(f"Error TooManyRequests (429) al tuitear: {e}. Has alcanzado el límite de la API.")
        return False
    except tweepy.TweepyException as e:
        logging.error(f"Error de Tweepy al publicar el tuit: {e}")
        return False
    except Exception as e:
        logging.error(f"Error inesperado al publicar el tuit: {e}")
        return False

# --- Función Principal del Bot ---

def main():
    logging.info("🤖 Iniciando U2opia Bot...")

    prompt_to_tweet = get_random_available_prompt()

    if not prompt_to_tweet:
        logging.warning("No hay prompts disponibles para tuitear o error al cargarlos. Terminando.")
        return

    logging.info(f"Prompt seleccionado: '{prompt_to_tweet}'")

    twitter_client = get_twitter_client()
    if not twitter_client:
        logging.error("No se pudo obtener el cliente de Twitter. Terminando.")
        return

    if post_tweet(twitter_client, prompt_to_tweet):
        save_used_prompt(prompt_to_tweet, USED_PROMPTS_FILE_PATH)
        logging.info(f"Prompt '{prompt_to_tweet}' marcado como usado.")
    else:
        logging.error(f"No se pudo publicar el prompt: '{prompt_to_tweet}'. No se marcará como usado.")

    logging.info("🤖 U2opia Bot ha finalizado su ejecución.")

if __name__ == "__main__":
    main()