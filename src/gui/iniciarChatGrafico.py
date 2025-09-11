import tkinter as tk
from opcoes import Dialogos
from usuarioInput import CaixaMensagem
from botOutput import Bot

#oque cada importe faz aqui

#o tkinter, serve para criar a interface grafica
#o opcoes, serve para importar a classe Dialogos que cria as caixas de dialogo
#o usuarioInput, serve para importar a classe CaixaMensagem que cria a caixa de mensagem do usuario
#o BotO

#Classe de testes por hora;

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bot = Bot()
        self.title("NutriChat")
        self.geometry("800x600")
        
        # Área onde as mensagens enviadas vão ser exibidas
        self.area_mensagens = tk.Frame(self)
        self.area_mensagens.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # caixa aonde o usuario vai digitar a mensagem
        self.caixa = CaixaMensagem(self, enviar_callback=self.receber_mensagem)
        self.caixa.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    def receber_mensagem(self, mensagem):
        """
        Função chamada quando usuário envia uma mensagem, basicamente o histórico de mensagens
        """
        label = tk.Label(
                        self.area_mensagens,
                        text=mensagem,
                        bg="#e0e0e0",
                        anchor="w",
                        padx=5)
        label.pack(fill=tk.X, pady=2)

        # Gerar e exibir resposta do bot
        resposta_bot = self.gerar_resposta_do_bot(mensagem)
        label_bot = tk.Label(
                            self.area_mensagens,
                            text=f"Bot: {resposta_bot}",
                            bg="#d0ffd0",
                            anchor="e",
                            justify=tk.RIGHT,
                            padx=5
                            )
        label_bot.pack(fill=tk.X, pady=2)

    def gerar_resposta_do_bot(self, mensagem):

        return Bot().gerar_resposta(mensagem)
    
    def sair(self):
        if Dialogos.confirmar("Sair", "Deseja realmente sair?"):
            self.destroy()


if __name__ == "__main__":
    app = Root()
    app.mainloop()