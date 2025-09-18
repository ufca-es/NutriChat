import tkinter as tk
from tkinter import messagebox

class CaixaMensagem(tk.Frame):
    """Caixa para o usuário digitar uma mensagem"""
    def __init__(self, master, enviar_callback, altura=5, largura=40, **kwargs):
        super().__init__(master, **kwargs)
        self.enviar_callback = enviar_callback
        self.texto = tk.Text(self, height=altura, width=largura)
        self.texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.botao_enviar = tk.Button(self, text="Enviar", command=self.enviar_mensagem)
        self.botao_enviar.pack(side=tk.RIGHT)
        self.texto.bind("<Return>", self.enviar_mensagem_event)


    def enviar_mensagem_event(self, event):
        self.enviar_mensagem()
        return "break"

    def enviar_mensagem(self):
        mensagem = self.texto.get("1.0", tk.END).strip()
        if mensagem:
            self.enviar_callback(mensagem)
            self.texto.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite uma mensagem antes de enviar!")