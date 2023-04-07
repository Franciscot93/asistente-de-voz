import pyttsx3
import speech_recognition as sr
'''
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
'''
import datetime



# transformar audio a texto

def transformar_audio_en_texto():
    # recognizer en variable
    reco = sr.Recognizer()

    # configuracion de microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        reco.pause_threshold = 0.8

        # info de que comenzo la grabacion
        print("ya puedes hablar")

        # almacenar el audio
        audio = reco.listen(origen)

        # manejo de errores
        try:
            # buscar en google
            pedido = reco.recognize_google(audio, language="es-ar")

            # test de ingreso
            print('Dijiste: ' + pedido)

            # retorno de pedido
            return pedido

        # en caso de que no se comprenda el audio
        except sr.UnknownValueError:

            # test de que no comprendio el audio
            print("Ups, no entendi")

            # return error
            return "Sigo sin entrender"

        except sr.RequestError:
            # test de que no comprendio el audio
            print("Ups, no hay servicio")

            # return error
            return "Sigo sin entrender"


        # error inesperado
        except:
            # test de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # return error
            return "Sigo esperando"

# opciones de vos / idiomas (eng / spa)
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

# funcion para escuchar a el asistente
def hablar(mensaje):
    # encender el motor pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id2)

    # pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():
    dia=datetime.date.today()
    dia_semana= dia.weekday()
    calendario ={ 0:'Lunes',
                  1:'Martes',
                  2:'Miércoles',
                  3:'Jueves',
                  4:'Viernes',
                  5:'Sábado',
                  6:'Domingo',
    }
    return calendario[dia_semana]

# informar hora
def pedir_hora():
    hora=datetime.datetime.now()
    hora_procesada=f'En este momento son las {hora.hour} horas con {hora.minute} minutos, {hora.second} segundos'

    return hora_procesada


#saludo inicial

def saludo_inicial():
    hora=datetime.datetime.now()

    if hora.hour < 6 or hora.hour> 20:
        hablar('Hola, buenas noches, soy Sabina, tu asistente personal, en que puedo ayudarte?')
    elif 20>hora.hour>=13:
        hablar('Hola,buenas tardes, soy Sabina, tu asistente personal, en que puedo ayudarte?')
    elif 13>hora.hour>=6:
        hablar('Hola, buenos días, soy Sabina, tu asistente personal, en que puedo ayudarte?')



saludo_inicial()

hablar(pedir_dia())
