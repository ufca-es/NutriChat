import tkinter as tk
from tkinter import messagebox

class CaixaMensagem(tk.Frame):
    """Caixa para o usuário digitar uma mensagem"""
    def __init__(self, master, enviar_callback, altura=5, largura=40, **kwargs):
        super().__init__(master, **kwargs)
        
        self.enviar_callback = enviar_callback  # função que será chamada ao enviar a mensagem

        # Campo de texto
        self.texto = tk.Text(self, height=altura, width=largura)
        self.texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

        # Botão de enviar
        self.botao_enviar = tk.Button(self, text="Enviar", command=self.enviar_mensagem)
        self.botao_enviar.pack(side=tk.RIGHT)

        # Permite enviar mensagem pressionando Enter (return = Enter)
        self.texto.bind("<Return>", self.enviar_mensagem_event)
    
    def enviar_mensagem_event(self, event):
        """Chamada quando Enter é pressionado"""
        # Evita quebrar a linha no Text
        self.enviar_mensagem()
        return "break"

    def enviar_mensagem(self):
        """Pega o texto digitado e chama o callback"""
        #1.0 significa pegar do início, tk.END até o final
        mensagem = self.texto.get("1.0", tk.END).strip()
        if mensagem:
            self.enviar_callback(mensagem)
             #limpa o campo
            self.texto.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite uma mensagem antes de enviar!")