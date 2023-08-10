import os
#from mutagen.mp3 import MP3
from mutagen import File

def percorrer_diretorio(diretorio):
    # Percorre todos os arquivos e subdiretórios
    for item in os.listdir(diretorio):
        item_path = os.path.join(diretorio, item)

        # Se o item for um diretório, chama recursivamente a função
        if os.path.isdir(item_path):
            percorrer_diretorio(item_path)

        # Se o item for um arquivo, verifica se é um arquivo de música
        elif os.path.isfile(item_path):
            if item_path.lower().endswith(".mp3") or item_path.lower().endswith(".flac"):
                if item_path.lower().endswith(".mp3"):
                    ler_tags_mp3(item_path)
                else:
                    if item_path.lower().endswith(".flac"):
                        ler_tags_flac(item_path)
                        

def ler_tags_mp3(file_path):
    try:
        #audiofile = MP3(file_path)
        audiofile = File(file_path)

        # Obter as tags do arquivo
        tags = audiofile.tags
#
        if tags:
            #linha = print(file_path,"#",tags.get("TIT2"),"#",tags.get("TPE1"),"#",tags.get("TALB"),"#",tags.get("TDRC"),tags.get("TCON")
            #      ,tags.get("TRCK"),tags.get("TCOM"),tags.get("TPE2"),tags.get("TPE3"),tags.get("TPE4"),tags.get("TPOS"),tags.get("TCMP")
            #      ,tags.get("COMM"),tags.get("APIC"),tags.get("USLT"))
            arquivo.write(file_path,"#",tags.get("TIT2"),"#",tags.get("TPE1"),"#",tags.get("TALB"),"#",tags.get("TDRC"),tags.get("TCON")
                  ,tags.get("TRCK"),tags.get("TCOM"),tags.get("TPE2"),tags.get("TPE3"),tags.get("TPE4"),tags.get("TPOS"),tags.get("TCMP")
                  ,tags.get("COMM"),tags.get("APIC"),tags.get("USLT"))


            #linha = print(file_path,"#",tags.get("TIT2"),"#",tags.get("TPE1"),"#",tags.get("TALB"))
            #arquivo.write(str(linha))
            #print("-" * 50)

    except Exception as e:
        arquivo.write("Erro ao ler o arquivo:", str(e))

def ler_tags_flac(file_path):
    try:
        audiofile = File(file_path)

        # Obter as tags do arquivo
        tags = audiofile.tags

        if tags: 
            #           
            #linha = print(file_path,"#",tags.get("title"),"#",tags.get("artist"),"#",tags.get("album"),"#",tags.get("TDRC"),tags.get("genre")
           #      ,tags.get("tracknumber"),tags.get("composer"),tags.get("artist"),tags.get("conductor"),tags.get("translator"),tags.get("compilation"),tags.get("comments")
           #      ,tags.get("comment"),tags.get("covr"))
            arquivo.write(file_path,"#",tags.get("title"),"#",tags.get("artist"),"#",tags.get("album"),"#",tags.get("TDRC"),tags.get("genre")
                 ,tags.get("tracknumber"),tags.get("composer"),tags.get("artist"),tags.get("conductor"),tags.get("translator"),tags.get("compilation"),tags.get("comments")
                 ,tags.get("comment"),tags.get("covr"))


            #linha = print(file_path,"#",tags.get("title"))

            #arquivo.write(linha)
            #print("-" * 50)

    except Exception as e:
        arquivo.write("Erro ao ler o arquivo:", str(e))        

# Exemplo de uso da função recursiva
nome_arquivo = "arquivo_de_musicas.txt"

with open(nome_arquivo, 'w') as arquivo:
    caminho_diretorio = './MP3/'
#caminho_diretorio = '\\\\MAC01065383\\_Collection'
    print("Caminho#Título da música#Artista#Álbum#Ano de lançamento (data de gravação)#Gênero#Número da faixa#Compositor#Artista do álbum (Band/Orchestra/Acompanhamento)#Condutor/Intérprete/Solista do álbum#Tradutor, intérprete adaptador ou editor do álbum#Número do disco (para álbuns de várias discos)#Indicador de compilação (0 = não é uma compilação, 1 = é uma compilação)#ComentáriosCapa do álbum (imagem)#Letras da música")
    #arquivo.write("Caminho#Título da música#Artista#Álbum#Ano de lançamento (data de gravação)#Gênero#Número da faixa#Compositor#Artista do álbum (Band/Orchestra/Acompanhamento)#Condutor/Intérprete/Solista do álbum#Tradutor, intérprete adaptador ou editor do álbum#Número do disco (para álbuns de várias discos)#Indicador de compilação (0 = não é uma compilação, 1 = é uma compilação)#ComentáriosCapa do álbum (imagem)#Letras da música") 
    #arquivo.write("Caminho#Título da música#Artista#Álbum") 
    percorrer_diretorio(caminho_diretorio)
