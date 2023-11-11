from tkinter import*
from PIL import ImageTk, Image

root = Tk()

root.title('Options')

root.iconbitmap('logo.ico')

#criando participantes
part1 = Label(root, text='Participante 1')
part2 = Label(root, text='Participante 2')

#criando placares
placar1 = Entry(root, width=15, borderwidth=3, justify='right', font = ('System', 15), state= 'readonly', readonlybackground='#373A41', fg = '#ffffff')
placar2 = Entry(root, width=15, borderwidth=3, justify='right', font = ('System', 15), state= 'readonly', readonlybackground='#373A41', fg = '#ffffff')

#criando painel de perguntas
painel = Entry(root, width=50, borderwidth=3, justify='right', font = ('System', 15), state= 'readonly', readonlybackground='#373A41', fg = '#ffffff')

#definindo função do botão +1point do placar1 e 2
def click_1point(numero):
    placar1.config(state='normal')
    num_placar1=placar1.get() + str(numero)
    placar1.delete(0, END)
    placar1.insert(0, num_placar1)
    placar1.configure(state='readonly')

def click_1point2(numero):
    placar2.config(state='normal')
    num_placar2=placar2.get() + str(numero)
    placar2.delete(0, END)
    placar2.insert(0, num_placar2)
    placar2.configure(state='readonly')

#criando botão +1point 1 e 2
btn1 = Button(root, text='+1', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_1point(1))
btn2 = Button(root, text='+1', pady=15, font=('Helvetica', 9), bg='#373A41', fg='#ffffff', command=lambda: click_1point2(1))


#posicionando participantes, placares, painel de perguntas e botões +1point
part1.grid(row=0, column=0)
placar1.grid(row=1,column=0)

part2.grid(row=0, column=4)
placar2.grid(row=1,column=4)

painel.grid(row=0, column=2, rowspan=4, columnspan=2)

btn1.grid(row=2, column=0)
btn2.grid(row=2, column=4)










root.mainloop()