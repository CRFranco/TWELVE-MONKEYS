#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
Created on 24 de mai de 2016

@author: cristiano.franco
'''
from random import randint
from versao1_entities.alimentos import *
from versao1_entities.macacos import *
from utils.util import Util



    

if __name__ == "__main__":
    
    FRUTAS = 0
    BANANAS = 1
    MACACOS = 2
    
    print("VERSÃO 1 \n\n")
    _quantidades = Util.interface()
        
    # listas de alimentos
    frutas = []
    for i in range (_quantidades[FRUTAS]):
        frutas.append(Fruta("Fruta"))
        
    bananas = []
    for i in range (_quantidades[BANANAS]):
        bananas.append(Banana("Banana"))
        
    macacos = Util.geraMacacos1(_quantidades[MACACOS])
   
        
    alimentos = []
    alimentos.append(frutas)
    alimentos.append(bananas)
    alimentos.append(macacos)
       
    
    while (len(macacos) > 0):
         
        alimento = alimentos[randint(0, len(alimentos) - 1)]
        i = randint(0, (len(macacos) - 1))
        
        
        print("\n\n Peguei macaco do tipo ",type(macacos[i]))
        macacos[i].comer(alimento)
        
        if(macacos[i]._life == 0):
            print(type(macacos[i]), " morreu com ", macacos[i]._life)
            macacos.pop(i)
            print(len(macacos), " macacos sobraram")
        
            
    print("Todos os macacos morreram")
    
