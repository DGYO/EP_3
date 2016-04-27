# -*- coding: utf-8 -*-
import tkinter as tk
from JogoDaVelhaCodigo import JogoDaVelha

class Tabuleiro:
    def __init__(self,Back):
        self.window = tk.Tk()
        self.window.geometry("600x650")
        self.window.title("Jogo da Velha")
        self.window.rowconfigure(0, minsize = 200 ,weight=1)
        self.window.rowconfigure(1, minsize = 200 ,weight=1)
        self.window.rowconfigure(2, minsize = 200 ,weight=1)
        self.window.rowconfigure(3, minsize = 50 ,weight=1)
        self.window.columnconfigure(0, minsize = 200 ,weight=1)
        self.window.columnconfigure(1, minsize = 200 ,weight=1)
        self.window.columnconfigure(2, minsize = 200 ,weight=1)
        
        
        botão = tk.Button(self.window)
        botão.grid(row=0, column=0, sticky="nsew")
                
        botão2 = tk.Button(self.window)
        botão2.grid(row=1, column=0, sticky="nsew")
        
        botão3 = tk.Button(self.window)
        botão3.grid(row=2, column=0, sticky="nsew")
        
        botão4 = tk.Button(self.window)
        botão4.grid(row=0, column=1, sticky="nsew")
        botão4.flash()
        
        botão5 = tk.Button(self.window)
        botão5.grid(row=1, column=1, sticky="nsew")
        
        botão6 = tk.Button(self.window)
        botão6.grid(row=2, column=1, sticky="nsew")
       
        botão7 = tk.Button(self.window)
        botão7.grid(row=0, column=2, sticky="nsew")
        
        botão8 = tk.Button(self.window)
        botão8.grid(row=1, column=2, sticky="nsew")
       
        botão9 = tk.Button(self.window)
        botão9.grid(row=2, column=2, sticky="nsew")
        
        botão10 = tk.Button(self.window)
        botão10.grid(row=3, column=0, sticky="nsew")
        
        
    def iniciar(self):
        self.window.mainloop()
        
b = JogoDaVelha()
a = Tabuleiro(b)
a.iniciar()

