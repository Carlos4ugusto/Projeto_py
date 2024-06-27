# para saber o tipo de dados de uma variável, utilizamos a instrução type()
# tipos de dados em python
nome = 'Advogado Constituído'
classe_carta = 'Druida'
custo_mana = 2
pontos_ataque = 1
pontos_vida = 3
colecionavel = True

# Operações em python

total_mana = 10
custo_mana = 2
total_mana = total_mana - custo_mana

print(total_mana)

# entrada de dados  - instrução input()
nome_carta = input('Qual o nome da carta: ')
pontos_vida = int(input('Quantos pontos de vida: '))

# Descobrindo os tipos de dados
# Verificar conversão de dados
type(pontos_vida)

# Saída de dados
# Escrever a saída no padrão Card : nome_card (custo_mana)
print(nome_carta)
print(pontos_vida)

# atividade 2
mana_jogador = 5
mana_invocar = int(input('Custo de mana do card: '))

if mana_jogador > mana_invocar:
    mana_jogador = mana_jogador - mana_invocar
    print('Card foi posicionado na mesa')
else:
    print('Você não tem mana suficiente! Escolha outro card')

print('Pontos de mana: ', mana_jogador)

# Elif
print('Informe o tipo de carta que você deseja buscar: ',
      '(1) Druida',
      '(2) Caçador',
      '(3) Mago',
      '(4) Paladino',
      '(5) Xamã')
tipo_carta = input('Digite um número: ')

if tipo_carta == '1':
    tipo_carta = 'Druida'
elif tipo_carta == '2':
    tipo_carta = 'Caçador'
elif tipo_carta == '3':
    tipo_carta = 'Mago'
elif tipo_carta == '4':
    tipo_carta = 'Paladino'
elif tipo_carta == '5':
    tipo_carta = 'Xamã'
else:
    print('Erro, nenhum tipo correspondente!')

print(tipo_carta)
