from typing import Tuple
from PIL import Image
import customtkinter as ctk

bg_image = ctk.CTkImage(
    light_image=Image.open("bg_image.png"),
    dark_image=Image.open("bg_image.png"),
    size=(450,550)
)

class Janela(ctk.CTk):
    def __init__(self, window_title, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title(window_title)
        self._config()
        
        self._backgroud = ctk.CTkLabel(
            master=self, image=bg_image, text=""
        ).place(x=0,y=0)

        self._frame_conversas = ctk.CTkScrollableFrame(
            master=self._backgroud, fg_color="#fafafa",
            width=350, height=370, corner_radius=20, bg_color="#2D4557"
        )
        self._frame_conversas.pack(pady=(35,0))

        self._frame_acoes = ctk.CTkFrame(
            master=self._backgroud, fg_color="#fafafa",
            width=385, height=50, corner_radius=20, bg_color="#2D4557"
        )
        self._frame_acoes.pack(pady=(5,35))
        self._frame_acoes.grid_columnconfigure((0,10), weight=1)
        
        self.entrada = ctk.CTkEntry(
            master=self._frame_acoes, border_width=0, 
            placeholder_text="Comando", placeholder_text_color="#4d4d4d",
            width=350, fg_color="#fafafa", text_color="#212121"
        )
        self.entrada.grid(row=0, column=0,padx=10, pady=10, sticky='nswe', columnspa=8)
        # self.entrada.bind("<Return>", self._enter)
    
    def _config(self):
        self.geometry("450x550")
        self.iconbitmap("icon.ico")
        self.resizable(False, False)

janelinha = Janela("Título")

janelinha.mainloop()