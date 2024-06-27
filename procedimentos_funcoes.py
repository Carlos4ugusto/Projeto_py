novo_deck = []

# inserir um novo card no deck


def inserir_novo():
    novo = input('Qual o nome do pokemon: ')
    if verificar(novo):
        novo_deck.append(novo)
    else:
        print('Esse card já existe no deck')

# Consultando o que está armazenado na lista

# Verificar se o item já existe na lista


def verificar(pokemon):
    if pokemon in novo_deck:
        return False
    else:
        return True



# Invocar funções
inserir_novo()
