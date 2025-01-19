# Exemplos com listas
def risco():
    print('*' * 80)

risco()

# - Caso 1: Dobrar o valor de um produto
# - Caso 2: Todos os produtos que custarem acima de 1.000 dolares, imposto de 50% sobre o valor total

precos = [500, 1500, 2000, 100, 25]

# Caso 1
novo_preco = []
for preco in precos:
    novo_preco.append(preco * 2)
print(novo_preco)

risco()

# Caso 2
imposto = []
for preco in precos:
    if preco > 1000:
        imposto.append(preco / 2)
print(imposto)
# out  [1000, 3000, 4000, 200, 50]
#      [750.0, 1000.0]

risco()

### fazendo com list comprehension

# Caso 1
novo_preco2 = [preco * 2 for preco in precos]
print(novo_preco2)

risco()

# Caso 2
imposto2 = [preco / 2 for preco in precos if preco > 1000]
print(imposto2)
# out: [1000, 3000, 4000, 200, 50]
#      [750.0, 1000.0]

# Qual a vantagem?

# tudo em 1 linha de código
# mais rápido e "simples" se você já está acostumado


carros = ['Variante', 'Gol', 'Fuscão', 'Opala']

# append adiciona no final da lista
carros.append('Corcel')
#  ['Variante', 'Gol', 'Fuscão', 'Opala', 'Corcel']

carros[0]
# Variante

# insert para inserir na posição que quiser
carros.insert(1, 'Escort')
# ['Variante', 'Escort', 'Escort', 'Gol', 'Fuscão', 'Opala', 'Corcel']

# remover elementos da lista
# pop remove o último elemento da lista
carros.pop()
# Corcel
# ['Variante', 'Escort', 'Escort', 'Gol', 'Fuscão', 'Opala']
# remove elemento na posição escolhida
del carros[1]
# ['Variante', 'Escort', 'Gol', 'Fuscão', 'Opala']

# remove() remove por parâmetro
carros.remove('Gol')
# ['Variante', 'Escort', 'Gol', 'Opala']

# adiciona na posição
carros[2] = "Gol"

# count para contar quantos elementos com o nome informado existem na lista
carros.count('Gol')
# 1

carros.append('Fuscão')
# ['Variante', 'Escort', 'Gol', 'Opala', 'Kombi', 'Fuscão']

# invertindo a ordem dos elementos
carros.reverse()
# ['Fuscão', 'Kombi', 'Opala', 'Gol', 'Escort', 'Variante']

# ordenar a lista
carros.sort()
# ['Escort', 'Fuscão', 'Gol', 'Kombi', 'Opala', 'Variante']


