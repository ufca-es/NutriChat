import tkinter as tk
from opcoes import Dialogos
from usuarioInput import CaixaMensagem


#Classe de testes por hora;

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NutriChat")
        self.geometry("800x600")

        tk.Button(self, text="Mostrar Informação",
                  command=lambda: Dialogos.info("Info", "Isso é uma mensagem de informação")).pack(pady=5)

        tk.Button(self, text="Mostrar Aviso",
                  command=lambda: Dialogos.aviso("Aviso", "Isso é um aviso")).pack(pady=5)

        tk.Button(self, text="Mostrar Erro",
                  command=lambda: Dialogos.erro("Erro", "Isso é um erro")).pack(pady=5)

        tk.Button(self, text="Confirmar Saída",
                  command=self.sair).pack(pady=5)
        
        # Área onde as mensagens enviadas vão ser exibidas
        self.area_mensagens = tk.Frame(self)
        self.area_mensagens.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # caixa aonde o usuario vai digitar a mensagem
        self.caixa = CaixaMensagem(self, enviar_callback=self.receber_mensagem)
        self.caixa.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    def receber_mensagem(self, mensagem):
        """Função chamada quando usuário envia uma mensagem, basicamente o histórico de mensagens"""
        label = tk.Label(self.area_mensagens, text=mensagem, bg="#e0e0e0", anchor="w", padx=5)
        label.pack(fill=tk.X, pady=2)

        # Gerar e exibir resposta do bot
        resposta_bot = self.gerar_resposta_do_bot(mensagem)
        label_bot = tk.Label(
                            self.area_mensagens,
                            text=f"Bot: {resposta_bot}",
                            bg="#d0ffd0",
                            anchor="e", 
                            padx=5
                            )
        label_bot.pack(fill=tk.X, pady=2)
    
    def gerar_resposta_do_bot(self, mensagem_usuario):
        """
        Função simples para gerar resposta do bot \n.
        :param mensagem_usuario: Mensagem enviada pelo usuário.
        :return: Resposta do bot.
        """

        # Exemplo: resposta automática
        return f"Você disse: '{mensagem_usuario}'. Esta é uma resposta do NutriChat."

    def sair(self):
        if Dialogos.confirmar("Sair", "Deseja realmente sair?"):
            self.destroy()


if __name__ == "__main__":
    app = Root()
    app.mainloop()