import sqlite3

conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS cadastro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo TEXT NOT NULL,
    email TEXT NOT NULL,
    celular TEXT NOT NULL,
    cpf TEXT NOT NULL
)
''')

conn.commit()
conn.close()

def cadastrar_pessoa(nome_completo, email, celular, cpf):
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO cadastro (nome_completo, email, celular, cpf)
    VALUES (?, ?, ?, ?)
    ''', (nome_completo, email, celular, cpf))
    
    conn.commit()
    conn.close()
    print("Pessoa cadastrada com sucesso!")

def listar_pessoas():
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM cadastro')
    pessoas = cursor.fetchall()
    
    for pessoa in pessoas:
        print(f"ID: {pessoa[0]}, Nome Completo: {pessoa[1]}, E-mail: {pessoa[2]}, Celular: {pessoa[3]}, CPF: {pessoa[4]}")
    
    conn.close()

def atualizar_pessoa(id, nome_completo, email, celular, cpf):
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE cadastro
    SET nome_completo = ?, email = ?, celular = ?, cpf = ?
    WHERE id = ?
    ''', (nome_completo, email, celular, cpf, id))
    
    conn.commit()
    conn.close()
    print("Pessoa atualizada com sucesso!")

def deletar_pessoa(id):
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM cadastro WHERE id = ?', (id,))
    
    conn.commit()
    conn.close()
    print("Pessoa deletada com sucesso!")

def menu():
    while True:
        print("\nSistema de Cadastro de Pessoas")
        print("1. Cadastrar pessoa")
        print("2. Listar pessoas")
        print("3. Atualizar pessoa")
        print("4. Deletar pessoa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome_completo = input("Nome Completo: ")
            email = input("E-mail: ")
            celular = input("Celular: ")
            cpf = input("CPF: ")
            cadastrar_pessoa(nome_completo, email, celular, cpf)
        
        elif opcao == '2':
            listar_pessoas()
        
        elif opcao == '3':
            id = int(input("ID da pessoa a ser atualizada: "))
            nome_completo = input("Nome Completo: ")
            email = input("E-mail: ")
            celular = input("Celular: ")
            cpf = input("CPF: ")
            atualizar_pessoa(id, nome_completo, email, celular, cpf)
        
        elif opcao == '4':
            id = int(input("ID da pessoa a ser deletada: "))
            deletar_pessoa(id)
        
        elif opcao == '5':
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()