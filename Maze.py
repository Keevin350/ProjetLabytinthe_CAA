# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 22:36:38 2021

@author: Kevin
"""
import random


class Maze:
    """
    Classe Maze
    
    Génère le labyrinthe qui est un tableau à deux dimensions à partir d'un graphe d'adjacence.
    """
    #attributs
    graph = []
    lab = [] #le labyrinthe
    

    def __init__(self,w=3,h=3):
        """
        Constructeur de la classe Maze. Crée un graphe avec des noeuds qui ne sont pas reliés entre eux.
        ATTENTION : La taille et la largeur doivent être égales

        Paramètres
        ----------
        w : int, optional
            Représente la largeur du labyrinthe. La valeur par défaut est 3.
        h : int, optional
            Représente la hauteur du labyrinthe. La valeur par défaut est 3.

        Returns
        -------
        None.
        """
        #attributs
        self.width = w
        self.heigth = h
        
        for i in range(self.heigth):
            self.graph.append([])
            
        for i in range(self.heigth):
            for j in range(self.width):
                self.graph[i].append(i*self.width+j)
        
        for i in range(self.heigth):
            for j in range(self.width):
                print(self.graph[i][j],end='\t')
            print('\n')
    

    def createMaze(self):
        """
        Méthode createMaze()
        
        Méthode qui crée le labyrinthe sous forme de matrice à deux dimensions à partir d'un graphe d'adjacence.
        Les 0 sont des cases vides, les -1 des murs, 1 la case de départ et 2 la case d'arrivée.
        

        Returns
        -------
        None.
        """
        #utilisation algo backtracking pour faire graphe du laby et graphe d'adjacence
        
        #variables
        directions = [[-1,0],[0,1],[1,0],[0,-1]] #liste des directions Nord, Ouest, Sud, Est
        matrice = [] #graphe d'adjacence
        pile = []
        visited = [] #liste des noeuds visités
        
        #initialisation de la matrice d'adjacence
        for i in range(0,self.width*self.heigth):
            matrice.append([])
        
        #initialisation du point de départ pour l'utilisation de l'alogrithme de backtracking
        posX=random.randrange(self.width)
        posY=random.randrange(self.heigth)
        print("la position initiale posX=",posX,"\t posY=",posY)
        
        cell = self.graph[posY][posX]

        pile.append(cell)
        visited.append(cell)
        
        while len(pile) > 0 :
            
            validMoves = []#liste des directions possibles depuis une cellule
            
            #Nord
            if posY-1 >= 0 and self.graph[posY-1][posX] not in visited:
                validMoves.append("N")
            #Est
            if posX+1 < self.width and self.graph[posY][posX+1] not in visited:
                validMoves.append("E")
            #Sud
            if posY+1 < self.heigth and self.graph[posY+1][posX] not in visited:
                validMoves.append("S")
            #Ouest
            if posX-1 >= 0 and self.graph[posY][posX-1] not in visited:
                validMoves.append("O")
        
            
            if len(validMoves) > 0:
                moveChoice = random.choice(validMoves)
        
                print(moveChoice)
                if moveChoice == "N":
                    posY += directions[0][0]
                    
                elif moveChoice == "E":
                    posX += directions[1][1]
                    
                elif moveChoice == "S":
                    posY += directions[2][0]
                    
                elif moveChoice == "O":
                    posX += directions[3][1]
                    
                    
                newCell =  self.graph[posY][posX]
                matrice[newCell].append(cell)
                matrice[cell].append(newCell)
                cell = newCell
                visited.append(cell)
                pile.append(cell)
            
            else:
                cell = pile.pop()
                posX = cell % self.width
                posY = cell // self.heigth 
                
                
            
        print(matrice)
        
        #creation structure laby
        nodes=[]
        for i in range(self.width*self.heigth):
            nodes.append(i)
        
        #mise à jour des variables. Entre chaque noeuds, il y a une cellule vide qui sera -1 ou 0
        #selon le graphe d'adjacence
        self.heigth = self.heigth + self.heigth-1
        self.width = self.width + self.width-1
    
        hauteur = self.heigth
        largeur = self.width
        
        
        for i in range(hauteur):
            self.lab.append([])
        
        #ajout de -1 à toutes les lignes impaires
        for i in range(hauteur):
            if i % 2 != 0:
                for j in range(largeur):
                    self.lab[i].append(-1)
        
        #ajout de -1 ou numero de la cellule pour lignes paires
        for i in range(hauteur):
            if i % 2 == 0:
                for j in range(largeur):
                    if j%2 == 0:
                        self.lab[i].append(nodes.pop(0))
                    else:
                        self.lab[i].append(-1)
            
        """    
        for i in range(self.heigth):
            for j in range(self.width):
                print(self.lab[i][j],end='\t')
            print('\n')
        """
        
        #pour chaque noeud du graphe, on regarde si le noeud à sa droite ou en bas est son voisin
        #en vérifiant à partir du tableau d'adjacence. S'ils son voisin en ajoute -5 entre eux sinon -1
        #-1: murs et -5 futurs cellule 'couloirs'
        for i in range(hauteur):
            for j in range(largeur):
                currentCell = self.lab[i][j]
                if currentCell  > -1:
                    
                    if i < hauteur-1:
                        if self.lab[i+2][j] in matrice[currentCell]:
                            self.lab[i+1][j] = -5
                
                    if j < largeur-1:
                        if self.lab[i][j+2] in matrice[currentCell]:
                            self.lab[i][j+1] = -5
        """                
        for i in range(self.heigth):
            for j in range(self.width):
                print(self.lab[i][j],end='\t')
            print('\n')
        
        print('\n')
       """
       
        #on remplace les valeurs positives par 0
        for i in range(hauteur):
            for j in range(largeur):
                if self.lab[i][j] != -1:
                    self.lab[i][j] = -0
        """ 
        for i in range(self.heigth+self.heigth-1):
            for j in range(self.width + self.width-1):
                print(self.lab[i][j],end='\t')
            print('\n')
        """
        stop = False
        
        #on choisit la cellule de départ qui est la première cellule vide en partant d'en haut à gauche
        for i in range(hauteur):
            for j in range(largeur):
                if self.lab[i][j] == 0:
                    self.lab[i][j] = 1
                    self.start = (i,j)
                    stop = True
                    break
            if stop:
                break
        
        stop = False
        
        #on choisit la cellule d'arrivée qui est la dernière cellule vide en partant d'en bas à droite
        for i in range(hauteur-1,0,-1):
            for j in range(largeur-1,0,-1):
                if self.lab[i][j] == 0:
                    self.lab[i][j] = 2
                    self.end = (i,j)
                    stop = True
                    break
            if stop:
                break
               
        for i in range(hauteur):
            for j in range(largeur):
                print(self.lab[i][j],end='\t')
            print('\n')