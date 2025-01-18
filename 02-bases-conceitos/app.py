texto = "Animal 2025"

# mostra o tipo
print(type(texto)) 
# out string

# mostra a primeira posição da string
print (texto[0]) 
# out A

# Mostra da primeira até a 4a posição da string
print (texto[0:5]) 
# out Anima

# Mostra quantos caracteres tem na string
print (len(texto)) 
# out 11

# Mostra a posição que a busca encontrou
print (texto.find('2025'))
# out 7

# mostra quanstos A foram encontrados
print (texto.count('A'))
# out 1

# mostra quanstos 2 foram encontrados no intervalo
print (texto.count('2', 7,11))
# out 2

# mostra tudo em maiúscula
print (texto.upper())
# out 

# mostra tudo em minúscula
print (texto.lower())
# out 

# mostra a primeira letra em maiúscula
print (texto.capitalize())
# out Animal 2025

# mostra as primeiras letras das palavras em maiúsculas
print (texto.title())
# out Animal 2025

# Separa as palavras da string cria uma lista
print (texto.split())
# out ['Animal','2025']

# Junta todas as palavras da string
# dentro do parênteses você escolhe o separador
# no caso foi '_'
lista_de_palavras = texto.split()
print ('_'.join(lista_de_palavras))
# out Animal_2025

# Remove os espaços no início e no fim
texto = '    AULA DJ-PYTHON   '
print (texto.strip())
# out AULA DJ-PYTHON"

# Remove os espaços da direita
texto = '    AULA DJ-PYTHON   '
print (texto.rstrip())
# out     AULA DJ-PYTHON

# Remove os espaços da esquerda
texto = '    AULA DJ-PYTHON   '
print (texto.lstrip())
# out AULA DJ-PYTHON

# 0 é igual a falso
print (0 == False)
# out True

# 1 é igual a verdadeiro
print (1 == True)
# out True

print ('a' == 'A')

seu_nome = input('Digite seu nome: ')
print (f"Olá {seu_nome}! Tudo bem?")
resposta = input()

if resposta == 'sim':
    print ('Que bom!')
else:
    print ('Que pena')
