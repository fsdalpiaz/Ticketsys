# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:00:03 2022

@author: fsdalpiaz
"""

import datetime as dt
from guizero import *
import queue as que

cont = 0

class Ticket:
    def __init__(self, tipo, numero):
        self.datenow = dt.datetime.now()
        self.tipo = tipo
        self.numero = numero

janelamenu = App(title="Tickets",
                    width=500,
                    height=600,
                    layout="grid", 
                    visible=True, 
                    bg="#ADD8E6")

windowtickets = Box(janelamenu, grid=[250,0])
ticketsbutton = PushButton(windowtickets, padx=50)
callwindow = Box(janelamenu, grid=[251,0])
callsbutton = PushButton(callwindow, padx=50)

janelamenu.display()