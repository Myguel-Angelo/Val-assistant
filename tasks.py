import json
from datetime import datetime

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
            self.save({})
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
