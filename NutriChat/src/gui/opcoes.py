from tkinter import messagebox

# Classe usada para exibir diferentes tipos de caixas de diálogo
class Dialogos:
    
    def info(titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    def aviso(titulo, mensagem):
        messagebox.showwarning(titulo, mensagem)

    def erro(titulo, mensagem):
        messagebox.showerror(titulo, mensagem)

    def confirmar(titulo, mensagem):
        return messagebox.askyesno(titulo, mensagem)

    def ok_cancel(titulo, mensagem):
        return messagebox.askokcancel(titulo, mensagem)

    def retry_cancel(titulo, mensagem):
        return messagebox.askretrycancel(titulo, mensagem)
