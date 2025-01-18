# Bases e conceitos importantes

## Sistemas Desktop
* Ficam dentro do computador local
* Todos os recursos estão dentro do computador do usuário
* Não acessam recursos externos

## Sistemas Desktop em Rede
* O banco de dados fica no servidor na mesma rede que os demais computadores
* Os demais computadores acessam pela rede o banco de dados no servidor

## Sistemas Web
* Fica no proprietário pelo software, onde as empresas acessam pela web, 
sem precisar de programas instalados  nos computadores e nem servidor local.
* É necessário apenas o navegador de internet.

## A comunicação do sistema web é feita via protolo HTTP
* HTTP é a sigla para Hypertext Transfer Protocol, que em português significa Protocolo de Transferência de Hipertexto. É um protocolo de comunicação que permite a troca de informações entre dispositivos conectados em rede, como clientes e servidores da web

### HTTP e HTTPS
* O cliente faz uma requisição ao servidor (Request) e recebe uma resposta (Response)

## Exemplo do envio de um GET para o Google
* https://www.google.com/search?q=https&hl=pt-BR
* HTTPS (Hypertext Transfer Protocol Secure) é um protocolo que permite a transferência de dados entre um servidor e um navegador de forma segura e criptografada.

## O protocolo GET mostra as informações enviadas, no navagador, o POST envia uma "mensagem" para o servidor que enviará uma resposta a essa requisição.

## O que é PIP?
### É um gerenciador de pacotes para projetos Python. É com ele que instalamos, removemos e atualizamos pacotes em nossos projetos. É similar aos conhecidos npm e composer
### Local do ferramentas para Python https://pypi.org/
### Exemplo de busca de pacotes: https://pypi.org/project/pandas/

## Instação do Python no Windows 11
* https://www.python.org/
* Atual versão em 17/01/2025 3.13.1
* No instalador assinale a opção de Add python.exe to Path 
* Customize installation, marque todas opções
* Advanced Options, marque todas opções
* No prompt de comando: python --version

## Instalando VSCode
* https://code.visualstudio.com/Download
* Em 'Selecionar Tarefas Adicionais', marque todas menos atalho

## Instalando extensões
* Clique em extensões: Coloque na busca Python
* Instale o Python Microsoft
* Instale Material Icon Them de Philipp Kief
  * Ele muda os ícones de pastas e arquivos
* Instalar o Dracula Theme Official (Opcional)

## O PIP, atualmente, já é instalado por padrão, junto com o Python.
* Documentação e instalação do PIP: https://pip.pypa.io/en/stable/installation/
* Documentação do VENV: https://docs.python.org/3/library/venv.html#

## Caso você tenha algum problema com 'Política de Execução Powershell'
## Política de execução Powershell
* Windows Powershel (executar como administrador)
* Set-ExecutionPolicy RemoteSigned (Sim)
* Para voltar o bloqueio
* Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser (Sim)
* A linha acima vai liberar apenas para o ambiente atual
* Set-ExecutionPolicy Unrestricted
* A linha acima libera no principal tudo
* Get-ExecutionPolicy mostra RemoteSigned, porque escolhi liberar apenas essa

## Criando um ambiente virtual.
### Sempre que começarmos um projeto, iremos criar um ambiente virtual
### O ambiente virtual serve para não encher a máquina principal de pacotes, pois cada projeto precisará instalar os pacotes, que em outro projeto, não precisaria.
### Dentro da pasta de seu projeto
```bash
PS F:\seu_projeto\python -m venv ambiente
```
### Onde 'ambiente' é um nome qualquer. Alguns programadores utilizam 'venv' mesmo.
### Preferi colocar 'ambiente' para mostrar a diferença.

### Ativando o ambiente virtual
```bash
ambiente\Scripts\activate
```
### Aparece <span style="color:#1FD16E">(ambiente) PS F:\seu_projeto></span> na frente do prompt
### Sempre que você fechar o teminal, o ambiente virtual também será fechado
### Então habitue-se a sempre conferir se ele está ativado.

