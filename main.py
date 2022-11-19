# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:00:03 2022

@author: fsdalpiaz
"""

import datetime as dt
from guizero import *
import queue as que

def open_ticket_window():
    ticketwindow.show()
def open_call_window():
    callwindow.show()


cont = 0

class Ticket:
    def __init__(self, tipo, numero):
        self.datenow = dt.datetime.now()
        self.tipo = tipo
        self.numero = numero
#janela principal
windowmenu = App(title="Menu Principal",
                    width=720,
                    height=350,
                    layout="grid",
                    visible=True,
                    bg="black")
#configurações da janela principal
buttonbox = Box(windowmenu, layout="grid", border=80, grid=[0,0], visible=True, enabled=True)
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
                        visible=True,
                        bg="gray")
ticketwindow.hide()
#configurações da janela ticket
ticketbuttonbox = Box(ticketwindow, layout="grid", visible=True, enabled=True)
ticketbuttonbox.set_border(20, "gray")
generatepriorticket = PushButton(ticketbuttonbox, text=f"Prioritário", padx=100, pady=50, grid=[0,0])
generatenormalticket = PushButton(ticketbuttonbox, text=f"Normal", padx=100, pady=50, grid=[1,0])
generatepriorticket.bg = "yellow"
generatenormalticket.bg = "white"
generatepriorticket.text_size = 20
generatenormalticket.text_size = 20
#caixa de tickets gerados - fila
ticketlist = ListBox(ticketwindow,
                     width=500,
                     height=400,
                     scrollbar=True)
ticketlist.bg = "white"


#janela atendimento
callwindow = Window(windowmenu,
                        title="Gerar Tickets de Atendimento",
                        width=1000,
                        height=1000,
                        layout="auto",
                        visible=True,
                        bg="gray")
callwindow.hide()
#configurações da janela atendimento
callsbuttonbox = Box(callwindow, layout="grid", visible=True, enabled=True)
callsbuttonbox.set_border(20, "gray")
callpeople = PushButton(callsbuttonbox, text=f"Atender", padx=100, pady=50, grid=[0,0])
callpeople.bg = "white"
callpeople.text_size = 20
#caixa de tickets gerados - fila
callList = ListBox(callwindow, width=500, height=400)
callList.bg = "white"



#reproduz a GUI
windowmenu.display()