import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import yfinance as yf
import pyjokes
import webbrowser
import datetime


# transformar audio a texto

def transformar_audio_en_texto():
    # recognizer en variable
    reco = sr.Recognizer()

    # configuracion de microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        reco.pause_threshold = 0.5

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
    engine.setProperty('voice', id2)

    # pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():
    dia = datetime.date.today()
    dia_semana = dia.weekday()
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo',
                  }
    return hablar(calendario[dia_semana])


# informar hora
def pedir_hora():
    hora = datetime.datetime.now()
    hora_procesada = f'En este momento son las {hora.hour} horas con {hora.minute} minutos, {hora.second} segundos'

    return hablar(hora_procesada)


# saludo inicial

def saludo_inicial():
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        hablar('Hola, buenas noches, soy Sabina, tu asistente personal, en que puedo ayudarte?')
    elif 20 > hora.hour >= 13:
        hablar('Hola,buenas tardes, soy Sabina, tu asistente personal, en que puedo ayudarte?')
    elif 13 > hora.hour >= 6:
        hablar('Hola, buenos días, soy Sabina, tu asistente personal, en que puedo ayudarte?')


def centro_de_pedidos():
    saludo_inicial()

    comenzar = True

    while comenzar:

        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Entendido, abriendo youtube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Claro, estoy en ello')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Claro, comenzare a buscarlo')
            pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Pude encontrar el siguiente resultado de wikipedia')
            hablar(resultado)
            continue

        elif 'hasta luego sabina' in pedido:
            hablar('Me voy a descansar, avisame si me necesitas')
            comenzar = False

        elif 'busca en internet' in pedido:
            hablar('Yo me ocupo!')
            pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('he encontrado lo siguiente...')
            continue
        elif 'reproducir' in pedido:
            hablar('buena idea,ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            acciones = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[acciones]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {acciones}es {precio_actual}')
                continue
            except:
                hablar('Perdon pero no la he encontrado')
                continue


centro_de_pedidos()
