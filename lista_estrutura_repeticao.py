# Criando uma lista inicializada com valores
pokedex = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu']

# Verificando o tamanho da lista - função Len()
len(pokedex)
print(len(pokedex))

# Acessando elementos da lista
pos = 3
print(f"{pokedex[pos]} eu escolho você!")

# Acessando partes da lista
pokedex[1:4]

# Acessando o último item
print(f"Último pokemon na pokedex é o {pokedex[-1]}")

# Criando uma lista vazia
card_deck = []

# Adicionando itens na lista
card_deck.append('Pikachu, Charmander')
card_deck.append('Squirtle')
print(card_deck)

#estrutura de repetição
for pokemon in pokedex:
    print(f"{pokemon} está na sua pokedex")
else:
    print('Esses são todos os seus pokémons!')

print("Vamos montar o seu novo deck de pokemons!")

inserir = '1'
novo_deck = []

while inserir == '1':
    novo_card = input('Qual é o nome do pokemon: ')
    novo_deck.append(novo_card)
    inserir = input('Deseja inserir um novo? (1) Sim (0) Não: ')

print(f"Seu novo deck tem {len(novo_deck)} cards")

