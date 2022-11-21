# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:00:03 2022

@author: fsdalpiaz
"""

# don't forget to access https://lawsie.github.io/guizero/
# and https://docs.python.org/3/library/queue.html#module-queue
# and https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime
# to get more information about these important packages

import datetime as dt
from guizero import *
import queue as fila

#classes
class Ticket:
    def __init__(self, tipo, numero):
        self.datenow = dt.datetime.now()
        self.tipo = tipo
        self.numero = numero

#funções
def open_ticket_window():
    ticketwindow.show()
def open_call_window():
    callwindow.show()

def gera_ticket_normal():
    global contticket
    ticketnormal = Ticket("normal", contticket)
    ticketlistnormal.append(f"Ticket {ticketnormal.tipo}, Número: {ticketnormal.numero},"
                            f" Data: {ticketnormal.datenow.day}/{ticketnormal.datenow.month},"
                            f" Hora:{ticketnormal.datenow.hour}:{ticketnormal.datenow.minute}:{ticketnormal.datenow.second}")
    normalQueue.put(ticketnormal)
    ticketlistnormal.show()
    contticket += 1

def gera_ticket_prior():
    global contticket
    ticketprior = Ticket("Prioritário", contticket)
    ticketlistprior.append(f"Ticket {ticketprior.tipo}, Número: {ticketprior.numero},"
                            f" Data: {ticketprior.datenow.day}/{ticketprior.datenow.month},"
                            f" Hora:{ticketprior.datenow.hour}:{ticketprior.datenow.minute}:{ticketprior.datenow.second}")
    priorityQueue.put(ticketprior)
    ticketlistprior.show()
    contticket += 1

def atende_bem():
    global cont
    global calling
    if len(calling) > 0:
        calling.clear()
    if priorityQueue.empty() == True and normalQueue.empty() == True:
        callpeople.enabled = False
        callwindow.warn("Atenção", "Você não tem atendimentos registrados!")
        callpeople.enabled = True
    else:
        if cont == 2 and priorityQueue.empty() == False:
            ncalledticket = priorityQueue.get()
            callList.append(f"Ticket {ncalledticket.tipo}, Número: {ncalledticket.numero},"
                            f" Data: {ncalledticket.datenow.day}/{ncalledticket.datenow.month},"
                            f" Hora:{ncalledticket.datenow.hour}:{ncalledticket.datenow.minute}:{ncalledticket.datenow.second}")
            calling.append(f"Ticket {ncalledticket.tipo}, Número: {ncalledticket.numero}"
                       f" Data: {ncalledticket.datenow.day}/{ncalledticket.datenow.month}"
                       f" Hora:{ncalledticket.datenow.hour}:{ncalledticket.datenow.minute}:{ncalledticket.datenow.second}")
            callList.show()
            cont = 0
        elif cont != 2 and normalQueue.empty() == True:
            ncalledticket = priorityQueue.get()
            callList.append(f"Ticket {ncalledticket.tipo}, Número: {ncalledticket.numero},"
                            f" Data: {ncalledticket.datenow.day}/{ncalledticket.datenow.month},"
                            f" Hora:{ncalledticket.datenow.hour}:{ncalledticket.datenow.minute}:{ncalledticket.datenow.second}")
            calling.append(f"Ticket {ncalledticket.tipo}, Número: {ncalledticket.numero}"
                           f" Data: {ncalledticket.datenow.day}/{ncalledticket.datenow.month}"
                           f" Hora:{ncalledticket.datenow.hour}:{ncalledticket.datenow.minute}:{ncalledticket.datenow.second}")
            callList.show()
            cont = 0
        else:
            ncalledticket = normalQueue.get()
            callList.append(f"Ticket {ncalledticket.tipo}, Número: {ncalledticket.numero},"
                            f" Data: {ncalledticket.datenow.day}/{ncalledticket.datenow.month},"
                            f" Hora:{ncalledticket.datenow.hour}:{ncalledticket.datenow.minute}:{ncalledticket.datenow.second}")
            calling.append(f"Ticket {ncalledticket.tipo}, Número: {ncalledticket.numero}"
                           f" Data: {ncalledticket.datenow.day}/{ncalledticket.datenow.month}"
                           f" Hora:{ncalledticket.datenow.hour}:{ncalledticket.datenow.minute}:{ncalledticket.datenow.second}")
            callList.show()
            cont += 1
        whocalled.value = calling[0]
        whocalled.show()


#cria filas, listas e contadores
priorityQueue = fila.Queue(maxsize=0)
normalQueue = fila.Queue(maxsize=0)
contticket = 1
cont = 0
calling = []


#janela principal
windowmenu = App(title="Menu Principal",
                    width=720,
                    height=350,
                    layout="grid",
                    bg="black")
windowmenu.focus()
#configurações da janela principal
buttonbox = Box(windowmenu, layout="grid", border=80, grid=[0,0])
ticketswindowbutton = PushButton(buttonbox, text=f"Gerar Ticket", command=open_ticket_window, padx=50, pady=50, grid=[0,0])
callswindowbutton = PushButton(buttonbox, text=f"Atendimento",command=open_call_window, padx=60, pady=50, grid=[1,0])
ticketswindowbutton.bg = "white"
callswindowbutton.bg = "white"
ticketswindowbutton.text_size = 20
callswindowbutton.text_size = 20

#janela ticket
ticketwindow = Window(windowmenu,
                        title="Gerar Tickets de Atendimento",
                        width=1000,
                        height=1000,
                        layout="auto",
                        bg="gray")
ticketwindow.hide()
#configurações da janela ticket
#Box que encapsula os botões
ticketbuttonbox = Box(ticketwindow, layout="grid")
ticketbuttonbox.set_border(20, "gray")
#botões
generatenormalticket = PushButton(ticketbuttonbox, command=gera_ticket_normal, text=f"Normal", padx=100, pady=50, grid=[0,0])
generatepriorticket = PushButton(ticketbuttonbox, command=gera_ticket_prior, text=f"Prioritário", padx=100, pady=50, grid=[1,0])
generatepriorticket.bg = "yellow"
generatenormalticket.bg = "white"
generatepriorticket.text_size = 20
generatenormalticket.text_size = 20
#Box que encapsula as listbox
listsbox = Box(ticketwindow, layout="grid")
ticketbuttonbox.set_border(20, "gray")
#caixa de tickets gerados - fila normal
ticketlistnormal = ListBox(listsbox,
                            width=400,
                            height=400,
                            scrollbar=True,
                            grid=[0,0])
ticketlistnormal.bg = "white"
#caixa de tickets gerados - fila prioritária
ticketlistprior = ListBox(listsbox,
                            width=400,
                            height=400,
                            scrollbar=True,
                            grid=[1,0])
ticketlistprior.bg = "white"


#janela atendimento
callwindow = Window(windowmenu,
                    title="Gerar Tickets de Atendimento",
                    width=1000,
                    height=1000,
                    layout="auto",
                    bg="gray")
callwindow.hide()
#configurações da janela atendimento
callsbuttonbox = Box(callwindow, layout="grid")
callsbuttonbox.set_border(20, "gray")
#botão
callpeople = PushButton(callsbuttonbox, text=f"Atender", command=atende_bem, padx=100, pady=50, grid=[0,0])
callpeople.bg = "white"
callpeople.text_size = 20
#caixa de texto, mostra atendimento atual
called = TitleBox(callwindow, text=f"Em Atendimento: ", width=600, height=65)
whocalled = Text(called, text="", font="Arial", size=14)
whocalled.hide()
#caixa de tickets gerados - fila
callList = ListBox(callwindow,
                   width=500,
                   height=400,
                   scrollbar=True)
callList.bg = "white"


#reproduz a GUI
windowmenu.display()