import tkinter as tk
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








Nome = input('Diga seu nome ? ')

print(f'Então {Nome} acorda em sua casa como mais um dia!')

def decisaocama (): 
    input('Levantar da cama ? ').strip().lower()

    if decisaocama == 'Sim':
        print(f'{Nome} levanta de sua cama e percebe algo estranho')

    elif decisaocama == 'Nao':
        print(f'{Nome} decide continuar deitado e tirar mais um leve cochilo')
