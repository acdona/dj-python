# POO - Programação Orienteda a Objetos

## Conceito de POO com Python
### Um objeto possui propriedades e funções (métodos)

#### Exemplo:
```python
class Celular:
    marca = 'Motorolla'
    modelo = 'Tijolora'
    cor = 'Verde'
    tem_camera = False
    bateria = 'Infinita'
    
    def fazer_ligacoes(self):
        print('Fazendo ligação...')
        
    def jogar_cobrinha(self):
        print('Jogando cobrinha...')
        
    def despertador(self):
        print('Despertador...')
        
celular = Celular()
celular.marca
# out: Motorolla
```

```python
celular.jogar_cobrinha()
# out: Jogando cobrinha...
```

# self é uma instância da própria classe
### No contexto de Python, self é um parâmetro especial usado dentro de métodos de classes para se referir à instância atual da classe. Ele permite que você acesse atributos e métodos pertencentes a essa instância. Vamos entender melhor como ele funciona no exemplo fornecido:
### Explicação do código
A classe Celular tem atributos e métodos que descrevem o comportamento de um celular antigo (o famoso "tijorola"). Quando você cria um objeto dessa classe, como no caso de celular = Celular(), essa instância pode acessar os atributos e métodos definidos na classe.

Função do self:
Nos métodos da classe, como fazer_ligacoes, self é o primeiro parâmetro padrão.
O self é usado para acessar os atributos ou outros métodos da instância específica da classe.
No exemplo, o self não foi explicitamente utilizado, porque está acessando atributos de classe (não específicos de uma instância).

Comparação com o uso de self
Se quisermos que cada instância tenha valores diferentes para os atributos, precisaríamos definir esses atributos com self dentro de um método inicializador (__init__). Por exemplo:


```python
class Celular:
    def __init__(self, marca, modelo, cor, tem_camera, bateria):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.tem_camera = tem_camera
        self.bateria = bateria
    
    def fazer_ligacoes(self):
        print('Fazendo ligação...')

# Criando uma instância de Celular
celular1 = Celular('Nokia', 'Tijolão', 'Azul', False, 'Infinita')
celular2 = Celular('Motorola', 'Tijorolar', 'Preto', True, '500 mAh')

print(celular1.marca)  # Saída: Nokia
print(celular2.marca)  # Saída: Motorola

```

O que mudou?
- O método __init__ usa o self para inicializar atributos específicos de cada instância.
- Agora, marca, modelo e outros atributos pertencem a cada instância individual, e não à classe como um todo.

O que o self não é
- Não é uma palavra reservada – você pode usar outro nome, mas por convenção e legibilidade, usa-se self.
- Ele é automaticamente preenchido pela instância quando um método é chamado. Por exemplo:
```python
celular.fazer_ligacoes()
```
Internamente, Python traduz isso para:

```python
Celular.fazer_ligacoes(celular)
```
- Portanto, o self permite que você trabalhe com dados que pertencem à instância, tornando a classe mais flexível e reutilizável.

# Herança

### A herança em Python é um princípio fundamental da Programação Orientada a Objetos (POO) que permite que uma classe (chamada de classe derivada ou subclasse) herde atributos e métodos de outra classe (chamada de classe base ou superclasse). Isso promove a reutilização de código e permite que você construa hierarquias de classes.

### Principais Características da Herança:
1. Reutilização de código: A subclasse pode usar os atributos e métodos definidos na superclasse sem precisar reescrevê-los.

2. Extensibilidade: A subclasse pode adicionar novos atributos e métodos ou modificar (sobrescrever) os existentes na superclasse.

3. Hierarquias: Uma subclasse pode herdar de uma ou mais superclasses (herança múltipla).

### Como funciona a herança no Python?
Sintaxe básica:
##### Você especifica a superclasse entre parênteses ao definir a subclasse:

```python
class Superclasse:
    # Atributos e métodos da classe base
    pass

class Subclasse(Superclasse):
    # Atributos e métodos da subclasse
    pass

```

