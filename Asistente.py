import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime



#transformar audio a texto

def transformar_audio_en_texto():

    #recognizer en variable
    reco=sr.Recognizer()

    #configuracion de microfono
    with sr.Microphone() as origen:
        #tiempo de espera
        reco.pause_threshold=0.8

        # info de que comenzo la grabacion
        print("ya puedes hablar")

        # almacenar el audio
        audio=reco.listen(origen)

        # manejo de errores
        try:
            #buscar en google
            pedido= reco.recognize_google(audio, language="es-ar")

            # test de ingreso
            print('Dijiste: '+pedido)

            #retorno de pedido
            return pedido

        #en caso de que no se comprenda el audio
        except sr.UnknownValueError:

            #test de que no comprendio el audio
            print("Ups, no entendi")

            # return error
            return "Sigo sin entrender"

        except sr.RequestError:
            # test de que no comprendio el audio
            print("Ups, no hay servicio")

            # return error
            return "Sigo sin entrender"


        #error inesperado
        except:
            # test de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # return error
            return "Sigo esperando"




# funcion para escuchar a el asistente
def hablar(mensaje):

    #encender el motor pyttsx3
    engine=pyttsx3.init()

    #pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()





engine=pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)
