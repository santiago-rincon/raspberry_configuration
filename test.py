from twilio.rest import Client

# Reemplaza con tus credenciales obtenidas de Twilio.
account_sid = 'ACc8e4dea0c707eaaf1e0c2791bed15864'
auth_token = '612898e179a9ee270347b77799967b46'
twilio_phone_number = '+12184293654'
destinatario = '+573006099776'
mensaje = 'Hola, este es un mensaje de prueba desde Python y Twilio.'

# Crea el cliente de Twilio.
client = Client(account_sid, auth_token)

# Envía el SMS.
mensaje_enviado = client.messages.create(
    body=mensaje,
    from_=twilio_phone_number,
    to=destinatario
)

# Verifica si el mensaje se envió correctamente.
if mensaje_enviado.sid:
    print("Mensaje enviado con éxito.")
else:
    print("Error al enviar el mensaje.")
