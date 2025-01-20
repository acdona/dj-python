# Dicionários

### Dicionários em Python são coleções de pares chave-valor. Cada chave é única e é usada para acessar o valor correspondente. Eles são definidos usando chaves `{}` e os pares chave-valor são separados por dois pontos `:`. 

### Exemplo de um dicionário em Python:
```python
meu_dicionario = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}
```
### Listas são com [ ] e dicionários com { }
## Obter elemento do dicionário
```python
print (meu_dic['nome'])
print (meu_dic.get('profissao'))
```

## Remover elemento do dicionáio
```python
print (meu_dic.pop('idade'))
print (meu_dic)
# out 'nome': 'Felipe', 'profissao': 'Dev'}
```

## Mostrar as keys do dicionário
```python
meu_dic = {'nome': 'Felipe', 'idade': 25, 'profissao': 'Dev'}
print (meu_dic.keys())
```

## Mostrar todas od valores do dicionário
```python
meu_dic = {'nome': 'Felipe', 'idade': 25, 'profissao': 'Dev'}
print (meu_dic.values())
```

## Apagar todos dicionário
```python
meu_dic.clear()
print (meu_dic)
```

### Os dicionários, podem conter listas e outros dicionários
```python
pessoa = {
    'nome:': 'Felipe',
    'idade': 25,
    'profissao': 'Dev',
    'interesses': ['Python', 'Programação', 'Notebooks'],
    'pet' : {
        'nome': 'Loki',
        'idade': 1,
        'peso': '2kg'
    }
}

print (pessoa.get('interesses'))
print (pessoa.get('interesses')[0])

print (pessoa.get('pet'))
print (pessoa.get('pet').get('nome'))

print (pessoa['pet']['idade'])
```

### Para inserir dados no dicionário
```python
pessoa['ano_nascimento'] = 1964
print(pessoa)
pessoa['cores_favoritas'] = ['azul', 'verde', 'amarelo']
print(pessoa)
pessoa['mae'] = {'nome': 'Maria', 'idade': 50 }
print(pessoa)
```
