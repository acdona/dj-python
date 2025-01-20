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
print(celular.marca)

# ***************************************

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


# *************************************************

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def fazer_som(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Chamando o __init__ da superclasse
        super().__init__(nome, "Cachorro")
        self.raca = raca
    
    def fazer_som(self):  # Sobrescrevendo o método
        print("O cachorro late.")


# Criando uma instância de Cachorro
meu_cachorro = Cachorro("Caramelo", "Vira Lara Xexelento")

# Acessando métodos da superclasse e da subclasse
print(meu_cachorro.nome)     # Caramelo (herdado da superclasse)
print(meu_cachorro.especie)  # Cachorro (definido na superclasse)
print(meu_cachorro.raca)     # Vira Lata (definido na subclasse)

meu_cachorro.fazer_som()     # O cachorro late. (sobrescrito)
