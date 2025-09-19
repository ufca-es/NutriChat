import tkinter as tk
from tkinter import messagebox
from .usuarioInput import CaixaMensagem
from .chatController import ChatController
from ..historico import Historico
from src.personalidades import Personalidade
from pathlib import Path


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NutriChat")
        self.geometry("800x600")
        
        self.ultima_pergunta = None
        self.historico = Historico()
        self.historico.iniciar()
        
        self.controller = ChatController()
        self.controller.historico = self.historico
        
        #botão para gerar um relatório
        self.btn_relatorio = tk.Button(
        self,
        text="Gerar Relatório",
        bg="#10a37f",
        fg="white",
        activebackground="#0e8c6f",
        command = self.gerar_relatorio)
        self.btn_relatorio.pack(side=tk.BOTTOM, pady=5)
        
        # Botão para trocar a personalidade
        self.btn_personalidade = tk.Button(
            self, text="Trocar Personalidade", command=self.trocar_personalidade
        )
        self.btn_personalidade.pack(pady=10)
        
        # Botão para mostrar as últimas interações
        self.btn_ultimos = tk.Button(
        self,
        text="Mostrar últimas interações",
        bg="#10a37f",
        fg="white",
        activebackground="#0e8c6f",
        command=self.mostrar_ultimos
        )
        self.btn_ultimos.pack(side=tk.BOTTOM, pady=5)


        # Estilo inspirado pelo chat gepeto: cores mais escuras
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

    def adicionar_mensagem(self, texto, usuario=True, cor_fundo_custom=None):
        """Adiciona mensagem no estilo de balão \n 
        :param: texto: texto da mensagem
        :param: usuario: True se for mensagem do usuário, False se for do bot
        """
        
        # serve para dar cores customizadas para
        # funcoes que usem adicionar_mensagem
        if cor_fundo_custom:
            cor_fundo = cor_fundo_custom
        else:
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
        """salva em srchistorico.txt"""
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
    
    def gerar_relatorio(self):
        """Gera um relatório da última sessão (sobrescreve relatorio.txt a cada vez)."""

        # Gera/atualiza estatísticas
        # (o próprio gerar_relatorio do Historico chama gerar_estatisticas internamente)
        caminho_relatorio = self.historico.gerar_relatorio()

        # opcional: notificar o usuário onde o relatório foi salvo
        try:
            messagebox.showinfo("Relatório", f"Relatório gerado em:\n{caminho_relatorio}")
        except Exception:
            # sem GUI possível: apenas para debug, improvavel que aconteça durante a execução
            pass

        return caminho_relatorio
    
    
    def trocar_personalidade(self):
        """
        Abre uma janelinha com botões de escolha de personalidade.
        """
        popup = tk.Toplevel(self)
        popup.title("Escolher Personalidade")
        popup.geometry("300x200")

        tk.Label(popup, text="Selecione a personalidade:", font=("Arial", 12)).pack(pady=10)

        personalidades = ["formal", "engraçado", "rude"]

        for p in personalidades:
            btn = tk.Button(
                popup, text=p.capitalize(), width=20,
                command=lambda escolha=p: self.definir_personalidade(escolha, popup)
            )
            btn.pack(pady=5)
    
    def definir_personalidade(self, escolha, popup):
        """
        Define a personalidade escolhida e fecha o popup.
        """
        resultado = Personalidade.selecionar_personalidade(escolha)
        if resultado:
            self.controller.set_personalidade(resultado)
            messagebox.showinfo("Personalidade", f"Personalidade alterada para: {resultado}")
        else:
            messagebox.showwarning("Personalidade", f"'{escolha}' não é válida.")
        popup.destroy()
    
    def gerar_relatorio(self):
        """Chama o método gerar_relatorio_gui do Historico para criar um relatório com timestamp"""
        caminho_relatorio = self.historico.gerar_relatorio_gui()
        return caminho_relatorio

    def mostrar_ultimos(self):
        """
        Mostra as últimas 5 interações do usuário e do bot no chat.
        """
        ultimas_interacoes = self.historico.ler_ultimos_gui(5)  # supondo que você tenha ler_ultimos_gui
        for usuario_msg, bot_msg in ultimas_interacoes:
            self.adicionar_mensagem(f"Você: {usuario_msg}", usuario=True, cor_fundo_custom="#6b5b95")
            self.adicionar_mensagem(f"Bot: {bot_msg}", usuario=False, cor_fundo_custom="#88b04b")


if __name__ == "__main__":
    app = Root()
    app.mainloop()
