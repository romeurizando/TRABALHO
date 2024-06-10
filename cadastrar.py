import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

# Criar tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

def cadastrar_produto(nome, preco, quantidade):
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO produto (nome, preco, quantidade)
    VALUES (?, ?, ?)
    ''', (nome, preco, quantidade))
    
    conn.commit()
    conn.close()
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM produto')
    produtos = cursor.fetchall()
    
    for produto in produtos:
        preco_formatado = f"R${produto[2]:.2f}"
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: R${preco_formatado}, Quantidade: {produto[3]}")
    
    conn.close()

def atualizar_produto(id, nome, preco, quantidade):
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE produto
    SET nome = ?, preco = ?, quantidade = ?
    WHERE id = ?
    ''', (nome, preco, quantidade, id))
    
    conn.commit()
    conn.close()
    print("Produto atualizado com sucesso!")

def deletar_produto(id):
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM produto WHERE id = ?', (id,))
    
    conn.commit()
    conn.close()
    print("Produto deletado com sucesso!")

def menu():
    while True:
        print("\nSistema de Cadastro de Produtos")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Atualizar produto")
        print("4. Deletar produto")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            cadastrar_produto(nome, preco, quantidade)
        
        elif opcao == '2':
            listar_produtos()
        
        elif opcao == '3':
            id = int(input("ID do produto a ser atualizado: "))
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            atualizar_produto(id, nome, preco, quantidade)
        
        elif opcao == '4':
            id = int(input("ID do produto a ser deletado: "))
            deletar_produto(id)
        
        elif opcao == '5':
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()