import PySimpleGUI as sg
import os
import pygame
import player
import musica

sg.theme('Reddit')

song_title_column = [
    [sg.Text(text='Pressione play...', justification='center', background_color='black', text_color='white', size=(200, 0), font='Tahoma', key='song_name')]
]

player_info = [
    [sg.Text('SPOTI-NINHO', background_color='black', text_color='white', font=('Tahoma', 7))]
]

currently_playing = [
    [sg.Text(background_color='black', size=(200, 0), text_color='white', font=('Tahoma', 10), key='currently_playing')]
]

GO_BACK_IMAGE_PATH = 'Trabalho/Images/back.png'
GO_FORWARD_IMAGE_PATH = 'Trabalho/Images/next.png'
PLAY_SONG_IMAGE_PATH = 'Trabalho/Images/play_button.png'
PAUSE_SONG_IMAGE_PATH = 'Trabalho/Images/pause.png'
DEFAULT_ALBUM_COVER_IMAGE_PATH = 'Trabalho/Images/pilot.png'

main = [
    [sg.Canvas(background_color='black', size=(480, 20), pad=None)],
    [sg.Column(layout=player_info, justification='c', element_justification='c', background_color='black')],
    [
        sg.Canvas(background_color='black', size=(40, 350), pad=None),
        sg.Image(filename=DEFAULT_ALBUM_COVER_IMAGE_PATH, size=(350, 350), pad=None, key='album_cover'),
        sg.Canvas(background_color='black', size=(40, 350), pad=None)
    ],
    [sg.Canvas(background_color='black', size=(480, 10), pad=None)],
    [sg.Column(song_title_column, background_color='black', justification='c', element_justification='c')],
    [sg.Text('_'*80, background_color='black', text_color='white')],
    [
        sg.Canvas(background_color='black', size=(99, 200), pad=(0, 0)),
        sg.Image(pad=(10, 0), filename=GO_BACK_IMAGE_PATH, enable_events=True, size=(35, 44), key='previous', background_color='black'),
        sg.Image(filename=PLAY_SONG_IMAGE_PATH, size=(64, 64), pad=(10, 0), enable_events=True, key='play', background_color='black'),
        sg.Image(filename=PAUSE_SONG_IMAGE_PATH, size=(58, 58), pad=(10, 0), enable_events=True, key='pause', background_color='black'),
        sg.Image(filename=GO_FORWARD_IMAGE_PATH, enable_events=True, size=(35, 44), pad=(10, 0), key='next', background_color='black'),
    ],
    [sg.Column(layout=currently_playing, justification='c', element_justification='c', background_color='black', pad=None)]
]

window = sg.Window('Spoti-Ninho', layout=main, size=(480, 730), background_color='black', finalize=True, grab_anywhere=True, resizable=False)

def update_song_display(window, musica):
    
    window['song_name'].update(musica.nome)
    
    window['currently_playing'].update(f'Tocando: {musica.nome} - {musica.artista}')
    
    album_cover_path = musica.album_capa if hasattr(musica, 'album_capa') and os.path.exists(musica.album_capa) else DEFAULT_ALBUM_COVER_IMAGE_PATH
    
    window['album_cover'].update(filename=album_cover_path)

posic = 0

musica_pausada = False

Iniciar = None

def Play_music(posic_atual):
    
    global Iniciar, musica_pausada
    
    music = musica.musicas[posic_atual]
    
    if Iniciar:
        
        Iniciar.parar()
        
    Iniciar = player.Player(music)
    
    Iniciar.start()
    
    musica_pausada = False
    
    update_song_display(window, music)

while True:
    
    event, values = window.read(timeout=100)
    
    if event == sg.WIN_CLOSED:
        
        break
    
    elif event == 'play':
        
        Play_music(posic)
    
    elif event == 'pause':
        
        if not musica_pausada:
            
            Iniciar.pausar()
            
            musica_pausada = True
            
        else:
            
            Iniciar.despausar()
            
            musica_pausada = False

    elif event == 'next':
        
        posic = (posic + 1) % len(musica.musicas)
        
        Play_music(posic)

    elif event == 'previous':
        
        posic = (posic - 1) % len(musica.musicas)
        
        Play_music(posic)

    if Iniciar and not musica_pausada and not pygame.mixer.music.get_busy():
        
        posic = (posic + 1) % len(musica.musicas)
        
        Play_music(posic)
        
window.close()

pygame.quit()
