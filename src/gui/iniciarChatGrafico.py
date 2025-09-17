import tkinter as tk
from tkinter import messagebox
from .usuarioInput import CaixaMensagem
from .chatController import ChatController
from ..historico import Historico


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = ChatController()
        self.title("NutriChat")
        self.geometry("800x600")
        self.ultima_pergunta = None

        # Estilo ChatGPT: fundo escuro
        self.configure(background="#343541")

        # Área de mensagens (com scrollbar)
        self.container = tk.Frame(self, bg="#343541")
        self.container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(self.container, bg="#343541", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#343541")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Caixa de input do usuário
        self.caixa = CaixaMensagem(self, enviar_callback=self.receber_mensagem)
        self.caixa.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Caixa de aprendizado (inicialmente oculta)
        self.chat_aprendizado()

    def chat_aprendizado(self):
        self.frame_aprendizado = tk.Frame(self, bg="#444654")
        self.label_aprender = tk.Label(
            self.frame_aprendizado, text="Me ensine uma resposta:",
            bg="#444654", fg="white"
        )
        self.entry_aprender = tk.Entry(self.frame_aprendizado, width=40, bg="#565869", fg="white", insertbackground="white")
        self.btn_aprender = tk.Button(
            self.frame_aprendizado,
            width=15,
            text="Salvar resposta",
            bg="#10a37f", fg="white",
            activebackground="#0e8c6f",
            command=self.salvar_resposta_aprendida
        )

        self.label_aprender.pack(side=tk.LEFT, padx=5)
        self.entry_aprender.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.btn_aprender.pack(side=tk.LEFT, padx=5)

        # oculta no inicio
        self.frame_aprendizado.pack_forget()

    def adicionar_mensagem(self, texto, usuario=True):
        """Adiciona mensagem no estilo de balão"""
        cor_fundo = "#565869" if usuario else "#444654"
        cor_texto = "white"
        alinhamento = "e" if usuario else "w"
        padx = (100, 10) if usuario else (10, 100)

        frame_msg = tk.Frame(self.scrollable_frame, bg="#343541")
        label = tk.Label(
            frame_msg,
            text=texto,
            bg=cor_fundo,
            fg=cor_texto,
            wraplength=600,
            justify="left",
            anchor="w",
            padx=10,
            pady=8
        )
        label.pack(anchor=alinhamento, fill="x", padx=padx, pady=5, ipadx=5, ipady=5)

        frame_msg.pack(fill="x", anchor=alinhamento)

        # auto scroll pro fim
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1)

    def receber_mensagem(self, mensagem: str):
        """Exibe a mensagem do usuário e a resposta do bot"""
        self.adicionar_mensagem(f"Você: {mensagem}", usuario=True)

        resposta_bot = self.controller.responder(mensagem)
        self.adicionar_mensagem(f"Bot: {resposta_bot}", usuario=False)

        # Se o bot nnão souber responder, controller.pergunta_desconhecida fica com a pergunta
        if self.controller.pergunta_desconhecida:
            self.ultima_pergunta = self.controller.pergunta_desconhecida
            self.frame_aprendizado.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        else:
            self.ocultar_aprendizado()

        # se o widget estava visivel mas o usuario digitou outra pergunta que já
        # existe, escondemos o widget
        if self.frame_aprendizado.winfo_ismapped():
            if self.controller.pergunta_existe(mensagem):
                self.ocultar_aprendizado()

    def salvar_resposta_aprendida(self):
        nova_resposta = self.entry_aprender.get().strip()
        if self.ultima_pergunta and nova_resposta:
            self.controller.aprender(self.ultima_pergunta, nova_resposta)

            self.adicionar_mensagem(
                f"Bot: Obrigado! Aprendi a responder '{self.ultima_pergunta}'",
                usuario=False
            )

            self.ultima_pergunta = None
        else:
            messagebox.showwarning("Aviso", "Digite uma resposta antes de salvar!")

        self.entry_aprender.delete(0, tk.END)
        self.ocultar_aprendizado()

    def ocultar_aprendizado(self):
        self.ultima_pergunta = None
        self.frame_aprendizado.pack_forget()


if __name__ == "__main__":
    app = Root()
    app.mainloop()
