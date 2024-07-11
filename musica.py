import pygame

class musica():

    def __init__(self, artista, nome, estilo, duracao, file, album_capa):

        self.artista = artista
        self.nome = nome
        self.estilo = estilo
        self.duracao = duracao
        self.file = file
        self.album_capa = album_capa

    def mostrar(selfie):

        print(f'''Artista: {selfie.artista}.
Nome: {selfie.nome}.
Estilo: {selfie.estilo}.
duração: {selfie.duracao}.''')

m1 = musica("Maneskin", "Beggin", "Rock", 149, 'Trabalho/rep_musicas/Beggin.mp3', "Trabalho/Images/Beggin.png")
m2 = musica("Natanzinho", "Anjo Azul", "Sertanejo", 143, "Trabalho/rep_musicas/anjo.mp3", "Trabalho/Images/anjo.png" )
m3 = musica("Marila Medonça","Troco de calçada", "Sertanejo", 154, "Trabalho/rep_musicas/mm.mp3", "Trabalho/Images/MM.png")
m4 = musica("Link Park", "In The End", "Eletrônica", 167, "Trabalho/rep_musicas/link_park.mp3", "Trabalho/Images/link.png")
m5 = musica("Ikimono-gakari", "Blue Bird", "Anime", 250, "Trabalho/rep_musicas/Blue Bird.mp3", "Trabalho/Images/bluebird.png")
m6 = musica("Delacruz", "Sunshine", "Hip Hop", 230, "Trabalho/rep_musicas/delacruz.mp3", "Trabalho/Images/sunshine.png")

lista_musicas = [m1, m2, m3, m4, m5, m6]

musicas = lista_musicas