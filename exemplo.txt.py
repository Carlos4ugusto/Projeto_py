# Abre o arquivo 'exemplo.txt' no modo de escrita
# e garante que ele seja fechado após a execução 
with open('exemplo.txt', 'w') as arquivo:
  arquivo.write('Olá este é o primeiro arquivo criado em Python.\n')
  arquivo.write('Ele será usado para demonstrar funções de manipulação.')

# Abre o mesmo arquivo no modo de leitura
  with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)