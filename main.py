# simple clock with TKinter
# William dos Santos Junqueira

from tkinter import *
from time import ctime
# estilo Label
estilolb = {
     'font': 'LEMON/MILK 40'
}


class App:
    def __init__ (self, master):

        self.master = master
        self.tempo = StringVar()
        self.tempo.set(self.horaAtual())

        # lb que mostra o titulo da janela
        self.lb_til = Label(self.master, font='Arial 20', text='Clock')
        self.lb_til.pack()


        # Criação do label que mostra a hora
        self.lb = Label(self.master, estilolb, textvariable=self.tempo, )
        self.lb.pack(pady=5)
        
        self.mostrarHora()
    

    # retorna a hora atual
    def horaAtual(self):        
        t = ctime()
        return(t[10:19])
    

    #  pega a hora atual e mostra no label
    def mostrarHora(self):  
        self.tempo.set(self.horaAtual())
        self.lb.after(1000, self.mostrarHora)


root = Tk()

App(root)
root.geometry('300x150')
root.title('Clock')
root.resizable(0, 0)

root.mainloop()
