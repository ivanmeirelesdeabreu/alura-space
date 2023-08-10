#import eyed3
from mutagen.mp3 import MP3

#from django.shortcuts import render
from django.http import HttpResponse

def tag_to_string(tag):
    
    #cover = tag.AlbumCover if tag.AlbumCover else "não"
    artist = tag.artist if tag.artist else "Unknown Artist"
    title = tag.title if tag.title else "Unknown Title"
    album = tag.album if tag.album else "Unknown Album"
    track_number = tag.track_num[0] if tag.track_num else "Unknown Track Number"

    #return f"Cover: {cover} Artist: {artist}, Title: {title}, Album: {album}, Track Number: {track_number}"
    #print(dir(tag)))
    for attribute in dir(tag):
        print(str(attribute))
    return attribute



def index(request):
    file_path = "./musicas/MP3/teste.mp3"
    #audiofile = eyed3.load(file_path)
    audiofile = MP3(file_path)
    tag_attributes = audiofile.tags
    print(tag_attributes)

    tag_string = tag_to_string(audiofile.tag)
    #tags = audiofile.tag
    if audiofile is not None:
        # Obtenha as tags do arquivo
        tags = audiofile.tag

        # Exemplo de leitura das tags existentes
        #print("Título: ", tags.title)
        #print("Artista: ", tags.artist)
        #print("Álbum: ", tags.album)
        #print("Ano: ", tags.year)
    else:
        print("O arquivo não foi carregado corretamente.")

    musicas_array =  []

    #for attribute in tag_attributes:
        #musicas_array.append(f"{attribute}")
        #musicas_array.append(f"{tag}: {audiofile.tag.frame_set[tag]}")

    #tags_string = "\n".join(tags)
    return HttpResponse(tag_string)
#    return render(request, 'galeria/index.html')

#def imagem(request):
#    return render(request, 'galeria/imagem.html')
