def risco():
    print('*' *80)

risco()

meu_dic = {'nome': 'Antonio', 'idade': 60, 'profissao': 'Dev'}

print('Obter elemento do dicionário:')
# Obter elemento do dicionário
print (meu_dic['nome'])
print (meu_dic.get('profissao'))

risco()

print('Remover elemento do dicionário:')
# Remover elemento do dicionário
print (meu_dic.pop('idade'))
print (meu_dic)
# out 'nome': 'Antonio', 'profissao': 'Dev'}

risco()

print('Mostrar as keys do dicionário:')
# Mostrar as keys do dicionário
print (meu_dic.keys())

risco()

print('Mostrar todos os valores do dicionário:')
# Mostrar todas os valores do dicionário
print (meu_dic.values())

risco()

print('Apagar todos os dados do dicionário:')
# Apagar todos os dados do dicionário
meu_dic.clear()
print (meu_dic)

risco()

print('Os dicionários, podem conter listas e outros dicionários')

risco()

pessoa = {
    'nome:': 'Antonio',
    'idade': 60,
    'profissao': 'Dev',
    'interesses': ['Python', 'Programação', 'Marcenaria'],
    'pet' : {
        'nome': 'Tanajura',
        'idade': 100,
        'peso': '20kg'
    }
}

print('Interesses e primeiro item interesses')
print (pessoa.get('interesses'))
print (pessoa.get('interesses')[0])

risco()

print('pet e primeiro item pet')
print (pessoa.get('pet'))
print (pessoa.get('pet').get('nome'))

risco()

print('pet e idade do petg')
print (pessoa['pet']['idade'])

risco()

### Para inserir dados no dicionário
print('Para inserir dados no dicionário')
pessoa['ano_nascimento'] = 1964
print(pessoa)
pessoa['cores_favoritas'] = ['azul', 'verde', 'amarelo']
print(pessoa)
pessoa['mae'] = {'nome': 'Xispita', 'idade': 184 }
print(pessoa)
