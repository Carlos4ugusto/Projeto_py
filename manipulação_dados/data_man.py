import os
from PIL import Image
from random import randint

def criar_imagem_exemplo(largura, altura):
    """Cria uma imagem simples com gradiente para a demonstração."""
    img = Image.new('RGB', (largura, altura))
    pixels = img.load()
    for y in range(altura):
        for x in range(largura):
            # Cria um gradiente de cores
            r = int((x / largura) * 255)
            g = int((y / altura) * 255)
            b = 100
            pixels[x, y] = (r, g, b)
    print("Imagem de exemplo criada.")
    img.save("imagem_original.png")
    return img

def main():
    """Função principal que executa todas as operações."""
    
    # 1. Carregar uma imagem simples do sistema de arquivos
    try:
        imagem_original_pil = criar_imagem_exemplo(256, 256)
    except FileNotFoundError:
        print("Erro: A imagem 'imagem_original.png' não foi encontrada. Certifique-se de que o arquivo existe.")
        return

    # 2. Converter a imagem em uma representação binária
    # Convertendo a imagem para o modo 'RGB' e obtendo os dados brutos (bytes)
    dados_binarios = imagem_original_pil.tobytes()
    print(f"\n2. Imagem convertida para dados binários. Tamanho: {len(dados_binarios)} bytes.")

    # 3. Exibir os dados binários (primeiros 50 bytes para não poluir a tela)
    print("3. Primeiros 50 bytes da imagem:")
    print(dados_binarios[:50].hex())

    # 4. Salvar esses dados em um arquivo binário
    nome_arquivo_binario = "dados_imagem.bin"
    with open(nome_arquivo_binario, "wb") as f_bin:
        f_bin.write(dados_binarios)
    print(f"\n4. Dados binários salvos em '{nome_arquivo_binario}'.")

    # 5. Fazer uma cópia desse arquivo binário
    nome_arquivo_copia = "dados_imagem_copia.bin"
    with open(nome_arquivo_binario, "rb") as f_bin, open(nome_arquivo_copia, "wb") as f_copia:
        f_copia.write(f_bin.read())
    print(f"\n5. Cópia do arquivo binário criada em '{nome_arquivo_copia}'.")

    # 6. Manipular os dados do arquivo binário cópia
    print("\n6. Manipulando os dados binários (invertendo bytes aleatórios)...")
    
    with open(nome_arquivo_copia, "r+b") as f_modificado:
        tamanho_arquivo = os.path.getsize(nome_arquivo_copia)
        
        # Manipula 1% dos bytes do arquivo aleatoriamente
        num_modificacoes = int(tamanho_arquivo * 0.01)
        for _ in range(num_modificacoes):
            # Posiciona o cursor em um byte aleatório
            posicao = randint(0, tamanho_arquivo - 1)
            f_modificado.seek(posicao)
            
            # Lê o byte, inverte seus bits e escreve de volta
            byte_original = f_modificado.read(1)
            byte_modificado = bytes([~byte_original[0] & 0xFF])
            
            f_modificado.seek(posicao)
            f_modificado.write(byte_modificado)
    print("Dados binários manipulados com sucesso.")

    # 7. Carregar a imagem modificada a partir do arquivo binário e exibi-la
    print("\n7. Carregando a imagem modificada e exibindo o resultado.")
    with open(nome_arquivo_copia, "rb") as f_modificado:
        dados_modificados = f_modificado.read()
    
    # Criar uma nova imagem a partir dos dados binários modificados
    # A largura e altura devem ser as mesmas da imagem original
    largura, altura = imagem_original_pil.size
    try:
        imagem_modificada = Image.frombytes('RGB', (largura, altura), dados_modificados)
        imagem_modificada.save("imagem_modificada.png")
        imagem_modificada.show()
    except ValueError as e:
        print(f"Erro ao reconstruir a imagem: {e}")
        print("Isso pode ocorrer se a manipulação corrompeu o cabeçalho do arquivo.")

if __name__ == "__main__":
    main()