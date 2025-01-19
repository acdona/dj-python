def risco():
    print('*' * 80)

def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

# lista de clientes
clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']

envia_email(clientes[0])
envia_email(clientes[1])
envia_email(clientes[2])
envia_email(clientes[3])
envia_email(clientes[4])

risco()

# A própria declaração do for já cria a variável cliente
# FOR (Utilizado quando você quiser rodar do início ao fim da lista)
for cliente in clientes:
    envia_email(cliente)

risco()

# Para retornar o índice também utilizamos o enumerate
for i, cliente in enumerate(clientes) :
    print(i, cliente)

risco()

# WHILE quando você quiser rodar enquanto encontrar uma condição verdadeira
numero = 0
while numero < 5:
    print(numero)
    numero += 1

risco()

# Executar 10x use range
for i in range(10):
    print(i)

risco()

# interrompendo laços com break
# enviando para determinado número de clientes
for i, cliente in enumerate(clientes):
    if i == 2:
        break
    envia_email(cliente)

risco()

numero = 0
while numero < 5:
    if numero == 2:
        break
    print(numero)
    numero += 1

risco()

# O continue pula para o próximo
for i, cliente in enumerate(clientes):
    if i == 2:
        continue
    envia_email(cliente)
# Só quando atender a condição vai enviar email

risco()

# Iterando cobre uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
print("Lista de frutas:")
for fruta in frutas:
    print(fruta)

risco()

# Somando número até 10
soma = 0
numero = 1
while numero <= 10:
    soma += numero
    numero += 1
print(f"A soma de 1 a 10 é: {soma}")

risco()

# Imprimindo números pares entre 1 e 10 (for)
print("Números pares de 1 a 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

risco()

print("Interrompendo ao encontrar 7:")
numero = 1
while True:
    print(numero)
    if numero == 7:
        break
    numero += 1

risco()

# Pulando números com continue (for)
print("Pulando o número 5:")
for i in range(1, 8):
    if i == 5:
        continue
    print(i)

risco()
