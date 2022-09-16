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
listaPuntaje=[]
listaPuntajeIntento=[]

print(YELLOW+"Bienvenid@ a mi trivia sobre Cultura General\n")
print("Pondremos a prueba tus conocimientos. Estas Listo?\n"+RESET)

nombre = input("Ingresa tu nombre: ")

print(
    GREEN+"\n Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET
)


while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = random.randint(0, 10)
  print("Tienes", puntaje, "puntos\n")

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  
  for numero_carga in range(5,0,-1):
    print(numero_carga)
    time.sleep(1)

  # Pregunta 1
  print(MAGENTA+"1) ¿Que evento histórico sucedio el 1929?"+RESET)
  print(CYAN+"a) 1 Guerra Mundial")
  print("b) Gran Depresión")  #Respuesta
  print("c) 2 Guerra Mundial")
  print("d) Guerra Civil Española"+RESET)
  respuesta_1 = input("\nTu respuesta: ")
  while respuesta_1 not in ("a", "b", "c", "d"):
      respuesta_1 = input(
          "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "b":
      print("\n ✔ Correcto!", nombre,"!\n")
      puntaje += random.randint(0, 20)
      print("\nTienes", puntaje, "puntos\n")
  else:
      print("\n ❌ Incorrecto!\n")
      puntaje -= random.randint(0, 10)
      print("\nTienes", puntaje, "puntos\n")
  time.sleep(2)
  # Pregunta 2
  print(MAGENTA+"2) ¿Que antigua civilización construyó la ciudad de UR?"+RESET)
  print(CYAN+"a) Sumeria")  #Respuesta
  print("b) Hitita")
  print("c) Egipcia")
  print("d) Romana"+RESET)

  respuesta_2 = input("\nTu respuesta: ")
  
  while respuesta_2 not in ("a", "b", "c", "d","x"):
      respuesta_2 = input(
          "Debes responder a, b, c. x o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_2 == "b":
    print("\n ❌ Incorrecto!", nombre, "Hitita edificaron poderosos reinos\n")
    puntaje -= random.randint(0, 10)
    print("\nTienes", puntaje, "puntos\n")
  elif respuesta_2 == "c":
    print("\n ❌ Incorrecto!", nombre, "Los egipcios formaron dos grandes reinos: uno en el Alto Egipto y otro en el Bajo Egipto\n")
    puntaje -= random.randint(0, 10)
    print("\nTienes", puntaje, "puntos\n")
  elif respuesta_2 == "d":
    print("\n ❌ Incorrecto!", nombre,"\n")
    puntaje -= random.randint(0, 10)
    print("\nTienes", puntaje, "puntos\n")
  elif respuesta_2 == "x":
    print("\n Sabías que", nombre, "la ciudad de Ur fue uno de los primeros núcleos urbanos de Mesopotamia y, por ende, de la humanidad\n")
    puntaje += random.randint(0, 100)
    print("\nTienes", puntaje, "puntos\n")
  else:
    print("\n ✔ Correcto!", nombre,"!\n")
    puntaje += random.randint(0, 20)
    print("\nTienes", puntaje, "puntos\n")
  time.sleep(2)
  # Pregunta 3
  print(MAGENTA+"3) ¿Quién pintó el fresco 'La Creación de Adán'?"+RESET)
  print(CYAN+"a) Sandro Botticelli")
  print("b) Miguel Ángel")  #Respuesta
  print("c) Leonardo da Vinci")
  print("d) Filippo Brunelleschi"+RESET)

  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
      respuesta_3 = input(
          "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "b":
      print("\n ✔ Correcto!", nombre,"!\n")
      puntaje += random.randint(0, 20)
      print("\nTienes", puntaje, "puntos\n")
  else:
      print("\n ❌ Incorrecto!\n")
      puntaje -= random.randint(0, 10)
      print("\nTienes", puntaje, "puntos\n")
  
  print(nombre, "llevas", puntaje, "puntos")
  time.sleep(2)
  # Pregunta 4
  print (MAGENTA+"\n1) ¿En cuál de estas religiones existen muchos dioses?"+RESET)
  print (CYAN+"a) Judaismo")
  print ("b) Islam")
  print ("c) Cristianismo")
  print ("d) Hinduismo"+RESET)
  
  respuesta_4 = input("\nTu respuesta: ")
  
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_4 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
    print("\nTienes", puntaje, "puntos\n")
  elif respuesta_4 == "b":
    print ("...")
    puntaje = puntaje + 5
    print("\nTienes", puntaje, "puntos\n")
  elif respuesta_4 == "c":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
    print("\nTienes", puntaje, "puntos\n")
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 2
    print("\nTienes", puntaje, "puntos\n")
  
  time.sleep(2)
  print("Lluvia de Puntaje")
  for numero in range(2,random.randint(2, 8),1):
      nuevo=puntaje*numero
      print("Tu nuevo puntaje es: ",nuevo)
      time.sleep(1)
  print("\nTienes", nuevo, "puntos\n")
  listaPuntajeIntento.append(nuevo)
  
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
    print ("\nGracias", nombre, "por jugar mi trivia, alcanzaste", nuevo, "puntos 🪙")
    print("Los puntajes de tus intentos son: ")
    for element in listaPuntajeIntento:
      print(element)
    print("\nEspero", nombre,"que lo hayas pasado bien, hasta pronto!")
    iniciar_trivia = False 