#### Exemplo de herança:
#### Superclasse:


```python
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def fazer_som(self):
        print("O animal faz um som.")
```

#### Subclasse:

```python
class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Chamando o __init__ da superclasse
        super().__init__(nome, "Cachorro")
        self.raca = raca
    
    def fazer_som(self):  # Sobrescrevendo o método
        print("O cachorro late.")

```

#### Uso:

```python
# Criando uma instância de Cachorro
meu_cachorro = Cachorro("Caramelo", "Vira Lara Xexelento")

# Acessando métodos da superclasse e da subclasse
print(meu_cachorro.nome)     # Caramelo (herdado da superclasse)
print(meu_cachorro.especie)  # Cachorro (definido na superclasse)
print(meu_cachorro.raca)     # Vira Lata (definido na subclasse)

meu_cachorro.fazer_som()     # O cachorro late. (sobrescrito)
```

### O que é super()?
- A função super() é usada para acessar métodos ou atributos da superclasse.
- No exemplo acima, super().__init__(nome, "Cachorro") chama o construtor (__init__) da classe Animal, evitando a duplicação de código.

#### Herança Múltipla:
Python suporta herança múltipla, ou seja, uma classe pode herdar de mais de uma superclasse. Exemplo:


```python
class Mamifero:
    def amamentar(self):
        print("Amamentando...")

class Terrestre:
    def andar(self):
        print("Andando sobre a terra...")

class Gato(Mamifero, Terrestre):
    def miar(self):
        print("Miau!")

```

#### Uso:

```python
gato = Gato()
gato.amamentar()  # Amamentando...
gato.andar()      # Andando sobre a terra...
gato.miar()       # Miau!
```

    Amamentando...
    Andando sobre a terra...
    Miau!
    

#### Benefícios da Herança:
- Reduz duplicação de código.
- Facilita a manutenção: alterações na superclasse afetam todas as subclasses automaticamente.
- Permite polimorfismo: métodos podem ser sobrescritos nas subclasses para alterar comportamentos.

#### Quando usar?
Use herança quando há uma relação de "é um(a)" entre as classes. Por exemplo, um cachorro é um animal. Se não houver essa relação natural, pode ser melhor usar composição ou outra abordagem.

# Polimorfismo de Classe

Permite que classes diferentes que herdam da mesma classe, possam ter propriedades e funções com o mesmo nome, mas façam coisas diferentes

Sua definição de polimorfismo está correta e bem colocada! Em termos simples, polimorfismo na Programação Orientada a Objetos (POO) permite que objetos de diferentes classes (que compartilham uma relação por meio de herança) usem métodos com o mesmo nome, mas que se comportam de maneira diferente dependendo da classe.

#### Explicando o conceito:
O termo polimorfismo vem do grego e significa "muitas formas". Em POO, isso se traduz na capacidade de usar um mesmo método ou propriedade com diferentes implementações em subclasses.

### Características principais do polimorfismo:
1. Flexibilidade:

   . Você pode tratar diferentes objetos da mesma forma e deixar que eles decidam o que fazer com base em sua própria implementação.


2. Sobrescrita de métodos (overriding):

   . Subclasses podem redefinir métodos da superclasse para implementar um comportamento específico.


3. Interface comum:
 
    .Classes diferentes podem oferecer métodos com nomes idênticos, garantindo que sejam usadas de forma consistente no programa.

#### Exemplo de polimorfismo:
##### Superclasse:


```python
class Animal:
    def fazer_som(self):
        print("O animal faz um som.")

```

#### Subclasses com métodos sobrescritos


```python
class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late: Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("O gato mia: Miau!")

```

#### Uso do Polimorfirmo


```python
# Lista de objetos de diferentes classes
animais = [Cachorro(), Gato()]

# Iteração polimórfica
for animal in animais:
    animal.fazer_som()

```

    O cachorro late: Au Au!
    O gato mia: Miau!
    

Aqui, ambos os objetos (Cachorro e Gato) possuem o método fazer_som, mas cada um implementa um comportamento diferente. O código trata todos os objetos como instâncias da classe Animal, mas os métodos específicos das subclasses são executados.

