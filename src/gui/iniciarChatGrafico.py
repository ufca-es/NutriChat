import tkinter as tk
from tkinter import messagebox
from .usuarioInput import CaixaMensagem
from .chatController import ChatController


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = ChatController()
        self.title("NutriChat")
        self.geometry("800x600")
        self.ultima_pergunta = None
         
        self.area_mensagens = tk.Frame(self)
        self.area_mensagens.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.caixa = CaixaMensagem(self, enviar_callback=self.receber_mensagem)
        self.caixa.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Caixa de aprendizado (inicialmente oculta)
        self.chat_aprendizado()

    def chat_aprendizado(self):
        self.frame_aprendizado = tk.Frame(self)
        self.label_aprender = tk.Label(self.frame_aprendizado, text="Me ensine uma resposta:")
        self.entry_aprender = tk.Entry(self.frame_aprendizado, width=40)
        self.btn_aprender = tk.Button(
            self.frame_aprendizado,
            width=15,
            text="Salvar resposta",
            command=self.salvar_resposta_aprendida
        )

        self.label_aprender.pack(side=tk.LEFT, padx=5)
        self.entry_aprender.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.btn_aprender.pack(side=tk.LEFT, padx=5)

        # oculta no inicio
        self.frame_aprendizado.pack_forget()

    def receber_mensagem(self, mensagem: str):
        """Exibe a mensagem do usuÃ¡rio e a resposta do bot"""
        tk.Label(
            self.area_mensagens,
            text=f"VocÃª: {mensagem}",
            bg="#e0e0e0",
            anchor="w",
            padx=5
        ).pack(fill=tk.X, pady=2)

        resposta_bot = self.controller.responder(mensagem)
        tk.Label(
            self.area_mensagens,
            text=f"Bot: {resposta_bot}",
            bg="#d0ffd0",
            anchor="w",
            justify=tk.LEFT,
            padx=5
        ).pack(fill=tk.X, pady=2)

        # Se o bot nnão souber responder, controller.pergunta_desconhecida fica com a pergunta
        if self.controller.pergunta_desconhecida:
            # guarda para quando o usuario ensinar a resposta
            self.ultima_pergunta = self.controller.pergunta_desconhecida
            # mostra o widget de aprendizado
            self.frame_aprendizado.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        else:
            # caso o bot saiba a pergunta, o widget fica oculto
            self.ocultar_aprendizado()

        # se o widget estava visivel mas o usuario digitou outra pergunta que já
        # existe, escondemos o widget
        if self.frame_aprendizado.winfo_ismapped():
            # verifica se a pergunta atual existe nos bancos
            if self.controller.pergunta_existe(mensagem):
                self.ocultar_aprendizado()

    def salvar_resposta_aprendida(self):
        nova_resposta = self.entry_aprender.get().strip()
        if self.ultima_pergunta and nova_resposta:
            self.controller.aprender(self.ultima_pergunta, nova_resposta)

            tk.Label(
                self.area_mensagens,
                text=f"Bot: Obrigado! Aprendi a responder '{self.ultima_pergunta}'",
                bg="#d0ffd0",
                anchor="w",
                justify=tk.LEFT,
                padx=5
            ).pack(fill=tk.X, pady=2)

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
