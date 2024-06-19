import time
from machine import Machine, audio_verify
from tasks import TaskList, app_lista_tarefas, FILE_PATH
import datetime

sara = Machine("Sara")
# sara.myself()

my_tasks = TaskList(FILE_PATH)

while True:
    input("Press Enter to speak")
    speech = sara.hear().lower()   
    
    if audio_verify(speech=speech, machine=sara): continue
    
    print(speech)
    if "abrir lista de tarefas" in speech:
        sara.speak("Certo! O que deseja fazer?")
        comand = sara.hear().lower()
        if audio_verify(speech=comand, machine=sara): 
            sara.speak("fechando lista de tarefas")
            continue
        
        while True:
            app_lista_tarefas(comand=comand, task_list=my_tasks, machine=sara)
            sara.speak("mais alguma coisa?")
            resposta = sara.hear().lower()
            if "não" in resposta:
                sara.speak("Certo! Fechando lista de tarefas")
                break
            comand = resposta
    else:
        sara.speak('Não entendi o comando')