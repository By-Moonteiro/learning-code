




# Abre arquivo
arquivo = open("text.txt", "w")

# Escreve um texto no arquivo
arquivo.write("testando escrita.")

# Fecha arquivo
arquivo.close()

# Copiando um arquivo em outro arquivo
leitura = open("arq1.txt", "r")
escrita = open("arq2.txt", "w")

texto = leitura.read()
escrita.write(texto)

leitura.close()
escrita.close()

# Copiando e checando erros na abertura dos arquivos
try:
    leitura = open("arq1.txt", "r")
except FileNotFoundError:
    print("Nao consegui abrir o arq1.txt")
else:
    try:
        escrita = open("arq2.txt", "w")
    except:
        print("Nao consegui abrir o arq2.txt")
    else:
        texto = leitura.read()
        escrita.write(texto)
        escrita.close()
        leitura.close()

# Copiando um vetor de numeros para um arquivo, com cada elemento em linhas diferentes
vetor = []
n = int(input("digite o tamanho do vetor: "))
print("digite os elementos do vetor: ")
for i in range(n):
    elemento = int(input())
    vetor.append(elemento)
arquivo.open("vetor1.txt", "w")
arquivo.write(f"\n {n}")
for i in range(n):
    arquivo.write(f"\n {vetor[i]}")
arquivo.close()

# função "open" abre um arquivo recebendo o nome e o caminho, além do modo de abertura do arquivo.
arquivo1 = open("meutexto.txt", "w")
arquivo2 = open("c:/doc/arq.c", "r")

# Abertura de arquivos
objarquivo = open("nome_arquivo, modo")

# COPIANDO UM VETOR DE N INTEIROS, C/ CADA ELEMETO EM LINHAS DIFERENTES COM O WITH:
vetor = []
n = int(input("digite o tamanho do vetor: "))
print("digite os elementos do vetor: ")
for i in range(n):
    elemento = int(input())
    vetor.append(elemento)
with open ("vetor1.txt", "w") as arquivo:
    arquivo.write(f"\n{n}")
    for i in range(n):
        arquivo.write(f"\n{vetor[i]}")

# LEITURA DE UM ARQUIO CONTENDO VETOR DE NUMEROS INTEIROS:
vetor = []
with open("vetor1.txt", "r") as arquivo:
    n = int(arquivo.readline())
    for i in range(n):
        elemento = int(arquivo.readline())
        vetor.append(elemento)
print(f"Foram lidos {n} elementos: ")
for i in range(n):
    print(vetor[i])

# LENDO UM ARQUIVO DO QUAL NAO SE CONHECE PREVIAMENTE O NUMERO DE LINHAS:
    # esta ainda opcao é a melhor
    # o loop for sobre a colecao de linhas
    # permite ler uma linha por vez do arquivo
string = input("Digite o nome do arquivo: ")
with open(string, "r") as arquivo:
    for linha in arquivo:
        print(linha)

"""
# MODOS DE ABERTURA:
-r:  Abre o arquivo somente para leitura. Se o arquivo não existir, 
um erro é gerado.

-w:  Abre o arquivo somente para escrita. SEMPRE cria um novo arquivo. 
Portanto, se o arquivo já existir, ele é apagado.

-a:  Abre o arquivo para leitura/escrita. Escreve apenas no final do
 arquivo (append). Caso o arquivo já exista, ele abre, caso contrário,
 o arquivo é criado.

-r+:  Abre o arquivo para leitura/escrita. Se o arquivo não existir,
 um erro é gerado. Stream posicionado no início do arquivo.

-w+: Abre o arquivo para leitura/escrita. SEMPRE cria um novo
 arquivo. Portanto, se o arquivo já existir ele é apagado.
"""
"""
# COMANDO DE ESCRITA:
objarquivo.write(str) <- Obs.: somente para arquivos abertos em modo de escrita
    -> similar ao print, mas com apenas um parâmetro, que deve ser 
    obrigatoriamente uma string. 
    -> Diferente do print, não insere uma linha no final. Para fazer 
    isto, é preciso adicionar \n ao final da string.

# FECHAMENTO DE UM ARQUIVO:
objarquivo.close()

# COMANDO DE LEITURA:
objarquivo.read() <- Obs.: somente para arquivos abertos em modo de leitura
    -> similar ao input, lê e retorna uma string de todo o texto que 
    está no arquivo.
objarquivo.readline() <- Obs.: somente para arquivos abertos em modo de leitura
    -> similar ao read() acima, com a diferença que lê apenas uma 
    linha do arquivo e retorna esta linha em uma string.

# COMANDO WITH:
O comando with é um comando composto (de bloco) que permite 
simplificar o tratamento de arquivos.
    -> O bloco with é iniciado com a abertura do arquivo
    -> O fechamento do arquivo é feito automaticamente ao 
    encerrar o bloco with
Exemplo: 
# abre arquivo para escrita
with open("test.txt", "w") as arquivo:
    arquivo.write("testando escrita")
"""