# class Rotulo:
# '''O Modulo __init__  permite contruir objetos de uma classe.'''

#     def __init__(self):
#      ''' - self significa o proprio objeto de uma classe;  
#          - O que e referenciado com "self" dentro da classe e chamado de "atributo" 
#          (ou "membro") da classe;  

#          '''
#         self.variavel1 = valor_default1
#         self.variavel2 = valor_default2
#         ...
#         self.variaveln = valor_defaultn


# A definicao de uma classe capaz de armazenar as info de um fucionario ficaria assim:
# class Funcionario:
#     '''~ Armazena informacoes do funcionario.'''
#     def __init__(self):
#         self.nome = ""
#         self.matricula = 0
#         self.salario = 0.0


# f1 = Funcionario() # <- Objeto
#  vvv Exemplo Generico:
# f1.nome = "Wagner"
# f1.matricula = 25111000
# f1.salario = 1518.00
# print(f1.nome)
# print(f1.matricula)
# print(f1.salario)

# Programa Principal
# f1 = Funcionario()
# print("Entre com os dados do funcionario...")
# f1.nome = input("Digite o nome: ")
# f1.salario = float(input("Digite o salario: "))
# f1.matricula = int(input("Digite a matricula: "))
# print("Os dados lidos foram: ")
# print(f"Nome: {f1.nome}")
# print(f"Numero da matricula: {f1.matricula}")
# print(f"Salario: {f1.salario}")


# Estrutura de dados dentro de uma classe:
# class Funcionario:
#     '''~ Armazena informacoes do funcionario.'''
#     def __init__(self):
#         self.nome = ""
#         self.matricula = 0
#         self.salario = 0.0
#         self.horasExtras = {} # <- Dicionario

# Inserir 10 horas no Quinto dia do mes:
# f = Funcionario()
# f.horasExtras[5] = 10


# Metodos de uma classe:
# class Funcionario:
#     def __init__(self):
#         self.nome = ""
#         self.matricula = 0
#         self.salario = 0.0
#         self.anoNascimento = 0 # <-
    # Como fazer para encontrar a idade do funcionario?

# Calculando a idade de um funcionario:
# from datetime import date


# class Funcionario:
#     def __init__(self):
#         self.nome = ""
#         self.matricula = 0
#         self.salario = 0.0
#         self.anoNascimento = 0
#     def idade(self):
        # anoAtual = date.today().year
        # idade = anoAtual - self.anoNascimento
        # return idade
    
# Programa Principal
# f1 = Funcionario()
# print("Entre com os dados do funcionario...")
# f1.nome = input("Digite o nome: ")
# f1.salario = float(input("Digite o salario: "))
# f1.matricula = int(input("Digite a matricula: "))
# f1.anoNascimento = int(input("Digite ano de nascimento: "))
# print(f"A idade do funcionario é: {f1.idade()}")


# Classes dentro de Classe:

# class Ponto:
#     def __init__(self):
#         self.x = 0.0
#         self.y = 0.0

# class Reta:
#     def __init__(self):
#         self.p1 = Ponto()
#         self.p2 = Ponto()

# Programa Principal
# r = Reta()

# r.p1.x = 100.0
# r.p2.y = 200.5
# r.p2.x = float(input("Digite a abscissa do ponto: "))
# r.p2.y = float(input("Digite a ordenada do ponto: "))

# print(f"P1 = {r.p1.x}, {r.p1.y}")
# print(f"P2 = {r.p2.x}, {r.p2.y}")


# Objetos podem ser passados como parâmetros de uma função.
# class Funcionario:
#     def __init__(self):
#         self.nome = ''
#         self.matricula = 0
#         self.salario = 0.0

# def leFuncionario(f):
#     print("Entre com os dados do funcionário...")
#     f.nome = input("Digite o nome: ")
#     f.salario = float(input("Digite o salário: "))
#     f.matricula = int(input("Digite a matrícula: "))

# programa principal
# func = Funcionario()
# leFuncionario(func)
# print("Os dados lidos foram:")
# print(f"Nome: {func.nome}")
# print(f"Salario:{func.salario}")
# print(f"Matricula: {func.matricula}")


# Lista de Objetos:

# funcionarios = [] # <- Lista de Funcionarios
# funcionarios.append(Funcionario())

    # Para acessar:
# funcionarios[0].nome = "Monteiro"
# funcionarios[0].salario = 2500.32
# funcionarios[0].matricula = 123


# Podemos criar o objeto completo primeiro:

# f = Funcionario()
# f.nome = "Monteiro"
# f.salario = 1700.00
# f.matricula = 456
# funcionarios.append(f)


# Programa para receber os dados de 50 funcionarios e, em seguida, lista-los:
# class Funcionario:
#     def __init__(self):
#         self.nome = ""
#         self.matricula = 0
#         self.salario = 0.0

# Programa Principal
# funcionarios = [] # <- Lista
# for i in range(50):
#     print(f"Entre com os dados do funcionario: {i + 1}")
#     f = Funcionario()
#     f.nome = input("Digite o nome: ")
#     f.salario = float(input("Digite o salário: "))
#     f.matricula = int(input("Digite a matrícula: "))
#     funcionarios.append(f)

# print("\n\nOs dados lidos foram:\n")
# for funcionario in funcionarios:
#     print("Proximo Funcionario: ")
#     print(f"nome: {funcionarios.nome}")
#     print(f"Matricula: {funcionarios.matricula}")
#     print(f"Salario: {funcionarios.salario:.2f}")


# Dicionario de Objetos:
# funcionarios = {} # <- Dicionario
# for i in range(50):
#     print(f"Entre com os dados do funcionario: {i + 1}")
#     f = Funcionario()
#     f.nome = input("Digite o nome: ")
#     f.salario = float(input("Digite o salário: "))
#     f.matricula = int(input("Digite a matrícula: "))
#     funcionarios[f.matricula] = f # <- A chave é a Matricula

# print("\n\nOs dados lidos foram:\n")
# for chave in funcionarios:
#     print(f"Funcionario: {chave}")
#     funcionario = funcionarios[chave]
#     print(f"Nome: {funcionario.nome}")
#     print(f"Matricula: {funcionario.matricula}")
#     print(f"Salario: {funcionario.salario:.2f}")