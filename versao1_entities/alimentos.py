#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
Created on 24 de mai de 2016

@author: cristiano.franco
'''
class Fruta():

    def __init__(self, nome):
        self._descricao = nome
        
    def get_descricao(self):
        return self.__descricao


    def set_descricao(self, value):
        self.__descricao = value


    def del_descricao(self):
        del self.__descricao

    
    descricao = property(get_descricao, set_descricao, del_descricao, "descricao's docstring")
    
    
class Banana(Fruta):
    pass
    

    
    


