import speech_recognition as sr
from gtts import gTTS
import pygame
import os

pygame.mixer.init()
DEFAULT_MIC = sr.Microphone()

class Machine():
    """
    Classe principal com métodos de ouvir (hear) e falar (speak).
    
    obs: com um adicional para se apresentar (myself)
    """
    def __init__(self, name: str) -> None:
        self.name = name
        """ nome da máquina """
        self.recognizer = sr.Recognizer()
        """ reconhecedor da máquina"""
    
    def _text_converter(self, audio: sr.AudioData) -> str:
        """
        Com o dado de audio reconhecido pela voz do usuário, converte 
        em texto e retorna o mesmo. Caso haja algum erro na conversão
        ou o usurário não falar nada, retorna um erro em str
        """
        try:
            text = self.recognizer.recognize_google(audio, language="pt-BR")
            return text
        except sr.UnknownValueError:
            return "AudioError"
        except sr.Recognizer:
            return "RequestError"
    
    def hear(self, mic=DEFAULT_MIC) -> str:
        """
        Com o microfone padrão utilizado pelo sistema,
        reconhece o que o usuário falar e retorna em str
        """
        with mic as source:
            self.recognizer.adjust_for_ambient_noise(source=source)
            audio = self.recognizer.listen(source=source)
            comand = self._text_converter(audio=audio)
            return comand
    
    def speak(self, text: str) -> None:
        """
        Recebe um texto e cria um arquivo .mp3 com a classe gTTS;
        Utiliza o módulo pygame para reproduzir o arquimo mp3 e
        sem seguida o deleta do sistema
        """
        tts = gTTS(text=text, lang="pt-BR")
        file_path = "voice"+self.name+".mp3"
        tts.save(file_path)
        
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.unload()
        
        os.remove(file_path)        
        
    def myself(self) -> None:
        """ Se apresenta com o nome """
        self.speak(f"Olá, eu me chamo {self.name}. Faço parte do projeto Val,"\
            "e sou uma assistente virtual para laboratórios."\
                "Se precisar de ajuda estarei aqui"
        )


def audio_verify(speech: str, machine: Machine) -> bool:
    if speech == "audioerror":
        machine.speak("O senhor não disse nada...")
        return True
    if speech == "requesterror":
        machine.speak("Erro ao obter informações do reconhecedor")
    return False