#
# Tipos Primitivos no Python
## No Python, os tipos primitivos (ou tipos básicos) são aqueles que representam os dados fundamentais usados no dia a dia de programação. Estes incluem números, textos, valores booleanos e estruturas simples. Aqui estão os tipos primitivos mais comuns:

### 1 - Números
    - int (inteiro): Representa números inteiros, positivos ou negativos, sem ponto decimal e zero.
      Exemplo: 10, -5, 0
    - float (ponto flutuante): Representa números decimais (reais).
      Exemplo: 3.14, -0.01, 2.0
    - complex (números complexos): Representa números com parte real e imaginária.
      Exemplo: 3+4j, 1j, -2.5+0j
### 2. Sequências
    - str (string): Representa cadeias de caracteres (texto). Strings são delimitadas por aspas simples (') ou duplas (").
    Exemplo: "Hello, World!", 'Python', ""
    - list (lista): Coleção ordenada e mutável de elementos que podem ser de tipos diferentes.
      Exemplo: [1, 2, 3], ["apple", "banana", 42]
    - tuple (tupla): Coleção ordenada e imutável de elementos que podem ser de tipos diferentes.
      Exemplo: (1, 2, 3), ("a", "b", "c")
### 3. Conjuntos
    - set (conjunto): Coleção não ordenada de elementos únicos.
      Exemplo: {1, 2, 3}, {3, 5, 7, "a"}
    - frozenset (conjunto congelado): Um conjunto imutável.
      Exemplo: frozenset([1, 2, 3])
### 4. Mapeamentos
    - dict (dicionário): Coleção de pares chave-valor, onde as chaves são únicas.
      Exemplo: {"name": "John", "age": 30}, {1: "a", 2: "b"}
### 5. Booleanos
    - bool (booleano): Representa valores lógicos, usados em condições.
      Valores: True, False
### 6. Nenhum Valor
    - NoneType: Representa a ausência de valor ou um valor nulo. Há apenas um objeto desse tipo: None.
      Exemplo: None
### Esses tipos primitivos são os blocos básicos de construção para programar em Python.

### Exemplo em Python:
```python
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
# out ANIMAL 2025

# mostra tudo em minúscula
print (texto.lower())
# out animal 2025

# mostra a primeira letra em maiúscula
print (texto.capitalize())
# out Animal 2025

# mostra as primeiras letras das palavras em maiúsculas
print (texto.title())
# out Animal 2025

# Separa as palavras da string cria um array
print (texto.split())
# out ['Animal','2025']

# Junta todas as palavras da string
# dentro do parênteses você escolhe o separador
# no caso foi '_'
lista_de_palavras = texto.split()
print ('_'.join(lista_de_palavras))
# out Animal_2025

# Retira os espaços no início e no fim
texto = '    AULA DJ-PYTHON   '
print (texto.strip())
# out AULA DJ-PYTHON

# Remove os espaços da direita
texto = '    AULA DJ-PYTHON   '
print (texto.rstrip())
# out     AULA DJ-PYTHON

# Remove os espaços da esquerda
texto = '    AULA DJ-PYTHON   '
print (texto.lstrip())
# out AULA DJ-PYTHON
```

## Operadores lógicos
### São utilizados para verificações de verdadeiro ou falso
#### or -> condição OU 
#### and -> condição E
#### == -> igual
#### != -> diferente

```python
print (0 == False)
# out True

print (1 == True)
# out True
```
## Funções no Python
### Uma função nada mais é do que um conjunto ou bloco de comandos que executam alguma ação ou tarefa.
### A função pode possuir parâmetros ou não.

### Exemplo de função sem parâmetro(s):

```python
def animal():
    print('Animal')
```
### Exemplo de função com parâmetros:
```python
def somar(num1, num2):
    return (num1 + num2)
```
### Quando a função possui parâmetros, você precisa passar os argumentos para ela.
### Exemplo: 
#### print soma(3, 2) 0 3 e 0 2 são os 'argumentos' passados para função
### Se você precisar repetir um código mais de uma vez, transforme em uma função
### FUNÇÃO: POSSUI PARÂMETROS || Quando chamamos a função, passamos os argumentos para os parâmetros

