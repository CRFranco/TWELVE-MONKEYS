#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
Created on 24 de mai de 2016

@author: cristiano.franco
'''
from versao1_entities.alimentos import *


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
        raise NotImplementedError("A subclasse deve fornecer uma implementacao")
    
    
    descricao = property(get_descricao, del_descricao, "descricao's docstring")
    life = property(get_life, del_life, "life's docstring")
            
    def digerir(self, alimento):
        
        print(" comendo ", type(alimento[0]))
        alimento.pop()
        self._life += 1
        print("aumentando a vida do macaco para", self._life)
        
            


class MacacoPrego(Macaco):
    
    def comer(self, alimento):
        
        if(len(alimento) > 0 and type(alimento[0]) is Banana):
            super(MacacoPrego, self).digerir(alimento)
        else: 
            print("Esse tipo de macaco somente come banana")
            self._life -= 1
            print("diminuindo a vida do macaco para", self._life)
        


class MicoSagui(Macaco):
    
    def comer(self, alimento):
        if(len(alimento) > 0 and (type(alimento[0]) is Fruta or type(alimento[0]) is Banana)):
            super(MicoSagui, self).digerir(alimento)
        else: 
            print("Esse tipo de macaco somente come frutas")
            self._life -= 1
            print("diminuindo a vida do macaco para", self._life)
            



class MacacoZumbi(Macaco):
    
    def comer(self, alimento):
        if(len(alimento) > 0 and type(alimento[0]) is Macaco):
            super(MacacoZumbi, self).digerir(alimento)
        else: 
            print("Esse tipo de macaco somente come Macacos")
            self._life -= 1   
            print("diminuindo a vida do macaco ", self._life) 
