import speech_recognition as sr
from gtts import gTTS
import pygame
import os

pygame.mixer.init()
DEFAULT_MIC = sr.Microphone()

class Machine():
    def __init__(self, name: str) -> None:
        self.name = name
        self.recognizer = sr.Recognizer()
    
    def _text_converter(self, audio: sr.AudioData) -> str:
        try:
            text = self.recognizer.recognize_google(audio, language="pt-BR")
            print(type(text))
            return text
        except sr.UnknownValueError:
            return "AudioError"
        except sr.Recognizer:
            return "RequestError"
    
    def hear(self, mic=DEFAULT_MIC) -> str:
        with mic as source:
            self.recognizer.adjust_for_ambient_noise(source=source)
            audio = self.recognizer.listen(source=source)
            comand = self._text_converter(audio=audio)
            return comand
    
    def speak(self, text: str) -> None:
        tts = gTTS(text=text, lang="pt-BR")
        file_path = "voice"+self.name+".mp3"
        tts.save(file_path)
        
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.unload()
        
        os.remove(file_path)        
        
    def yourself(self) -> None:
        """ Se apresenta com o nome """
        self.speak(f"Olá, eu me chamo {self.name}. Faço parte do projeto Val,"\
            "e sou uma assistente virtual para laboratórios."\
                "Se precisar de ajuda estarei aqui"
        )

a = Machine('aaa')
sla = a.hear()