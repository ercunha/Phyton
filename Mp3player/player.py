#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
# Iniciando a biblioteca
pygame.init()
#
pygame.mixer.music.load('genoma.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()