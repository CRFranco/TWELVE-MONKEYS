#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
Created on 24 de mai de 2016
@author: cristiano.franco
'''

from random import randint

class Macaco :
    _descricao = None
    _life = 0
    
    def __init__(self, descricao):
        self._descricao = descricao
        self._life = 5

    def get_descricao(self):
        return self.__descricao


    def get_life(self):
        return self.__life


    def del_descricao(self):
        del self.__descricao


    def del_life(self):
        del self.__life

        
        
    def comer(self, alimento):

        if(len(alimento) > 0):
            
            print("comendo ", type(alimento[0]))
            print("sobraram ",len(alimento)-1, type(alimento[0]))
            alimento.pop(0)
            self._life += 1
            print("aumentando a vida do", type(self), " para", self._life)
        else:
            self._life -= 1
            print("diminuindo a vida do", type(self), " para", self._life)
    
    descricao = property(get_descricao, del_descricao, "descricao's docstring")
    life = property(get_life, del_life, "life's docstring")
            
      
            


class MacacoPrego(Macaco):
    pass
   
        


class MicoSagui(Macaco):
    pass
    


class MacacoZumbi(Macaco):
    def comer(self, alimento):
        
       
        ''' O primeiro laço serve para impedir que um macaco zumbi coma a si mesmo, quando so existirem dois macacos
            e um deles é zumbi e o indice do alimento caia em si mesmo.
        '''
        indice = 0;
        
        while(self == alimento[indice] and len(alimento) > 1):
                indice = randint(0, len(alimento)-1)
         
        if(len(alimento) > 0 and self != alimento[indice]):
            
            
            print("comendo ", type(alimento[indice]))
            print("sobraram ",len(alimento)-1, type(alimento[indice]))
            alimento.pop(indice)
            self._life += 1
            print("aumentando a vida do", type(self), " para", self._life)
        else:
            self._life -= 1
            print("diminuindo a vida do", type(self), " para", self._life)
   
