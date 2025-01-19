# LAÇOS DE REPETIÇÃO
## for / while

### Para enviar emais para uma lista de pessoas, você pode fazer assim:
```python
def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']

envia_email(clientes[0])
envia_email(clientes[1])
envia_email(clientes[2])
envia_email(clientes[3])
envia_email(clientes[4])
```
### Mas dessa forma, além de dar muito trabalho, você não vai saber quantos clientes possui na lista.
### Para isso existem os laços, exemplo:
### FOR (Utilizado quando você quiser rodar do início ao fim da lista)
```python
def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

# lista de clientes
clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']

# a prórpia declaração do for já cria a variável cliente
for cliente in clientes:
    envia_email(cliente)
```

### Para retornar o índice também, utilizamos o enumerate
```python
for i, cliente in enumerate(clientes) :
    print(i, cliente)

# out:
# 0 Ana
# 1 Jonas
# 2 Felipe
# 3 Cláudio
# 4 Renato
```

### WHILE quando você quiser rodar, enquanto for encontrada, uma condição verdadeira
```python
numero = 0

while numero < 5:
    print(numero)
    numero += 1
```

### MAIS EXEMPLOS
### Executar um for por 10x
```python
for i in range(10):
    print(i)
```
### Enviando para determinado número de clientes
```python
for i, cliente in enumerate(clientes):
    if i == 2:
        break
    envia_email(cliente)
```
### O break interrompe a execução de laços, tanto FOR, como WHILE

```python
numero = 0

while numero < 5:
    if numero == 2:
        break
    print(numero)
    numero += 1
```
### O continue pula para o próximo
```python
for i, cliente in enumerate(clientes):
    if i == 2:
        continue
    envia_email(cliente)
# Só quando atender a condição vai enviar email
```

### Contando de 1 a 5 (for)
```python
print("Contando de 1 a 5:")
for i in range(1, 6):
    print(i)
```

### Contando até ue o número seja 5 (while)
```python
print("Contando até 5:")
numero = 1
while numero <= 5:
    print(numero)
    numero += 1
```

### Iterando sobre uma lista
```python
frutas = ["maçã", "banana", "laranja", "uva"]
print("Lista de frutas:")
for fruta in frutas:
    print(fruta)
```

### Somando números até 10 (while)
```python
soma = 0
numero = 1
while numero <= 10:
    soma += numero
    numero += 1
print(f"A soma de 1 a 10 é: {soma}")
```

# Imprimindo números pares entre 1 e 10 (for)
```python
print("Números pares de 1 a 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

# Interrompendo um loop com break (while)
```python
numero = 1
while True:
    print(numero)
    if numero == 7:
        break
    numero += 1
```

# Pulando números com continue (for)
```python
print("Pulando o número 5:")
for i in range(1, 8):
    if i == 5:
        continue
    print(i)
```

