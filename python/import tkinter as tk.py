import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
    messagebox.showinfo("Mensagem", "Olá, mundo!")

# Criar uma janela principal
janela = tk.Tk()
janela.title("Aplicativo Interativo")

# Criar um rótulo
rotulo = tk.Label(janela, text="Bem-vindo ao meu aplicativo!")
rotulo.pack()

# Criar um botão
botao = tk.Button(janela, text="Clique Aqui", command=exibir_mensagem)
botao.pack()

# Iniciar o loop de eventos
janela.mainloop()