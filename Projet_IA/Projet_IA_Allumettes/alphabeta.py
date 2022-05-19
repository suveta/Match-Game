#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:39:53 2022

Ce module regroupe une classe et des fonctions qui permettent le bon fonctionnement de l'élagage
Alpha-Bêta

"""

# Définition de variables ayant des valeurs par défaut.
#Ces valeurs servent à initialiser les évaluations limites de l'élagage alpha-bêta
maxima, minima = 1000, -1000   

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


def alpha_beta(situation:list, maxi:bool, profondeur:int,coups_impaire:set,coups_paire:set, alpha:int, beta:int):
    """
    fonction effectuant l'élagage Alpha-Bêta

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
      ensemble des coups paires possibles.
    alpha : TYPE
        DESCRIPTION. Valeur initiale de coupure alpha
    beta : TYPE
        DESCRIPTION. Valeur initiale de coupure bêta

    Returns
    -------
    TYPE
        DESCRIPTION. Valeur du coup le plus optimal pour gagner par rapport à la profondeur fixée
    TYPE
        DESCRIPTION. Objet(s) <<Coup>> associé à la valeur optimale

    """
    if ((profondeur==0) or (situation[1] <= 0)):
         if situation[1]<0:
             if maxi:
                 situation[1] = 0
             else:
                 situation[1] = -situation[1]
         return evaluer(situation[1], maxi), 0
    if maxi:
         coups = situation[-1]
         val = minima
         solutions = []
         for coup in coups:
             c = Coup(coup)
             
             if situation[0] == "paire":
                 nouvelle_situation = ["impaire", situation[1]-c.getValeur(), coups_impaire]
             else:
                 nouvelle_situation = ["paire", situation[1]-c.getValeur(), coups_paire]
             score, t = alpha_beta(nouvelle_situation, not(maxi), profondeur-1,coups_impaire,coups_paire, alpha, beta)
             
             c.setHeuristic(score)
             val = max(val, score)
             alpha = max(alpha, val)
             solutions.append(c)
             
             if beta<=alpha:
                 break
         return val, solutions
             
    else:
         coups = situation[-1]
         val = maxima
         solutions = []
         for coup in coups:
             c = Coup(coup)
             
             if situation[0] == "paire":
                 nouvelle_situation = ["impaire", situation[1]-c.getValeur(), coups_impaire]
             else:
                 nouvelle_situation = ["paire", situation[1]-c.getValeur(), coups_paire]
             score, t = alpha_beta(nouvelle_situation, not(maxi), profondeur-1,coups_impaire,coups_paire, alpha, beta)
             c.setHeuristic(score)
             val = min(val, score)
             beta = min(beta, val)
             solutions.append(c)
                 
             if beta<=alpha:
                 break
         return val, solutions
     

def maximiser_coup(liste:list, nb_allumettes:int):
    """
    Cette fonction détermine le meilleur coup parmi une pléiade de bons coups possibles

    Parameters
    ----------
    liste : list
        DESCRIPTION. Liste représentant l'ensemble des coups optimaux obtenus par l'élagage Alpha-Bêta
    nb_allumettes : int
        DESCRIPTION. nombre d'allumettes restants à jouer

    Returns
    -------
    TYPE
        DESCRIPTION. Valeur du meilleur coup possible sans possibilité de perdre

    """
    pos, neg = [], []
    for element in liste:
        if nb_allumettes-element.getValeur()>0:
            pos.append(element.getValeur())
        else:
            neg.append(-element.getValeur())
    if len(pos) == 0:
        return abs(max(neg))
    elif len(neg) == 0:
        return max(pos)
    return abs(max(min(pos), max(neg)))
