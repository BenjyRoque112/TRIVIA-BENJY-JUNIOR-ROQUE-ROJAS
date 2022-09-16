import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


iniciar_trivia = True
intentos = 0

print (MAGENTA+"¡Hola! Bienvenido a una pequeña trivia")
time.sleep(2)
print ("\nNos divertiremos y pondremos a prueba tus conocimientos en deporte")
time.sleep(3)

print("\nOJO!..."+RESET)
print(GREEN+"\nRespuesta correcta: De 0 y 3 al azar"+RESET)
print(RED+"Respuesta incorrecta: De -3 y 0 al azar"+RESET)
time.sleep(2)

print (MAGENTA+"\nMUCHA SUERTE...!!!\n"+RESET)
time.sleep(1)

nombre = input(CYAN+"Para comenzar, ingresa tu nombre: "+RESET)

while iniciar_trivia == True:
  intentos += 1
  puntaje = random.randint(1, 6)

  print(CYAN+"\nHola",nombre,".")
  time.sleep(1)
  print("\nEste es tu intento numero: ", intentos)
  time.sleep(1)
  input("\nPresiona 'Enter' para para tirar el dado")
  time.sleep(1)
  
  print ("\nGenial! Obtuviste", puntaje, "puntos"+RESET)
  time.sleep(1)
  print(YELLOW+"\nAhora lee y responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta. Comenzaremos en: \n"+RESET)
  time.sleep(5)
  
  for numero_carga in range(5, 0, -1):
    print(numero_carga,"\n")
    time.sleep(1)
  
  # Pregunta 1
  print (GREEN+"Pregunta 1: ¿Qué boxeador fue conocido como “El más grande” y “El campeón del pueblo”?\n")
  time.sleep(3)
  print ("a) Mike Tyson")
  time.sleep(1)
  print ("b) Muhammad Ali")
  time.sleep(1)
  print ("c) Floyd Mayweather")
  time.sleep(1)
  print ("d) Oscar de la Hoya"+RESET)
  time.sleep(1)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  time.sleep(2)
  
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_1 == "a":
    print(RED+"\nIncorrecto!..."+RESET)
    puntaje -= random.randint(0, 3)
    time.sleep(1)
    print("La respuesta correcta es: “b) Muhammad Ali”")
  elif respuesta_1 == "c":
    print(RED+"\nIncorrecto!..."+RESET)
    puntaje -= random.randint(0, 3)
    time.sleep(1)
    print("La respuesta correcta es: “b) Muhammad Ali”")
  elif respuesta_1 == "d":
    print(RED+"\nIncorrecto!..."+RESET)
    puntaje -= random.randint(0, 3)
    time.sleep(1)
    print("La respuesta correcta es: “b) Muhammad Ali”")
  else:
    print(GREEN+"\nCorrecto!..."+RESET)
    puntaje += random.randint(0, 3)
  print("Muhammad Ali ganó la medalla de oro en los Juegos Olímpicos de 1960 y se convirtió en el primer boxeador en ganar el título de peso pesado tres veces.")
  time.sleep(2)
  print("\nTienes: ", puntaje, "puntos.")
  time.sleep(3)
  
  
  # Pregunta 2
  print(GREEN+"\nPregunta 2: ¿En qué país se celebraron los primeros Juegos Olímpicos?\n")
  time.sleep(3)
  print("a) Italia")
  time.sleep(1)
  print("b) Japón")
  time.sleep(1)
  print("c) Grecia")
  time.sleep(1)
  print("d) Francia"+RESET)
  time.sleep(1)
  
  # Almacenamos la rspuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ")
  time.sleep(2)
  
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_2 == "a":
    puntaje -= random.randint(0, 3)
    print(RED+"\nIncorrecto!..."+RESET)
    time.sleep(1)
    print("La respuesta correcta es: “c) Grecia”")
  elif respuesta_2 == "b":
    puntaje -= random.randint(0, 3)
    print(RED+"\nIncorrecto!..."+RESET)
    time.sleep(1)
    print("La respuesta correcta es: “c) Grecia”")
  elif respuesta_2 == "d":
    puntaje -= random.randint(0, 3)
    print(RED+"\nIncorrecto!..."+RESET)
    time.sleep(1)
    print("La respuesta correcta es: “c) Grecia”")
  else:
    puntaje += random.randint(0, 3)
    print(GREEN+"\nCorrecto!..."+RESET)
  print("Los Juegos Olímpicos de Verano de 1896 celebrados en Atenas, Grecia. Fueron los primeros Juegos Olímpicos internacionales celebrados en la historia moderna.")
  time.sleep(2)
  print("\nTienes: ", puntaje, "puntos.")
  time.sleep(3)
  
  
  # Pregunta 3
  print(GREEN+"\nPregunta 3: ¿Cada cuántos años se llevan a cabo los Juegos Olímpicos?\n")
  time.sleep(4)
  print("a) Seis años")
  time.sleep(1)
  print("b) Siete años")
  time.sleep(1)
  print("c) Cinco años")
  time.sleep(1)
  print("d) Cuatro años"+RESET)
  time.sleep(1)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ")
  time.sleep(2)
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_3 == "a":
    puntaje -= random.randint(0, 3)
    print(RED+"\nIncorrecto!..."+RESET)
    time.sleep(1)
    print("La respuesta correcta es: “d) Cuatro años”")
  elif respuesta_3 == "b":
    puntaje -= random.randint(0, 3)
    print(RED+"\nIncorrecto!..."+RESET)
    time.sleep(1)
    print("La respuesta correcta es: “d) Cuatro años”")
  elif respuesta_3 == "c":
    puntaje -= random.randint(0, 3)
    print(RED+"\nIncorrecto!..."+RESET)
    time.sleep(1)
    print("La respuesta correcta es: “d) Cuatro años”")
  else:
    puntaje += random.randint(0, 3)
    print(GREEN+"\nCorrecto!..."+RESET)
    time.sleep(1)
  print("Los Juegos Olímpicos se celebran cada cuatro años como muestra de respeto a los antiguos Juegos Olímpicos, que se celebraban cada cuatro años en Olimpia.")
  time.sleep(2)
  print("\nEn las tres preguntas llegaste a sumar: ", puntaje, "puntos")

  ruleta_1 = 0
  ruleta_2 = 0
  ruleta_3 = 0
  
  if puntaje>0:    
    print(YELLOW+"\nFELICIDADES!!! Obtuviste un puntaje positivo y ganaste 3 giros en la RULETA, el puntaje total de los giros en la ruleta se sumaran a tus puntos obtenidos en la TRIVIA")
    input("\nPresiona 'Enter' para el primer giro de la RULETA")
    time.sleep(2)
    ruleta_1 += random.randint(0,10)
    print("Cayo en el numero: ",ruleta_1)
    time.sleep(2)
    input("\nPresiona 'Enter' para el segundo giro de la RULETA")
    time.sleep(2)
    ruleta_2 += random.randint(0,10)
    print("Cayo en el numero: ",ruleta_2)
    time.sleep(2)
    input("\nPresiona 'Enter' para el tercer giro de la RULETA")
    time.sleep(2)
    ruleta_3 += random.randint(0,10)
    print("Cayo en el numero: ",ruleta_3)
    time.sleep(2)
    print("\nGanaste: ", ruleta_1+ruleta_2+ruleta_3," puntos en la RULETA"+RESET)
    time.sleep(2)
    print(GREEN+"\nTU PUNTAJE SUMA EN TOTAL: ", ruleta_1+ruleta_2+ruleta_3+puntaje, "puntos"+RESET)
 
  else:
      print(YELLOW+"\nObtuviste un puntaje negativo, mas suerte para la proxima"+RESET)

  print(RED+"\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()
  if repetir_trivia != "si": 
   print("\nEspero",nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False 
