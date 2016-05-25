#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
Created on 24 de mai de 2016

@author: cristiano.franco
'''

from random import randint
from versao2_entities.alimentos import *
from versao2_entities.macacos import *
from utils.util import Util


if __name__ == "__main__":
    
    FRUTAS = 0
    BANANAS = 1
    MACACOS = 2
    
    print("VERSÃO 2 \n\n")
    _quantidades = Util.interface()
        
    # listas de alimentos
    frutas = []
    for i in range (_quantidades[FRUTAS]):
        frutas.append(Fruta("Fruta"))
        
    bananas = []
    for i in range (_quantidades[BANANAS]):
        bananas.append(Banana("Banana"))
        
    macacos = Util.geraMacacos2(_quantidades[MACACOS])
   
        
    alimentos = []
    alimentos.append(frutas)
    alimentos.append(bananas)
    alimentos.append(macacos)
    
    
    while (len(macacos) > 1):
         
        
        i = randint(0, (len(macacos) - 1))
        macacoDaVez = macacos[i]
        
        print("\n\n Peguei macaco do tipo ", type(macacoDaVez))
        
        if(type(macacoDaVez) is MicoSagui):
            if(len(frutas) > 0):
                macacoDaVez.comer(frutas)
            elif(len(bananas)>0):
                macacoDaVez.comer(bananas)
                            
        elif (type(macacoDaVez) is MacacoPrego):
            if(len(bananas)>0):
                macacoDaVez.comer(bananas)
                           
        else:
            macacoDaVez.comer(macacos)    
        
        if(macacoDaVez._life == 0):
            print(type(macacoDaVez), " morreu com ", macacoDaVez._life)
            macacos.pop(i)
            print(len(macacos), " macacos sobraram")
        
            
    print("Todos os macacos morreram")
