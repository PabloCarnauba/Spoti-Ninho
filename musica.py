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

m1 = musica("Maneskin", "Beggin", "Rock", 149, 'Spoti-Ninho/rep_musicas/Beggin.mp3', "Spoti-Ninho/Images/Beggin.png")
m2 = musica("Natanzinho", "Anjo Azul", "Sertanejo", 143, "Spoti-Ninho/rep_musicas/anjo.mp3", "Spoti-Ninho/Images/anjo.png" )
m3 = musica("Marila Medonça","Troco de calçada", "Sertanejo", 154, "Spoti-Ninho/rep_musicas/mm.mp3", "Spoti-Ninho/Images/MM.png")
m4 = musica("Link Park", "In The End", "Eletrônica", 167, "Spoti-Ninho/rep_musicas/link_park.mp3", "Spoti-Ninho/Images/link.png")
m5 = musica("Ikimono-gakari", "Blue Bird", "Anime", 250, "Spoti-Ninho/rep_musicas/Blue Bird.mp3", "Spoti-Ninho/Images/bluebird.png")
m6 = musica("Delacruz", "Sunshine", "Hip Hop", 230, "Spoti-Ninho/rep_musicas/delacruz.mp3", "Spoti-Ninho/Images/sunshine.png")

lista_musicas = [m1, m2, m3, m4, m5, m6]

musicas = lista_musicas