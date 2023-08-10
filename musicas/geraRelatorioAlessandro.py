import os
from mutagen.mp3 import MP3
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
                    ler_tags_flac(item_path)    

def ler_tags_mp3(file_path):
    linha=""
    try:
        audiofile = MP3(file_path)
        if audiofile is not None:
            # Verificar as tags e metadados disponíveis no arquivo
            if audiofile.tags:
                
                for tag, valor in audiofile.tags.items():

                    if valor is not None:

                        # Garantir que o valor seja uma string antes de imprimi-lo
                        if tag.lower() == 'tit2' or tag.lower() == 'tpe1' or tag.lower() == 'talb':
                            #valor_str = str(valor)
                            linha += "{};{};{}".format(file_path.replace(caminho_diretorio, ".\\"),tag,valor)

                        # Se você quiser gravar os metadados em um arquivo, descomente as linhas abaixo:
                        # with open("metadados_audio.txt", "a") as arquivo_saida:
                        #     arquivo_saida.write(f"{tag}: {valor_str}\n")
                    else:
                        linha = "O arquivo não possui tags ou metadados."
                arquivo.write(f"{linha}\n")          
            else:
                arquivo.write("O arquivo não é um arquivo de áudio válido.")
    except Exception as e:
        arquivo.write(f"Erro ao abrir o arquivo: {e}")
        
def ler_tags_flac(file_path):
    linha = ""
    try:
        audiofile = File(file_path)
        if audiofile is not None:
            # Verificar as tags e metadados disponíveis no arquivo
            if audiofile.tags:
                
                for tag, valor in audiofile.tags.items():

                    if valor is not None:

                        # Garantir que o valor seja uma string antes de imprimi-lo
                        if tag.lower() == 'title' or tag.lower() == 'artist' or tag.lower() == 'album':
                            linha += "{};{};{}".format(file_path.replace(caminho_diretorio, ".\\"),tag,valor)

                        # Se você quiser gravar os metadados em um arquivo, descomente as linhas abaixo:
                        # with open("metadados_audio.txt", "a") as arquivo_saida:
                        #     arquivo_saida.write(f"{tag}: {valor_str}\n")
                    else:
                        linha = "O arquivo não possui tags ou metadados."
                arquivo.write(f"{linha}\n")        
            else:
                arquivo.write("O arquivo não é um arquivo de áudio válido.")
    except Exception as e:
        arquivo.write(f"Erro ao abrir o arquivo: {e}")



# Exemplo de uso da função recursiva

nome_arquivo = "arquivo_de_musicas_Alessandro.txt"
caminho_diretorio = './MP3/'
with open(nome_arquivo, 'w') as arquivo:
    #caminho_diretorio = '\\\\MAC01065383\\_Collection'
    #print("Caminho#Título da música#Artista#Álbum#Ano de lançamento (data de gravação)#Gênero#Número da faixa#Compositor#Artista do álbum (Band/Orchestra/Acompanhamento)#Condutor/Intérprete/Solista do álbum#Tradutor, intérprete adaptador ou editor do álbum#Número do disco (para álbuns de várias discos)#Indicador de compilação (0 = não é uma compilação, 1 = é uma compilação)#ComentáriosCapa do álbum (imagem)#Letras da música")
    #arquivo.write("Caminho#Título da música#Artista#Álbum#Ano de lançamento (data de gravação)#Gênero#Número da faixa#Compositor#Artista do álbum (Band/Orchestra/Acompanhamento)#Condutor/Intérprete/Solista do álbum#Tradutor, intérprete adaptador ou editor do álbum#Número do disco (para álbuns de várias discos)#Indicador de compilação (0 = não é uma compilação, 1 = é uma compilação)#ComentáriosCapa do álbum (imagem)#Letras da música") 
    #arquivo.write("Caminho#Título da música#Artista#Álbum") 
    linha = "CAMINHO;TITULO;ARTISTA;ALBUM"
    arquivo.write(f"{linha}\n")      
    percorrer_diretorio(caminho_diretorio)
