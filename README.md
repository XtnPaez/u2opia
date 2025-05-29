# U2opia - El Bot de Prompts para la IA

[![GitHub](https://img.shields.io/github/stars/XtnPaez/u2opia?style=social)](https://github.com/XtnPaez/u2opia)

**Objetivo:** Crear un bot de Twitter (X) que publique prompts de alta calidad para la generación de contenido con Inteligencia Artificial (IA).

**Cuenta de Twitter (X):** [@U2opia\_x](https://twitter.com/U2opia_x)
**Correo Electrónico (para soporte, feedback, etc.):** u2opia.mail@gmail.com

**Visión:** Inspirar y ayudar a creadores, desarrolladores y entusiastas de la IA a explorar las posibilidades del lenguaje y la generación de contenido a través de prompts efectivos.

**Tecnologías:**

*   **Lenguaje de Programación:** Python
*   **API:** Twitter API v2
*   **Librería:**  (Por definir, pero probablemente Tweepy o una librería similar)
*   **Almacenamiento de Prompts:** Archivo `.txt`
*   **Programación de Tareas (Scheduler):**  GitHub Actions

**Estructura del Proyecto:**

1.  **`main.py`:**  El script principal del bot, que realizará las siguientes tareas:
    *   Leer un prompt del archivo `.txt`.
    *   Autenticarse en Twitter (X) usando la API.
    *   Publicar el prompt como un tuit.
    *   Gestionar la selección del siguiente prompt (evitando repeticiones).
2.  **`prompts.txt`:**  Un archivo de texto que contiene una lista de prompts. Cada prompt estará en una línea separada.
3.  **`requirements.txt`:** (Por definir, se incluirán las dependencias necesarias - ejemplo: tweepy, etc.).
4.  **`.github/workflows/`:** Contendrá el archivo de flujo de trabajo (workflow) de GitHub Actions para programar la ejecución del bot.

**Plan de Implementación (Etapas):**

1.  **[En Progreso] Inicialización del Repositorio:** Este `README.md`. Creación inicial del script `main.py` y el archivo `prompts.txt`.
2.  **Desarrollo del Script Principal:**  Escribir el código Python para leer, autenticarse, publicar y gestionar los prompts.
3.  **Pruebas y Depuración:**  Probar el script localmente y corregir errores.
4.  **Configuración de GitHub Actions:** Crear el workflow para automatizar la ejecución del bot cada 6 horas.
5.  **Puesta en Marcha y Monitoreo:**  Lanzar el bot en Twitter (X) y monitorear su funcionamiento, el engagement y la calidad de los prompts.
6.  **Iteración y Mejora Continua:**  Agregar nuevos prompts, refinar el código, y analizar los resultados para optimizar el bot y la estrategia de contenidos.

**Próximos Pasos (Listado de Tareas):**

*   [ ] Definir el formato de los prompts en `prompts.txt`.
*   [ ] Escribir el código Python en `main.py`.
*   [ ] Crear el archivo `requirements.txt`.
*   [ ] Escribir el workflow de GitHub Actions.
*   [ ] Probar y depurar el código.

**Licencia:** (Por definir, pero se sugiere una licencia de software libre como MIT o Apache 2.0)

---

**Prompt para Iniciar un Nuevo Chat (Desarrollo Etapa 1):**

"Hola, soy el creador de @U2opia_x, un bot de Twitter que publica prompts para IA. Acabo de crear un repositorio en GitHub (XtnPaez/u2opia) y necesito tu ayuda para el desarrollo de la Etapa 1. Ya tengo las cuentas de Twitter y correo, y el `README.md` inicial.

**Objetivo Específico de esta Conversación:**

**Ayúdame a escribir el código de `main.py` en Python, que deberá:**

1.  **Leer un prompt aleatorio del archivo `prompts.txt`.** (Asume un formato simple: un prompt por línea).
2.  **Autenticarse en Twitter (X) usando la API v2** (necesito ayuda con el código de autenticación y el manejo de errores).
3.  **Publicar el prompt como un tuit.**
4.  **Gestionar la selección del siguiente prompt, evitando repeticiones.** (Piensa en diferentes estrategias: borrar el prompt usado, marcarlo, etc.).
5.  **Manejar los errores** (ej. errores de API, problemas con el archivo .txt).
6.  **Documentar el código con comentarios claros.**

**Por favor, crea un archivo Python `main.py` con el código y explica cada sección y por qué la implementaste de esa manera. Podemos ir iterando y ajustando el código en esta conversación.**

¡Comencemos con la magia de la programación! ¿Estás listo para crear el bot de prompts?"
