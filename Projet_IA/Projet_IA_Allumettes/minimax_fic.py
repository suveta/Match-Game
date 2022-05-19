
# -*- coding: utf-8 -*-
"""
Created on fri Apr  15 17:35:28 2022

@author: ANANDARAJ Suvéta
@author: ADOTRI Frimpong

Ce module regroupe une classe et une fonction qui permettent le bon fonctionnement de l'algorithme
Minimax

"""

from dataclasses import dataclass
from typing import Callable

 
@dataclass            
class Coup :
    __valeur:int
    __heuristic:int = 0
         
    def getValeur(self) -> int:
        """
        Fonction de récupération de la valeur du coup joué 

        Returns
        -------
        int
            DESCRIPTION. Valeur du coup joué par l'utilisateur

        """
        return self.__valeur
    
    def getHeuristic(self) -> int:
        """
        Fonction de récupération de l'heuristique du coup joué 

        Returns
        -------
        int
            DESCRIPTION. Valeur de l'heuristique (évaluation) du coup de l'utilisateur

        """
        return self.__heuristic
    
    def setValeur(self, nouvelle_valeur:int) -> None:
        """
        Fonction d'affectation de la valeur du coup joué 

        Parameters
        ----------
        nouvelle_valeur : int
            DESCRIPTION. Nouvelle valeur du coup de l'utilisateur

        Returns
        -------
        None
            DESCRIPTION.

        """
        self.__valeur = nouvelle_valeur
        
    def setHeuristic(self, valeur_heuristic:int) -> None:
        """
        Fonction d'affectation de l'heuristique du coup joué 

        Parameters
        ----------
        valeur_heuristic : int
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION. Nouvelle valeur de l'heuristique (évaluation) du coup de l'utilisateur

        """
        self.__heuristic = valeur_heuristic
        
    def __repr__(self):
        """
        Fonction de représentation d'un objet de class << Coup >>

        Returns
        -------
        str
            DESCRIPTION. Objet de classe << Coup >> sous forme de chaîne de caractères

        """
        return f"(v={self.getValeur()}, h={self.getHeuristic()})"
        
      
        
evaluer: Callable[[int, bool], int] = lambda valeur, maxi: valeur if maxi else -valeur                


def minmax(situation:list, maxi:bool, profondeur:int, coups_impaire:set, coups_paire:set ) -> int:
    """
      fonction effectuant l'algorithme minimax

    Parameters
    ----------
    situation : list
        liste contenant les informations du jeu actuel
    maxi : boolean
        << true >> si le joueur qui joue est max, << false >> sinon
    profondeur : int
        indique la profondeur de l'arbre de recherche
    coups_impaire : set
       ensemble des coups impaires possibles
    coups_paire : set
        ensemble des coups paires possibles

    Returns
    -------
    int
        DESCRIPTION. Valeur du coup le plus optimal pour gagner par rapport à la profondeur fixée

    """
    if ((profondeur==0) or (situation[1] <= 0)):
        if situation[1]<0:
            if maxi:
                situation[1] = 0
            else:
                situation[1] = -situation[1]
        return evaluer(situation[1], maxi)
    else:
        coups = situation[-1]
        solutions = []
        for coup in coups:
            c = Coup(coup)
            if situation[0] == "paire" :
                nouvelle_situation = ["impaire", situation[1]-c.getValeur(), coups_impaire]
            else:
                nouvelle_situation = ["paire", situation[1]-c.getValeur(), coups_paire]
            score = minmax(nouvelle_situation, not(maxi), profondeur-1,coups_impaire,coups_paire)
            c.setHeuristic(score)
            solutions.append(c)
            
        
            
        if maxi:
            
            maximum = solutions[0]
            for i in range (1,len(solutions)):
                if solutions[i].getHeuristic() >= maximum.getHeuristic() :
                    maximum = solutions[i]
            
            return maximum.getValeur()
        else:
          
            minimum = solutions[0]
            for i in range (1,len(solutions)) :
                if solutions[i].getHeuristic() <= minimum.getHeuristic() :
                    minimum = solutions[i]
            
            return minimum.getValeur()
    

