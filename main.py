import machine
import tasks
import datetime

sara = machine.Machine("Sara")
sara.myself()
def audio_verify(speech: str) -> bool:
    if speech == "audioerror":
        sara.speak("O senhor não disse nada...")
        return True
    return False

my_tasks = tasks.TaskList(tasks.FILE_PATH)
def app_lista_tarefas(comand: str):
    if "adicionar" in comand:
        sara.speak("Qual a tarefa?")
        tarefa = sara.hear()
        
        sara.speak("E para que horas?")
        horario = sara.hear().replace("horas e", ':')
        horario.replace('minutos', '')
        horario.replace('e', ':')
        print(horario)
                
        my_tasks.add(tarefa, horario)
        sara.speak("Tarefa adicionada!")
        
    if "salva" in comand or "salve" in comand:
        my_tasks.save()
        sara.speak("Salvando as alterações!")

while True:
    input("Press Enter to speak")
    speech = sara.hear().lower()   
    
    if audio_verify(speech): continue
    
    if "abir lista de tarefas":
        sara.speak("Certo!, Estou na sua lista de tarefas. O que deseja fazer?")
        comand = sara.hear().lower()
        if audio_verify(comand):  
            sara.speak('Não entendi o comando')
            continue
        
        app_lista_tarefas(comand)
    else:
        sara.speak('Não entendi o comando')