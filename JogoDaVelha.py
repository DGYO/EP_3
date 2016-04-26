# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:44:18 2016

@author: frana
"""
import numpy as np


class JogoDaVelha:
    def __init__(self,x):
        self.base = np.zeros((x,x))
        #Jogador varia entre 1(X) e 2(O)
        
        
        
        
        
        
    def rodada(self,jogador,base,jogada):
        if jogada == 7 and base[0][0] == 0:
            base[0][0] = jogador
        elif jogada == 8 and base[0][1] == 0:
            base[0][1] = jogador
        elif jogada == 9 and base[0][2] == 0:
            base[0][2] = jogador
        elif jogada == 4 and base[1][0] == 0:
            base[1][0] = jogador
        elif jogada == 5 and base[1][1] == 0:
            base[1][1] = jogador
        elif jogada == 6 and base[1][2] == 0:
            base[1][2] = jogador
        elif jogada == 1 and base[2][0] == 0:
            base[2][0] = jogador
        elif jogada == 2 and base[2][1] == 0:
            base[2][1] = jogador
        elif jogada == 3 and base[2][2] == 0:
            base[2][2] = jogador
        
        
    def vitoria(self,base,jogador):
        if base[0][0] == base[0][1] and base[0][0] == base[0][2] and not base[0][2] == 0 or base[1][0] == base[1][1] and base[1][0] == base[1][2] and not base[1][2] == 0 or base[2][0] == base[2][1] and base[2][0] == base[2][2] and not base[2][2] == 0 or base[0][0] == base[1][0] and base[1][0] == base[2][0] and not base[2][0] == 0 or base[0][1] == base[1][1] and base[1][1] == base[2][1] and not base[2][1] == 0 or base[0][2] == base[1][2] and base[1][2] == base[2][2] and not base[2][2] == 0 or base[0][0] == base[1][1] and base[0][0] == base[2][2] and not base[0][0] == 0 or base[0][2] == base[1][1] and base[2][0] == base[0][2] and not base[0][2] == 0:
            return jogador
        elif not base[0][0] == 0 and not base[0][1] == 0 and not base[0][2] == 0 and not base[1][0] == 0 and not base[1][1] == 0 and not base[1][2] == 0 and not base[2][0] == 0 and not base[2][1] == 0 and not base[2][2] == 0:
            print('Deu Velha')
            return 3
        else:
            return 0
        
            
    def fim_rodada(self):
        if self.jogador == 1:
            self.jogador = 2
        else:
            self.jogador = 1
            
    def show_player(self):
        return self.jogador
            
    def show_game(self,base):
        print(base)



    def game_play(self,jogador):
        
        print('Vez do Jogador: ',jogador)
        play = int(input('Inserir um n° de 1-9: '))
        self.rodada(jogador,self.base,play)
        self.show_game(self.base)
        vitoria = self.vitoria(self.base,jogador)
        if vitoria == 1 or vitoria == 2:
            print('VicTory')
            print('Jogador ',jogador,' Venceu!!!!')
            return 1
        elif vitoria == 3:
            return 1
        else:
            self.fim_rodada
            return 0
    


a = JogoDaVelha(3)
print(a.base)
jogador = 2
h = 0
while h == 0:
    if jogador == 2:
        jogador = 1
    elif jogador == 1:
        jogador = 2
    h = a.game_play(jogador)



'''
base[0][0] == base[0][1] and base[0][0] == base[0][2] and not base[0][2] == 0 or
base[1][0] == base[1][1] and base[1][0] == base[1][2] and not base[1][2] == 0 or
base[2][0] == base[2][1] and base[2][0] == base[2][2] and not base[2][2] == 0 or
base[0][0] == base[1][0] and base[1][0] == base[2][0] and not base[2][0] == 0 or
base[0][1] == base[1][1] and base[1][1] == base[2][1] and not base[2][1] == 0 or
base[0][2] == base[1][2] and base[1][2] == base[2][2] and not base[2][2] == 0 or
base[0][0] == base[1][1] and base[0][0] == base[2][2] and not base[0][0] == 0 or
base[0][2] == base[1][1] and base[2][0] == base[0][2] and not base[0][2] == 0
'''