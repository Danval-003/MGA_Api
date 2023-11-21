from twilio.rest import Client


def enviar_sms(trabajador, muertes):
    to = '+502 59504420'
    mensaje = f'El trabajador {trabajador} ha reportado {muertes} muertes en su galera.'
    # Reemplaza con tus credenciales de Twilio
    account_sid = 'ACfe510db47f7ac9c65f6166c81a048f2c'
    auth_token = '2f7254b736083b64638951c3b78920d7'
    twilio_phone_number = '+14782174439'

    # Crea un cliente de Twilio
    client = Client(account_sid, auth_token)

    try:
        # Envía el mensaje
        message = client.messages.create(
            body=mensaje,
            from_=twilio_phone_number,
            to=to
        )
        print(f'Mensaje enviado con SID: {message.sid}')
    except Exception as e:
        print(f'Error al enviar el mensaje: {str(e)}')
