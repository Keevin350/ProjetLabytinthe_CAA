# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 22:39:35 2022

@author: Kevin
"""
import pygame
import os
from pygame.locals import *
from Maze import Maze
from Fenetre import Fenetre
import datetime


if __name__ == '__main__':
    
    pygame.init()#initialisation python
    
    x = 100
    y = 35
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    
    
    screen = pygame.display.set_mode((500,500))#initialisation taille écran
    pygame.display.set_caption('Le jeu du labyrinthe')#initialisation nom de la fenêtre
    
    #texte à afficher
    police = pygame.font.Font(None, 25)
    txt1 = police.render("1 - Niveau facile", 1,(255,255,255))
    txt2 = police.render("2 - Niveau moyen", 1, (255,255,255))
    txt5 = police.render("3 - Niveau difficile", 1, (255,255,255))
    txt3 = police.render("Perdu !", 1, (255,0,0))
    txt4 = police.render("Gagné !", 1, (0,255,0))
    
    screen.blit(txt1, (180,125))
    screen.blit(txt2, (180,250))
    screen.blit(txt5, (180,375))
    pygame.display.flip()
    
    #variables
    continuer = True
    start = False
    accueil = True
    findEnd = False
    playing = True
    while continuer:
        
        #fenetre de menu
        while accueil:
            for event in pygame.event.get():
                if event.type == QUIT:#ferme la fenêtre
                    accueil = False
                    continuer = False
                    start = True
                    playing = False
                
                elif event.type == pygame.KEYDOWN:
                    #niveau facile
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        screen.fill((0,0,0))
                        m = Maze(5,5)
                        m.createMaze()
                    #niveau moyen
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        screen.fill((0,0,0))
                        m = Maze(10,10)
                        m.createMaze()
                    #niveau difficile   
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        screen.fill((0,0,0))
                        m = Maze(13,13)
                        m.createMaze()
                    
                    f = Fenetre(m,screen)
                    accueil = False
        
        windowW, windowH = pygame.display.get_surface().get_size()
        
        #phase de clique sur case de départ
        while start == False:
            for event in pygame.event.get():#ferme la fenêtre
                if event.type == QUIT:
                    start = True
                    continuer = False
                    playing = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #passe à la phase de jeu
                    mousePos = pygame.mouse.get_pos()
                    posX = mousePos[0]//f.size
                    posY = mousePos[1]//f.size
                    
                    if m.lab[posY][posX] == 1:
                        print("ca commence")
                        startTime = datetime.datetime.now().replace(microsecond=0)
                        start = True
                        continuer = False
        
        #phase de jeu
        while findEnd==False and playing:
            for event in pygame.event.get():
                
                #postion du curseur
                mousePos = pygame.mouse.get_pos()
                posX = mousePos[0]//30
                posY = mousePos[1]//30
                
                if event.type == QUIT:#ferme la fenêtre
                    playing = False
                    continuer = False
                
                #si curseur touche mur ou sort de l'écran c'est perdu
                elif m.lab[posY][posX] == -1 or pygame.mouse.get_focused()==0:
                    screen.fill((0,0,0))
                    screen.blit(txt3, (windowW/2.5,windowH/2))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    playing = False
                    continuer = False
                
                #si curseur sur case d'arrivée c'est gagné
                elif m.lab[posY][posX] == 2:
                    endTime = datetime.datetime.now().replace(microsecond=0)
                    duration = endTime - startTime
                    duration = str(duration)
                    txt6 = police.render("Temps : "+duration,1,(255, 255, 255))
                    
                    screen.fill((0,0,0))
                    screen.blit(txt4, (windowW/2.5,windowH/2))
                    screen.blit(txt6, (windowW/3.25,windowH/1.5))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    playing = False
                    continuer = False
                
    pygame.quit()