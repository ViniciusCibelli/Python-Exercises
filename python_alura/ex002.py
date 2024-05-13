#usando dictionary, {}
#dicionarios são sempre em pares e recebem qualquer valor. Ex:
instrutores = {"Vinicim": 21, "Vinisao": 20, "Bonizario": 87}
print(instrutores["Vinisao"])

dados = {'nome': 'Vinícius', 'idade': 20, 'sexo': 'Masculino'}
print(dados['nome'])
del dados['idade'] #deleta o indice pedido
print(dados)
dados['peso'] = 64.3 #cria um indice
print(dados['peso'])
print(dados)
