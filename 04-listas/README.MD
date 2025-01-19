# LISTAS E SEUS MÉTODOS
## Listas são utilizadas para guardar valores de itens semelhantes
## Listas em Python são estruturas de dados muito flexíveis e amplamente usadas para armazenar coleções de itens de diferentes tipos. Elas funcionam como arrays dinâmicos, o que significa que podem crescer ou diminuir de tamanho conforme necessário.
### Exemplo, lista de nomes de carros:
```python
carros = ['Fusca', 'Opala', 'Variante', 'Gol']
```
##  Aqui estão os principais aspectos das listas:
### 1 - Criação de listas
    . Uma lista em Python é criada usando colchetes ([]) e os elementos são separados por vírgulas.
```python
# Lista vazia
lista_vazia = []

# Lista com elementos
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]
mista = [42, "Python", 3.14, True]
```
### 2 - Propriedadses das listas
    . Ordenadas: Os itens têm uma ordem definida e podem ser acessados por índices.
    . Mutáveis: Você pode alterar os itens após criar a lista.
    . Permitem duplicatas: Uma lista pode conter itens repetidos.

### 3 - Operações básicas
    . Indexação
      Os elementos são acessados usando índices (começam do 0). 
      Você também pode usar índices negativos para acessar do final para o início.
```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Saída: maçã
print(frutas[-1]) # Saída: laranja
```
    . Fatiamento (Slicing)
      Você pode obter sublistas especificando intervalos.
```python
numeros = [1, 2, 3, 4, 5]
print(numeros[1:4])   # Saída: [2, 3, 4]
print(numeros[:3])    # Saída: [1, 2, 3]
print(numeros[::2])   # Saída: [1, 3, 5] (pula de 2 em 2)

```
    . Modificação
      Você pode alterar, adicionar ou remover elementos.
```python
# Alterar elementos
numeros[0] = 10
print(numeros)  # Saída: [10, 2, 3, 4, 5]

# Adicionar elementos
numeros.append(6)        # Adiciona ao final
numeros.insert(2, 15)    # Insere 15 no índice 2

# Remover elementos
numeros.remove(4)        # Remove o primeiro 4 encontrado
ultimo = numeros.pop()   # Remove o último item e o retorna
```
### 4 - Métodos úteis
### Listas possuem vários métodos embutidos para manipulação:

    . Adicionar elementos:
      append(x): Adiciona x ao final da lista.
      extend(iterável): Adiciona todos os itens do iterável.
    
    . Remover elementos:
      remove(x): Remove o primeiro elemento igual a x.
      pop([i]): Remove e retorna o elemento no índice i (ou o último, se i não for especificado).

    . Ordenação e Reversão:
      sort(): Ordena a lista em ordem crescente (ou personalizada).
      reverse(): Inverte a ordem dos elementos.

    . Outros:
      index(x): Retorna o índice da primeira ocorrência de x.
      count(x): Conta quantas vezes x aparece.
      clear(): Remove todos os elementos.
```python
numeros = [3, 1, 4, 1, 5]
numeros.sort()
print(numeros)  # Saída: [1, 1, 3, 4, 5]
```

### 5 - Iteração com listas
#### Você pode percorrer uma lista usando loops.

```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```
#### Ou com compreensão de listas para criar novas listas de forma concisa:
```python
quadrados = [x**2 for x in range(5)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16]
```

### 6 - Copiando listas
#### Cuidado ao copiar listas, pois elas são mutáveis:
```python
lista1 = [1, 2, 3]
lista2 = lista1      # Ambas apontam para a mesma lista
lista2[0] = 42
print(lista1)        # Saída: [42, 2, 3]
```
#### Para criar uma cópia real:
```python
lista2 = lista1.copy()

# Ou usando slicing:
lista2 = lista1[:]
```
### Listas são extremamente versáteis e utilizadas em quase todos os tipos de aplicações Python.

#
## Mais exemplos com listas e seus métodos:
- Caso 1: Dobrar o valor de um produto
- Caso 2: Todos os produtos que custarem acima de 1.000 dolares, imposto de 50% sobre o valor total

```python
precos = [500, 1500, 2000, 100, 25]

# Caso 1
novo_preco = []
for preco in precos:
    novo_preco.append(preco * 2)
print(novo_preco)

# Caso 2
imposto = []
for preco in precos:
    if preco > 1000:
        imposto.append(preco / 2)
print(imposto)
```

    [1000, 3000, 4000, 200, 50]
    [750.0, 1000.0]
   
### fazendo com list comprehension
```python
# Caso 1
novo_preco2 = [preco * 2 for preco in precos]
print(novo_preco2)

# Caso 2
imposto2 = [preco / 2 for preco in precos if preco > 1000]
print(imposto2)
```
    [1000, 3000, 4000, 200, 50]
    [750.0, 1000.0]

### Qual a vantagem?

- tudo em 1 linha de código
- mais rápido e "simples" se você já está acostumado

```python
# Listas
carros = ['Variante', 'Gol', 'Fuscão', 'Opala']
carros
```
    ['Variante', 'Gol', 'Fuscão', 'Opala']

```python
# append adiciona no final da lista
carros.append('Corcel')
carros
```
    ['Variante', 'Gol', 'Fuscão', 'Opala', 'Corcel']

```python
carros[0]
```
    'Variante'
```python
# insert para inserir na posição que quiser
carros.insert(1, 'Escort')
carros
```
    ['Variante', 'Escort', 'Escort', 'Gol', 'Fuscão', 'Opala', 'Corcel']

```python
# remover elementos da lista
# pop remove o último elemento da lista
carros.pop()
```
    'Corcel'
```python
carros
```
    ['Variante', 'Escort', 'Escort', 'Gol', 'Fuscão', 'Opala']

```python
# remove elemento na posição escolhida
del carros[1]
```
    ['Variante', 'Escort', 'Gol', 'Fuscão', 'Opala']

```python
# remove() remove por parâmetro
carros.remove('Gol')
```
    ['Variante', 'Escort', 'Gol', 'Opala']

```python
carros[2] = "Gol"
```

```python
# count para contar quantos elementos com o nome informado existem na lista
carros.count('Gol')
```
    1

```python
carros.append('Fuscão')
```
    ['Variante', 'Escort', 'Gol', 'Opala', 'Kombi', 'Fuscão']

```python
# invertindo a ordem dos elementos
carros.reverse()
```
    ['Fuscão', 'Kombi', 'Opala', 'Gol', 'Escort', 'Variante']

```python
# ordenar a lista
carros.sort()
```
    ['Escort', 'Fuscão', 'Gol', 'Kombi', 'Opala', 'Variante']
