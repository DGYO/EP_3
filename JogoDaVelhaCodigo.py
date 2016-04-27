# -*- coding: utf-8 -*-
import numpy as np


class JogoDaVelha:
    def __init__(self):
        self.base = np.zeros((3,3))
        self.jogador = 1
        self.conPlayer1 = 0
        self.conPlayer2 = 0        
        
    def show_game(self):
        print(self.base)

    
    def recebe_jogada(self,i,j):
        self.base[i][j] = self.jogador
        if self.jogador == 1:
            self.jogador = 2
        else:
            self.jogador = 1
            
    def verifica_ganhador(self):
        if self.base[0][0] == self.base[0][1] and \
           self.base[0][0] == self.base[0][2] and \
           not self.base[0][2] == 0:
            return self.base[0][2]
        elif self.base[1][0] == self.base[1][1] and \
            self.base[1][0] == self.base[1][2] and \
            not self.base[1][2] == 0:
                return self.base[1][2]
        elif self.base[2][0] == self.base[2][1] and\
            self.base[2][0] == self.base[2][2] and\
            not self.base[2][2] == 0:
                return self.base[2][2]
        elif self.base[0][0] == self.base[1][0] and\
           self.base[1][0] == self.base[2][0] and\
           not self.base[2][0] == 0:
               return self.base[2][0]
        elif self.base[0][1] == self.base[1][1] and\
           self.base[1][1] == self.base[2][1] and\
           not self.base[2][1] == 0:
               return self.base[2][1]
        elif self.base[0][2] == self.base[1][2] and\
           self.base[1][2] == self.base[2][2] and\
           not self.base[2][2] == 0:
               return self.base[2][2]
        elif self.base[0][0] == self.base[1][1] and\
           self.base[0][0] == self.base[2][2] and\
           not self.base[0][0] == 0:
               return self.base[0][0]
        elif self.base[0][2] == self.base[1][1] and\
           self.base[2][0] == self.base[0][2] and\
           not self.base[0][2] == 0:
            return self.jogador
        elif not self.base[0][0] == 0 and\
        not self.base[0][1] == 0 and\
        not self.base[0][2] == 0 and\
        not self.base[1][0] == 0 and\
        not self.base[1][1] == 0 and\
        not self.base[1][2] == 0 and\
        not self.base[2][0] == 0 and\
        not self.base[2][1] == 0 and\
        not self.base[2][2] == 0:
            return 3
        else:
            return -1
        
        
    def limpa_jogada(self):
        self.base = np.zeros((3,3))
        if self.verifica_ganhador == 1:
            self.conPlayer1 += 1
        elif self.verifica_ganhador == 2:
            self.conPlayer2 += 1