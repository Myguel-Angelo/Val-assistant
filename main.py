import time
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

def app_lista_tarefas(comand: str) -> None:
    if "adicionar" in comand:
        while True:
            sara.speak("Qual a tarefa?")
            tarefa = sara.hear()
            if audio_verify(tarefa): continue
            break
        
        while True: 
            sara.speak("E para que horas?")
            horario = sara.hear().lower()
            if audio_verify(horario): continue
            
            horario.replace("horas e", ':')
            horario.replace('minutos', '')
            horario.replace('e', ':')
            print(horario)
                    
            my_tasks.add(tarefa, horario)
            sara.speak("Tarefa adicionada!")
            break
        
    if "salva" in comand or "salve" in comand:
        my_tasks.save()
        sara.speak("Salvando as alterações!")
    
    if "listar" in comand or "exibir" in comand:
        sara.speak("Suas tarefas são:")
        tarefas = my_tasks.listar()
        
        for item in tarefas:
            for tarefa, horario in item.items():
                horario = datetime.datetime.strptime(horario, "%H:%M")
                horario = datetime.datetime.strftime(horario, " as %H e %M")
                sara.speak(tarefa+horario)
                time.sleep(0.5)
        
    if "excluir todas" in comand or "exclua todas" in comand:
        my_tasks.reset()
        sara.speak("Entendi, sua lista de tarefas foi limpa!")
while True:
    input("Press Enter to speak")
    speech = sara.hear().lower()   
    
    if audio_verify(speech): continue
    
    print(speech)
    if "abrir lista de tarefas" in speech:
        sara.speak("Certo! O que deseja fazer?")
        comand = sara.hear().lower()
        if audio_verify(comand): 
            sara.speak("fechando lista de tarefas")
            continue
        
        while True:
            app_lista_tarefas(comand)
            sara.speak("mais alguma coisa?")
            resposta = sara.hear().lower()
            if "não" in resposta:
                sara.speak("Certo! Fechando lista de tarefas")
                break
            comand = resposta
    else:
        sara.speak('Não entendi o comando')