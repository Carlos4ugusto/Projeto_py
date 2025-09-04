print("Iterando sobre arquivos")

with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
    print("Fim do arquivo", arquivo.name)