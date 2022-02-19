
def escrever_arquivo(texto):
    diretorio = C:/Projetos/app_python/teste.txt
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('texte.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha. \n')
    atualizar_arquivo('Terceira linha. \n')