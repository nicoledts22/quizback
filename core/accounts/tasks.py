from celery import shared_task
from django.core.mail import send_mail
from .models import CustomUser
import pika  # Importar la librería pika

@shared_task
def enviar_correo_bienvenida():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar una cola en RabbitMQ
    channel.queue_declare(queue='usuario_registrado')

    def callback(ch, method, properties, body):
        usuario_id = int(body)
        try:
            usuario = CustomUser.objects.get(id=usuario_id)
            mensaje = f"Bienvenido/a, {usuario.nombre}! Gracias por registrarte."
            send_mail('Bienvenido/a!', mensaje, 'tu@email.com', [usuario.email])
        except Usuario.DoesNotExist:
            pass  # Manejar si el usuario no existe

    # Consumir mensajes de la cola
    channel.basic_consume(queue='usuario_registrado', on_message_callback=callback, auto_ack=True)

    # Empezar a consumir mensajes
    channel.start_consuming()