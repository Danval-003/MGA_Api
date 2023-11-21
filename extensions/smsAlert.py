from twilio.rest import Client


def enviar_sms(trabajador, muertes):
    with open('../credentials.txt', 'r') as archivo:
        account_sid = archivo.readline()
        auth_token = archivo.readline()
        twilio_phone_number = archivo.readline()
    to = '+502 59504420'
    mensaje = f'El trabajador {trabajador} ha reportado {muertes} muertes en su galera.'
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
