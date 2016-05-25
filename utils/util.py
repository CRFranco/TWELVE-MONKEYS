#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
Created on 25 de mai de 2016

@author: cristiano.franco
'''

from random import randint
import versao1_entities.macacos as v1
import versao2_entities.macacos as v2
from abc import abstractclassmethod

class Util:
    @abstractclassmethod
    def geraMacacos1(self, quantidadeMacacos):
        
        macacos = []
        for i in range (quantidadeMacacos):
            j = randint(0, quantidadeMacacos-1)
            if (j >= 0 and j < 4):
                macacos.append(v1.MacacoPrego("Macaco Prego"))
            elif (j >= 4 and j < 8):
                macacos.append(v1.MicoSagui("Mico Sagui"))
            else:
                macacos.append(v1.MacacoZumbi("Macaco Zumbi"))
        
        return macacos
    
    
    @abstractclassmethod
    def geraMacacos2(self, quantidadeMacacos):
        
        macacos = []
        for i in range (quantidadeMacacos):
            j = randint(0, quantidadeMacacos-1)
            if (j >= 0 and j < 4):
                macacos.append(v2.MacacoPrego("Macaco Prego"))
            elif (j >= 4 and j < 8):
                macacos.append(v2.MicoSagui("Mico Sagui"))
            else:
                macacos.append(v2.MacacoZumbi("Macaco Zumbi"))
        
        return macacos
    
    @abstractclassmethod
    def interface(self):
        quantidades = []
        quantidades.append(int(input('Digite a quantidade disponível de frutas:')))
        quantidades.append(int(input('Digite a quantidade disponível de bananas:')))
        quantidades.append(int(input('Digite a quantidade disponível de macacos: (Os tipos serão definidos aleatoriamente)')))
        
        return quantidades