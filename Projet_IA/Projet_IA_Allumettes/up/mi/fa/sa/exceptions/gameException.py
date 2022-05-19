#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:49:48 2022

@author: ANANDARAJ Suvéta
@author: ADOTRI Frimpong
"""

"""
Ce module contient une exception non native de Python à gérer pour le bon fonctionnement du jeu
"""

# IMPORT DES MODULES
from dataclasses import dataclass
import colorama


@dataclass
class GameException(Exception):
    __exception_message : str
    
    
    
    def __post_init__(self) -> None :
        """
        Cette méthode exécute toutes les instructions qui y sont définies automatiquement après
        une instanciation de la classe GameException

        Returns
        -------
        None
        
        """
        self.__exception_message = f"{colorama.Fore.RED}{colorama.Style.BRIGHT}\nGame Exception : {colorama.Style.RESET_ALL}" + self.__exception_message
        
    
    
    def toString(self) -> str:
        """
        Cette méthode retourne le message d'exception correspondant

        Returns
        -------
        str
            DESCRIPTION. Message d'exception explicite à afficher en cas d'exception levée
            
        """
        return self.__exception_message
