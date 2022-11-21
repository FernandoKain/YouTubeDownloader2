# pip install pytube
from pytube import YouTube, Playlist
from time import sleep
import os

def pasta_download():
    caminho = f"{os.getenv('USERPROFILE')}\\Downloads"
    print(caminho)

    return caminho

caminho = pasta_download()

def download_unico():
    link = input("Coloque o link do YouTube: ")
    yt = YouTube(link)
    sleep(2)
    tipo = input("Você quer vídeo ou áudio? V ou A: ").lower()
    if tipo == 'v':
        stream = yt.streams.get_by_itag(22)
        print('Fazendo o download!')
        sleep(2)
        stream.download(caminho)
        print('Download concluído!')
        sleep(2)
    else:
        stream = yt.streams.get_by_itag(140)
        print('Fazendo o download!')
        sleep(2)
        stream.download(caminho)
        print('Download concluído!')
        sleep(2)

def download_playlist():
    playlist = input('Coloque o link da playlist: ')
    sleep(3)
    pl = Playlist(playlist)
    for video in pl.videos:
        print(f'Baixando: "{video.title}"')
        video.streams.get_by_itag(140).download()

print("Bem vindo ao programa!")
print("Este programa foi desenvolvido para baixar Vídeos, Músicas ou Playlists inteiras do YouTube.")
print(f'Seus downloads ficarão salvos em {caminho}')

contador = 0

while contador == 0:
    escolha = input('Você quer baixar um Vídeo ou uma Playlist?: V ou P').lower()

    if escolha == 'v':
        download_unico()
    elif escolha == 'p':
        download_playlist()
    contador += 1







