# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 23:35:31 2022

@author: Kevin
"""
import pygame
from Maze import Maze

class Fenetre:
    """
    Classe Fenêtre
    
    S'occupe de l'affiche du labyrinthe à l'écran
    """
    
    def __init__(self, Maze, screen, s=30):
        """
        Le constructeur de la classe. Affiche des carrée d'une certaine couleur en fonction de la cellule
        du labyrinthe qui lui est associée

        Paramètres
        ----------
        Maze : Maze
            Objet de la classe Maze.
        screen : Fenetre
            Objet de la classe Fenetre.

        Returns
        -------
        None.

        """
        screen = pygame.display.set_mode((s*Maze.width,s*Maze.heigth))#mise à jour des dimensions de l'écran
        self.size = s
        
        #ajout des cases à l'écran
        for line in range(Maze.heigth):
            for column in range(Maze.width):
                if Maze.lab[line][column] == 1:#case de départ
                    pygame.draw.rect(screen, (51, 235, 255), (self.size * column, self.size * line, self.size, self.size), 0)
                
                elif Maze.lab[line][column] == 2:#case d'arrivée
                    pygame.draw.rect(screen, (161, 24, 243), (self.size * column, self.size * line, self.size, self.size), 0)
                
                elif Maze.lab[line][column] == -1:#case mur
                    pygame.draw.rect(screen, (0, 0, 0), (self.size * column, self.size * line, self.size, self.size), 0)
                    
                elif Maze.lab[line][column] == 0:#case vide
                    pygame.draw.rect(screen, (163, 196, 199), (self.size * column, self.size * line, self.size, self.size), 0)
        pygame.display.flip()
        
        