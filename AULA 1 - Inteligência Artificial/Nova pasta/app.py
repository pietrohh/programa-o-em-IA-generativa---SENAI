



import tkinter as tk 



def display():
    mostar_texto = dado.get()
    monstrar.config(text= mostar_texto)
    mostar_texto2 = dado2.get()
    monstrar2.config(text= mostar_texto2)


janela =  tk.Tk() # criar uma janela
janela.geometry('500x500')
tk.Label(janela, text='FOMULÁRIO').pack(pady=10)
tk.Label(janela, text='CADASTRE O E-MAIL').pack(pady=10)
dado = tk.Entry(janela)
dado.pack(pady=5)


tk.Label(janela, text='CADASTRE O NOME').pack(pady=10)
dado2 = tk.Entry(janela)
dado2.pack(pady=5)


btn = tk.Button(janela, text = 'Enviar', command=display)
btn.pack(pady=5)


monstrar = tk.Label(janela, text= '')
monstrar.pack()


monstrar2 = tk.Label(janela, text= '')
monstrar2.pack()


janela.mainloop()