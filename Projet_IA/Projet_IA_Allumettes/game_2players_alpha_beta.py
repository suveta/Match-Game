#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:36:51 2022

@author: ANANDARAJ Suvéta
@author: ADOTRI Frimpong

Ce module contient la fonction qui fait tourner le jeu à deux joueurs


"""



import matches_generator as mg
import alphabeta as alph
from up.mi.fa.sa.exceptions.gameException import GameException

def game2player_alpha_beta() -> None :
    
    """
    Fonction déroulant le jeu à deux joueurs contre une IA en utilisant l'algorithme Minimax
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    
    """
    try:
        print("-----------BIENVENUE AU JEU D'ALLUMETTES-----------")
        
        print("30 allumettes\n100 allumettes\n220 allumettes")
        
        
        nb_matches = int(input("Avec combien d allumettes voulez vous jouez ?"))
        
        if (nb_matches!= 30 and  nb_matches!= 100 and nb_matches!= 220):
           raise GameException("Le niveau demandé n'existe pas")
        
        print("-----------COMMENÇONS LE JEU------------")
        
        #Creation of game's grid
        grid = mg.game_matches(nb_matches)
        mg.print_game_matches(grid)
        
        
        #Creation of lists of numbers to remove
        removeChoice = mg.matchesToRemove()
        evenList = removeChoice[0]
        oddList = removeChoice[1]
        
        #Choix du niveau de difficulté
        print("\n Niveau facile : F\n Niveau intermédiaire :I\n Niveau Difficile :D")
        playerChoice = input("Quel est la difficulté du jeu souhaitée ?")
        
        if playerChoice == 'F' :
            dept = 3
        elif playerChoice == 'I' :
            dept = 9
        else :
            dept = 13
        print(f"Voici vos choix de nombre d'allumettes à retirer :\n liste paire : {evenList} \n liste impaire : {oddList}")
        
        players = ['player1','player2'] 
        
        playDecision = int(input("Joueur 1, voulez vous commencer le jeu en retirant un nombre paire (1) ou un nombre impaire(2) : "))
        
        if playDecision == 1:
            liste1, liste2 =  ['paire', 'impaire'], ['impaire', 'paire']
        else :
            liste1, liste2 = ['impaire', 'paire'], ['paire', 'impaire']
        while(len(grid) != 0 ) :
            for  player in players :
                print(player)
                
                if (player == "player1"):
                    if (liste1[0] == 'paire'):
                       playerChoice = int(input(f"Choississez le nombre d'allumettes que vous voulez elenver dans {evenList} {player} : "))
                       if not(playerChoice in evenList):
                           raise GameException("Vous avez choisi qui n'existe pas dans la liste") 
                       liste1 = ['impaire', 'paire']
                       grid = grid[playerChoice : len(grid)]
                       mg.print_game_matches(grid) 
                       print(f"\n le nombre d'allumettes en jeu : {len(grid)}")
                    elif(liste1[0] == 'impaire'):
                        playerChoice = int(input(f"Choississez le nombre d'allumettes que vous voulez elenver dans {oddList} {player} : "))
                        if not(playerChoice in oddList):
                            raise GameException("Vous avez choisi qui n'existe pas dans la liste") 
                        liste1 = ['paire', 'impaire']
                        grid = grid[playerChoice : len(grid)]
                        mg.print_game_matches(grid)
                        print(f"\n le nombre d'allumettes en jeu : {len(grid)}")
                elif(player == "player2"):
                    if (liste2[0] == 'paire'):
                       situation_paire = ["paire", len(grid), evenList]
                       playerChoice = alph.maximiser_coup(alph.alpha_beta(situation_paire, True, dept, oddList,evenList, -len(grid), len(grid))[-1], len(grid))
                       print(f"joueur 2 a choisi :{playerChoice}")
                       if not(playerChoice in evenList):
                           raise GameException("Vous avez choisi qui n'existe pas dans la liste") 
                       liste2 = ['impaire', 'paire']
                       grid = grid[playerChoice : len(grid)]
                       mg.print_game_matches(grid)
                       print(f"\n le nombre d'allumettes en jeu : {len(grid)}")
                    elif(liste2[0] == 'impaire'):
                        situation_impaire = ["impaire", len(grid), oddList]
                        playerChoice = alph.maximiser_coup(alph.alpha_beta(situation_impaire, True, dept, oddList,evenList, -len(grid), len(grid))[-1], len(grid))
                        print(f"joueur 2 a choisi :{playerChoice}")
                        if not(playerChoice in oddList) :
                            raise GameException("Vous avez choisi qui n'existe pas dans la liste") 
                        liste2 = ['paire', 'impaire']
                        grid = grid[playerChoice : len(grid)]
                        mg.print_game_matches(grid) 
                        print(f"\n le nombre d'allumettes en jeu : {len(grid)}")
                        
                if(len(grid) == 0) :
                    print(f"{player} a perdu !!!!!\n")
                    if player == 'player1' :
                        print("L'ordinateur a gagné ")
                    else :
                        print("Vous avez gagné contre l'ordinateur !!!!!!")
                    break
    except GameException as ge:
        print(ge.toString())    
            
            


game2player_alpha_beta()
    
    
