#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
Created on 24 de mai de 2016

@author: cristiano.franco
'''



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
        
        if(len(alimento) > 1):
            
            print("\n",type(self), " comendo ", type(alimento[0]))
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
    pass
   
