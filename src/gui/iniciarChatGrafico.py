import tkinter as tk
from .usuarioInput import CaixaMensagem
from .opcoes import Dialogos
from .chatController import ChatController

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = ChatController()
        self.title("NutriChat")
        self.geometry("800x600")

        # Área de mensagens
        self.area_mensagens = tk.Frame(self)
        self.area_mensagens.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Caixa de entrada do usuário
        self.caixa = CaixaMensagem(self, enviar_callback=self.receber_mensagem)
        self.caixa.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Caixa para aprendizado (inicialmente oculta)

        self.chat_aprendizado()

        # Última pergunta não respondida
        if self.esconder_nova_resposta ==True:
            self.chat_aprendizado()
        else:
            self.ultima_pergunta = None

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

    def receber_mensagem(self, mensagem):
        """Exibe a mensagem do usuário e a resposta do bot"""
        # Mensagem do usuário
        tk.Label(
            self.area_mensagens,
            text=f"Você: {mensagem}",
            bg="#e0e0e0",
            anchor="w",
            padx=5
        ).pack(fill=tk.X, pady=2)

        # Resposta do bot
        resposta_bot = self.controller.responder(mensagem)

        tk.Label(
            self.area_mensagens,
            text=f"Bot: {resposta_bot}",
            bg="#d0ffd0",
            anchor="w",
            justify=tk.LEFT,
            padx=5
        ).pack(fill=tk.X, pady=2)

        if self.controller.precisa_aprender() == False:
            self.ul

        # Se o bot não souber, habilita aprendizado
        elif self.controller.precisa_aprender():
            self.ultima_pergunta = mensagem
            self.frame_aprendizado.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    def salvar_resposta_aprendida(self):
        """Salva resposta que o usuário ensinou"""
        nova_resposta = self.entry_aprender.get().strip()
        if self.ultima_pergunta and nova_resposta:
            self.controller.aprender(self.ultima_pergunta, nova_resposta)

            # Exibir confirmação no chat
            tk.Label(
                self.area_mensagens,
                text=f"Bot: Obrigado! Aprendi a responder '{self.ultima_pergunta}' 😉",
                bg="#d0ffd0",
                anchor="w",
                justify=tk.LEFT,
                padx=5
            ).pack(fill=tk.X, pady=2)

            # Limpa campo e esconde novamente
            self.entry_aprender.delete(0, tk.END)
            self.frame_aprendizado.pack_forget()
            self.ultima_pergunta = None
        else:
            Dialogos.aviso("Aviso", "Digite uma resposta antes de salvar!")


if __name__ == "__main__":
    app = Root()
    app.mainloop()
