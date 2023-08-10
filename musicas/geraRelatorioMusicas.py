import os
from mutagen.mp3 import MP3

#from django.shortcuts import render


def tag_to_string(tags):

    if tags:
        print("Título:", tags.get("TIT2"))
        print("Artista:", tags.get("TPE1"))
        print("Álbum:", tags.get("TALB"))
        print("Ano:", tags.get("TDRC"))
        # E assim por diante para outras tags que você queira ler
    else:
        print("Nenhuma tag encontrada no arquivo.")
    
    #artist = tag.artist if tag.get("TPE1") else "Unknown Artist"
    #title = tag.title if tag.title else "Unknown Title"
    #album = tag.album if tag.album else "Unknown Album"
    #track_number = tag.track_num[0] if tag.track_num else "Unknown Track Number"
    #return f"Cover: {cover} Artist: {artist}, Title: {title}, Album: {album}, Track Number: {track_number}"
    return 'fim'

def gerar():
    file_path = "./MP3/teste.mp3"
    audiofile = MP3(file_path)
    tag_attributes = audiofile.tags
    tag_string = tag_to_string(audiofile.tags)

if(__name__ == "__main__"):
    gerar()