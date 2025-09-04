def processar_texto():
    """
    Captura, salva, formata e sobrescreve um arquivo de texto.
    """
    nome_do_arquivo = 'texto_autores.txt'

    # --- Etapa 1: Captura de texto ---
    print("Por favor, insira o texto. Digite uma linha em branco para finalizar.")
    
    conteudo_digitado = []
    while True:
        linha = input()
        if not linha:  # Se a linha estiver vazia, o loop para
            break
        conteudo_digitado.append(linha + '\n')

    # --- Etapa 2: Salvamento em arquivo ---
    # Abre o arquivo em modo de escrita ('w') e salva o texto
    try:
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(conteudo_digitado)
        print(f"\nTexto salvo com sucesso em '{nome_do_arquivo}'.")
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")
        return

    # --- Etapa 3: Leitura e conversão ---
    # Lê o conteúdo completo do arquivo e o converte para maiúsculas
    try:
        with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
            texto_original = arquivo.read()
            texto_maiusculo = texto_original.upper()
        print("\nTexto lido e convertido para maiúsculas.")
    except IOError as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    # --- Etapa 4: Sobrescrita do arquivo ---
    # Sobrescreve o arquivo com o texto em maiúsculas
    try:
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto_maiusculo)
        print(f"Arquivo '{nome_do_arquivo}' sobrescrito com a nova formatação.")
    except IOError as e:
        print(f"Erro ao sobrescrever o arquivo: {e}")
        return
    
    print("\nProcesso concluído com sucesso!")
    
# Executa a função principal
if __name__ == "__main__":
    processar_texto()