import json
import time
import datetime
from machine import Machine, audio_verify

FILE_PATH = "lista_tarefas.json"

class TaskList:
    def __init__(self, path: str) -> None:
        self.path = path
        self.lista = self._read()
    
    def _read(self):
        data = []
        try:
            with open(self.path, "r", encoding="utf-8") as arquivo:
                data = json.load(arquivo)
        except FileNotFoundError:
            self.save([])
        return data
    
    def save(self, lista=None) -> None:
        if lista is None:
            lista = self.lista
        with open(self.path, "w", encoding="utf-8") as arquivo:
            data = json.dump(lista, arquivo, indent=1, ensure_ascii=False)
        return data
    
    def reset(self) -> None:
        self.save([])
    
    def add(self, tarefa, horario):
        self.lista.append({tarefa: horario})

    def listar(self):
        return self.lista

def app_lista_tarefas(comand: str, task_list: TaskList, machine: Machine) -> None:
    if "adicionar" in comand:
        while True:
            machine.speak("Qual a tarefa?")
            tarefa = machine.hear()
            if audio_verify(tarefa, machine): continue
            break
        
        while True: 
            machine.speak("E para que horas?")
            horario = machine.hear().lower()
            if audio_verify(horario, machine): continue
            
            horario.replace("horas e", ':')
            horario.replace('minutos', '')
            horario.replace('e', ':')
            print(horario)
                    
            task_list.add(tarefa, horario)
            machine.speak("Tarefa adicionada!")
            break
        
    if "salva" in comand or "salve" in comand:
        task_list.save()
        machine.speak("Salvando as alterações!")
    
    if "listar" in comand or "exibir" in comand:
        machine.speak("Suas tarefas são:")
        tarefas = task_list.listar()
        
        for item in tarefas:
            for tarefa, horario in item.items():
                horario = datetime.datetime.strptime(horario, "%H:%M")
                horario = datetime.datetime.strftime(horario, " as %H e %M")
                machine.speak(tarefa+horario)
                time.sleep(0.3)
        
    if "excluir todas" in comand or "exclua todas" in comand:
        task_list.reset()
        machine.speak("Entendi, sua lista de tarefas foi limpa!")