#### Benefícios do polimorfismo:
1. Generalização do código:
   - Você pode criar funções ou estruturas que funcionam com qualquer objeto de uma hierarquia de classes.


2. Extensibilidade:
   - É fácil adicionar novas classes (como Pássaro ou Cavalo no exemplo acima) sem alterar o código existente.


3. Simplicidade:
   - Ele abstrai os detalhes das subclasses, focando no comportamento geral.


#### Conclusão: 
O polimorfismo é uma das ferramentas mais poderosas da POO, pois permite criar sistemas que são extensíveis, reutilizáveis e fáceis de manter. A sua definição reflete exatamente esse conceito!

# Polimorfismo de Interface

Polimorfismo de Interface é um tipo específico de polimorfismo em que diferentes classes implementam os mesmos métodos ou propriedades definidos por uma interface, garantindo que essas classes possam ser usadas de maneira intercambiável, mesmo que seus comportamentos sejam diferentes.

#### O que é uma interface?
Em termos gerais, uma interface define um contrato que uma classe deve seguir. Ela especifica quais métodos (e, às vezes, propriedades) devem ser implementados, mas não fornece a implementação deles.

Em Python, as interfaces podem ser simuladas usando classes abstratas, com a ajuda do módulo abc (Abstract Base Classes).

#### Características do Polimorfismo de Interface:
1. Definição comum:
   - Todas as classes que implementam a interface devem ter os mesmos métodos, garantindo consistência.


2. Comportamento único:
   - Cada classe pode implementar os métodos da interface de maneira diferente, adequando-se às suas necessidades específicas.


3. Substituibilidade:
   - Objetos de diferentes classes podem ser tratados de forma uniforme, desde que implementem a mesma interface.


4. Flexibilidade:
   - O código que utiliza a interface não precisa saber qual classe específica está sendo usada. Ele confia no contrato definido pela interface.

#### Exemplo em Python:
##### Definindo a Interface:
Usamos o módulo abc para criar uma interface. Aqui, definimos uma interface Forma, que exige que as classes implementem o método area:


```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass  # Método abstrato: não tem implementação na interface

```

### Implementando a Interface:
Agora criamos duas classes que implementam a interface Forma:


```python
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * (self.raio ** 2)

```

#### Uso do Polimorfismo de Interface:


```python
formas = [Retangulo(10, 5), Circulo(7)]

for forma in formas:
    print(f"A área é: {forma.area()}")

```

    A área é: 50
    A área é: 153.86
    

Aqui, o código que chama o método area não se preocupa se está lidando com um retângulo ou um círculo. Ele apenas confia que ambas as classes implementam o método area definido pela interface Forma.

#### Diferenças entre Polimorfismo Geral e de Interface:

| **Polimorfismo Geral**                            | **Polimorfismo de Interface**                  |
|---------------------------------------------------|-----------------------------------------------|
| Baseado em herança e sobrescrita de métodos na mesma hierarquia de classes. | Baseado em implementar um contrato comum, sem depender de herança direta. |
| Subclasses personalizam ou sobrescrevem métodos herdados. | Classes podem ser completamente diferentes, mas implementam a mesma interface. |
| Focado em hierarquias de classes.                | Focado em contratos comuns entre classes.     |



#### Benefícios do Polimorfismo de Interface:
1. Desacoplamento:

    . O código que usa a interface não depende de implementações específicas.


2. Flexibilidade e escalabilidade:

    . Adicionar novas classes que implementam a interface não requer mudanças no código existente.


3. Segurança:

    . A interface garante que as classes implementem os métodos necessários, evitando erros.

#### Conclusão:
O Polimorfismo de Interface é uma prática que promove a consistência e extensibilidade, permitindo que objetos de diferentes classes sejam tratados de forma uniforme por meio de métodos ou propriedades definidos em uma interface comum. É uma abordagem crucial para construir sistemas robustos e flexíveis.
