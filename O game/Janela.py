from tkinter import *
janela
#função de criar a janela
def criar_janela():
    #criação de janela principal
    root = tk.Tk()
    root.title('Game')

    #Criação de texto e adição a janela
    texto = tk.Label(root, text='Teste!')
    texto.pack(padx=20, pady=20)

    #Iniciar loop principal da interface gráfica
    root.mainloop()

#chamar função para criar janela
criar_janela
