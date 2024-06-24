from typing import Tuple, Literal
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
        
    #Definindo a imagem de fundo da interface de dialogo
        self._backgroud = ctk.CTkLabel(
            master=self, image=bg_image, text=""
        ).place(x=0,y=0)

    #Criando frame rolável para os diálogos
        self._frame_conversas = ctk.CTkScrollableFrame(
            master=self._backgroud, fg_color="#fafafa",
            width=350, height=370, corner_radius=20, bg_color="#2D4557"
        )
        self._frame_conversas.pack(pady=(35,0))

    #Criando frame para ações do usuário
        self._frame_acoes = ctk.CTkFrame(
            master=self._backgroud, fg_color="#fafafa",
            width=385, height=50, corner_radius=20, bg_color="#2D4557"
        )
        self._frame_acoes.pack(pady=(5,35))
        self._frame_acoes.grid_columnconfigure((0,10), weight=1) # configurando grade do frame

    # Definindo a caixa de entrada e configurando
        self.entrada = ctk.CTkEntry(
            master=self._frame_acoes, border_width=0, 
            placeholder_text="Comando", placeholder_text_color="#4d4d4d",
            width=286, fg_color="#fafafa", text_color="#212121",
            font=ctk.CTkFont("Calibri", 16, "normal")
        )
        self.entrada.grid(row=0, column=0,padx=10, pady=10, sticky='nswe', columnspa=8)
        # self.entrada.bind("<Return>", self._enter)
    
    # Definindo botão de enviar e configurando o estilo
        self.botao_enviar = ctk.CTkButton(
            self._frame_acoes, text="➤", font=ctk.CTkFont(size=20, weight="bold"),
            fg_color= "#28826c", text_color="#fafafa", width=30, hover_color= "#1d5c4d"
        )
        self.botao_enviar.grid(row=0, column=8, padx=0, pady=10, sticky="nse")
        
    # Definindo botão de ouvir e configurando o estilo
        self.botao_ouvir = ctk.CTkButton(
            self._frame_acoes, text="🎙", font=ctk.CTkFont(size=20, weight="bold"),
            fg_color= "#2D4557", text_color="#fafafa", width=30, hover_color= "#1f303d"
        )
        self.botao_ouvir.grid(row=0, column=9, padx=(2,10), pady=10, sticky="nse")

    def _config(self):
        self.geometry("450x550")
        self.iconbitmap("icon.ico")
        self.resizable(False, False)
    
    def make_dialogo(self, tipo: Literal["user", "machine"], texto:str):
        dialogo = ctk.CTkLabel(
            master=self._frame_conversas, font=ctk.CTkFont("Calibri", 16, "normal"),
            width=200, bg_color="#fafafa",
            corner_radius=20, text_color="#fff"
        )
        if tipo == "user":
            dialogo.configure(fg_color="#28826c", text=texto)
            dialogo.pack(padx=10, pady=5, anchor="e")
        else:
            dialogo.configure(fg_color="#2D4557", text=texto)
            dialogo.pack(padx=10, pady=5, anchor="w")


janelinha = Janela("Título")
janelinha.make_dialogo("user", "Olá assitente virtual, poderia \nme ajudar com uma coisa?")
janelinha.make_dialogo("machine", "Claro que sim. Como posso lhe ajudar?")
janelinha.mainloop()