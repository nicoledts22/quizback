Adjunto por acá el trabajo realizado a nivel de backend para el sistema de Quiz Interactivo. Se realizó un proyecto compuesto de dos aplicaciones "Quiz" y "Accounts".
La aplicación de Quiz, se encarga de generar un modelo que permite la creación, edición y eliminación de Quizzes, Preguntas y Respuestas de los mismos. Para generar un Quiz, es necesario crear la categoría, preguntas y respuestas del mismo.
La aplicación de Accounts, se encarga del sistema de registro de usuarios convencional brindado por Django, sumado con el campo de email, para el desarrollo del llamado a la cola de RabbitMQ y el generador de tareas en segundo plano de Celery. Ambos trabajan en conjunto para el envío de un correo de bienvenida al momento de registrar un usuario.

Para ejecutar este proyecto, es necesario la creación del respectivo ambiente virtual (preferiblemente en Python 3.8), así como tener disponible el broker de RabbitMQ instalado, en conjuno de la lista de los requerimientos, encontrados en el archivo requirements.txt

Para el funcionamiento correcto del sistema de envío de correos, es necesario configurar manualmente el mismo en la plantilla ubicada en el directorio settings.py
