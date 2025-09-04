import sqlite3

# Conectando ao banco de dados (ou criando um novo se não existir)
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Criando a tabela de professores
cursor.execute('''
CREATE TABLE IF NOT EXISTS professores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    disciplina TEXT NOT NULL
)
''')
conn.commit()

# Função para adicionar um professor
def adicionar_professor():
    nome = input("Digite o nome do professor: ")
    disciplina = input("Digite a disciplina do professor: ")
    cursor.execute('''
    INSERT INTO professores (nome, disciplina) VALUES (?, ?)
    ''', (nome, disciplina))
    conn.commit()
    print("Professor adicionado com sucesso!")

# Função para listar todos os professores
def listar_professores():
    cursor.execute('SELECT * FROM professores')
    professores = cursor.fetchall()
    if professores:
        for professor in professores:
            print(f"ID: {professor[0]}, Nome: {professor[1]}, Disciplina: {professor[2]}")
    else:
        print("Nenhum professor cadastrado.")

# Função para remover um professor
def remover_professor():
    id_professor = input("Digite o ID do professor a ser removido: ")
    cursor.execute('DELETE FROM professores WHERE id = ?', (id_professor,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Professor removido com sucesso!")
    else:
        print("ID do professor não encontrado.")

# Menu de opções
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar professor")
        print("2. Listar professores")
        print("3. Remover professor")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_professor()
        elif opcao == "2":
            listar_professores()
        elif opcao == "3":
            remover_professor()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executando o menu
menu()

# Fechando a conexão com o banco de dados
conn.close()