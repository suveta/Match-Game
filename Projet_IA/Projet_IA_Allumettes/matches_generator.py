#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:27:37 2022

@author: ANANDARAJ Suvéta
@author: ADOTRI Frimpong

This unit/module regroups the functions that create the initial configuration on the game.



"""

from typing import List
from numpy import random

from up.mi.fa.sa.exceptions.gameException import GameException



def game_matches(matches_number:int) -> List[str]:
    """

    Creation du paleau de jeu

    Parameters
    ----------
    matches_number : int
        DESCRIPTION. Le nombre d'allumettes disponible dans le jeu'

    Raises
    ------
    gameException
        DESCRIPTION. Une exception est levée si une erreur est survenue

    Returns
    -------
    List[str]
        DESCRIPTION. une list avec le nombre d'allumettes données en paramètres'
    """
    
    if (type(matches_number) != int):
        raise GameException("Type mismatch !")
    if (matches_number % 2 != 0):
        raise GameException("Matches number must be an even number !")
    heap1 = "|"*(matches_number)
    return heap1 



def print_game_matches(heap) -> None:
    """

    Affichage du plateau de jeu
    
    Parameters
    ----------
    heaps : List[str]
        DESCRIPTION. une liste avec les allumettes

    Returns
    -------
    None
    """
    
    print(heap)
        
        
def matchesToRemove():
    
    """
    
    Creation de deux ensembles de nombres aléatoires. 
    Une avec des nombres impaires et une autre avec des nombres paires 
    
    Returns
    -------
    list
    
    une liste contenant l'ensemble de nombre paire et l'ensemble de nombre impaire
        

    """
    
    matchesToRemoveOdd = {1}
    matchesToRemoveEven = {2}
    
    while(len(matchesToRemoveEven)<3 or len(matchesToRemoveOdd)<3) :
        nb = random.randint(3,12)
        
        
        if((nb%2 == 0) and len(matchesToRemoveEven)<3 ) :
            matchesToRemoveEven.add(nb)
            
        if((nb%2 == 1) and len(matchesToRemoveOdd)<3):
            matchesToRemoveOdd.add(nb)
            
     
            
    return [matchesToRemoveEven, matchesToRemoveOdd]





    

        
        
