import tkinter as tk
import JogoDaVelhaCodigo

class Tabuleiro:
    def __init__(self):
        self.game = JogoDaVelhaCodigo.JogoDaVelha()
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




        self.botão1 = tk.Button(self.window)
        self.botão1.configure(command=self.click_botão1)
        self.botão1.configure(font = "Arial 60 bold")
        self.botão1.grid(row=0, column=0, sticky="nsew")
        
        self.botão2 = tk.Button(self.window)
        self.botão2.configure(command=self.click_botão2)
        self.botão2.configure(font = "Arial 60 bold")
        self.botão2.grid(row=1, column=0, sticky="nsew")
        
        self.botão3 = tk.Button(self.window)
        self.botão3.configure(command=self.click_botão3)
        self.botão3.configure(font = "Arial 60 bold")
        self.botão3.grid(row=2, column=0, sticky="nsew")
        
        self.botão4 = tk.Button(self.window)
        self.botão4.configure(command=self.click_botão4)
        self.botão4.configure(font = "Arial 60 bold")
        self.botão4.grid(row=0, column=1, sticky="nsew")
        
        self.botão5 = tk.Button(self.window)
        self.botão5.configure(command=self.click_botão5)
        self.botão5.configure(font = "Arial 60 bold")
        self.botão5.grid(row=1, column=1, sticky="nsew")
        
        self.botão6 = tk.Button(self.window)
        self.botão6.configure(command=self.click_botão6)
        self.botão6.configure(font = "Arial 60 bold")
        self.botão6.grid(row=2, column=1, sticky="nsew")
        
        self.botão7 = tk.Button(self.window)
        self.botão7.configure(command=self.click_botão7)
        self.botão7.configure(font = "Arial 60 bold")
        self.botão7.grid(row=0, column=2, sticky="nsew")
        
        self.botão8 = tk.Button(self.window)
        self.botão8.configure(command=self.click_botão8)
        self.botão8.configure(font = "Arial 60 bold")
        self.botão8.grid(row=1, column=2, sticky="nsew")
        
        self.botão9 = tk.Button(self.window)
        self.botão9.configure(command=self.click_botão9)
        self.botão9.configure(font = "Arial 60 bold")
        self.botão9.grid(row=2, column=2, sticky="nsew")
        
        self.botão_reset = tk.Button(self.window)
        self.botão_reset.grid(row=3, sticky="nsew")
        self.botão_reset.configure(command=self.reset)
        
        
    def reset (self):
        self.game.limpa_jogadas()
        self.botão1.configure(text="")
        self.botão2.configure(text="")
        self.botão3.configure(text="")
        self.botão4.configure(text="")
        self.botão5.configure(text="")        
        self.botão6.configure(text="")
        self.botão7.configure(text="")
        self.botão8.configure(text="")
        self.botão9.configure(text="")        
            
    def click_botão1(self):
        if self.game.jogador == 1:
            self.botão1.configure(text="X")
        else:
            self.botão1.configure(text="O")
            
        self.game.recebe_jogada(0,0)
        
        if self.game.verifica_ganhador() == 1: 
            self.botão_reset.configure(text="SALVE X! (JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 2:
            self.botão_reset.configure(text="SALVE O!(JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 0: 
            self.botão_reset.configure(text="Ninguém, tente outra vez! (JOGUE DE NOVO!) ")
                
    def click_botão2(self):
        if self.game.jogador == 1:
            self.botão2.configure(text="X")
        else:
            self.botão2.configure(text="O")
            
        self.game.recebe_jogada(0,1)
        
        if self.game.verifica_ganhador() == 1: 
            self.botão_reset.configure(text="SALVE X! (JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 2:
            self.botão_reset.configure(text="SALVE O!(JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 0: 
            self.botão_reset.configure(text="Ninguém, tente outra vez! (JOGUE DE NOVO!) ")
            
    def click_botão3(self):
        if self.game.jogador == 1:
            self.botão3.configure(text="X")
        else:
            self.botão3.configure(text="O")
            
        self.game.recebe_jogada(0,2)
        
        if self.game.verifica_ganhador() == 1: 
            self.botão_reset.configure(text="SALVE X! (JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 2:
            self.botão_reset.configure(text="SALVE O!(JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 0: 
            self.botão_reset.configure(text="Ninguém, tente outra vez! (JOGUE DE NOVO!) ")
            
    def click_botão4(self):
        if self.game.jogador == 1:
            self.botão4.configure(text="X")
        else:
            self.botão4.configure(text="O")
            
        self.game.recebe_jogada(1,0)
        
        botão = tk.Button(self.window)
        botão.grid(row=0, column=0, sticky="nsew")
                
        botão2 = tk.Button(self.window)
        botão2.grid(row=1, column=0, sticky="nsew")

        
        if self.game.verifica_ganhador() == 1: 
            self.botão_reset.configure(text="SALVE X! (JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 2:
            self.botão_reset.configure(text="SALVE O!(JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 0: 
            self.botão_reset.configure(text="Ninguém, tente outra vez! (JOGUE DE NOVO!) ")
            
    def click_botão5(self):
        if self.game.jogador == 1:
            self.botão5.configure(text="X")
        else:
            self.botão5.configure(text="O")
            
        self.game.recebe_jogada(1,1)
        
        if self.game.verifica_ganhador() == 1: 
            self.botão_reset.configure(text="SALVE X! (JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 2:
            self.botão_reset.configure(text="SALVE O!(JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 0: 
            self.botão_reset.configure(text="Ninguém, tente outra vez! (JOGUE DE NOVO!) ")
            
    def click_botão6(self):
        if self.game.jogador == 1:
            self.botão6.configure(text="X")
        else:
            self.botão6.configure(text="O")
            
        self.game.recebe_jogada(1,2)
        
        if self.game.verifica_ganhador() == 1: 
            self.botão_reset.configure(text="SALVE X! (JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 2:
            self.botão_reset.configure(text="SALVE O!(JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 0: 
            self.botão_reset.configure(text="Ninguém, tente outra vez! (JOGUE DE NOVO!) ")
            
    def click_botão7(self):
        if self.game.jogador == 1:
            self.botão7.configure(text="X")
        else:
            self.botão7.configure(text="O")
            
        self.game.recebe_jogada(2,0)
        
        if self.game.verifica_ganhador() == 1: 
            self.botão_reset.configure(text="SALVE X! (JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 2:
            self.botão_reset.configure(text="SALVE O!(JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 0: 
            self.botão_reset.configure(text="Ninguém, tente outra vez! (JOGUE DE NOVO!) ")
            
    def click_botão8(self):
        if self.game.jogador == 1:
            self.botão8.configure(text="X")
        else:
            self.botão8.configure(text="O")
            
        self.game.recebe_jogada(2,1)
        
        if self.game.verifica_ganhador() == 1: 
            self.botão_reset.configure(text="SALVE X! (JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 2:
            self.botão_reset.configure(text="SALVE O!(JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 0: 
            self.botão_reset.configure(text="Ninguém, tente outra vez! (JOGUE DE NOVO!) ")
            
    def click_botão9(self):
        if self.game.jogador == 1:
            self.botão9.configure(text="X")
        else:
            self.botão9.configure(text="O")
            
        self.game.recebe_jogada(2,2)
        
        if self.game.verifica_ganhador() == 1: 
            self.botão_reset.configure(text="SALVE X! (JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 2:
            self.botão_reset.configure(text="SALVE O!(JOGUE DE NOVO!)")
        elif self.game.verifica_ganhador() == 0: 
            self.botão_reset.configure(text="Ninguém, tente outra vez! (JOGUE DE NOVO!) ")
        
    def iniciar(self):
        self.window.mainloop()
        

app = Tabuleiro()
app.iniciar()