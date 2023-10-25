import sqlite3


def criar_tabela():
  conn = sqlite3.connect('funcionario.db')
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL
  )
  ''')
  conn.commit()
  conn.close() 

def criar_funcionario(nome, cargo, salario):
  conn = sqlite3.connect('funcionario.db')
  cursor = conn.cursor()
  cursor.execute('''INSERT INTO funcionario (nome, cargo, salario) VALUES (?, ?, ?)''', (nome, cargo, salario))
  conn.commit()
  conn.close()

def listar_funcionario():
  conn = sqlite3.connect('funcionario.db')
  cursor = conn.cursor()
  cursor.execute('''SELECT * FROM funcionario''')
  funcionario = cursor.fetchall()
  if  len(funcionario) > 0:
    print("Lista dos Funcionarios")
    for funcionario in funcionario:
      print(f"ID: {funcionario[0]}")
      print(f"Nome: {funcionario[1]}")
      print(f"Cargo: {funcionario[2]}")
      print(f"Salario: {funcionario[3]}")
  else:
    print('Não há funcionários cadastrados')
      
  conn.commit()
  conn.close()
  
def atualizar_funcionario(funcionario_id, nome, cargo, salario):
  conn = sqlite3.connect('funcionario.db')
  cursor = conn.cursor()
  cursor.execute('''UPDATE funcionario SET nome = ?, cargo = ?, salario = ?
  WHERE id =?''',(nome, cargo, salario, funcionario_id))
  conn.commit()
  conn.close()

def excluir_funcionario(funcionario_id):
  conn = sqlite3.connect('funcionario.db')
  cursor = conn.cursor()
  cursor.execute('''DELETE FROM funcionario WHERE id = ?''', (funcionario_id,))
  conn.commit()
  conn.close()


criar_tabela()

criar_funcionario('João', 'Gerente', 4000)
criar_funcionario('Maria', 'Analista', 3000)

print("Listar Funcionários após a criação:\n")
listar_funcionario()

atualizar_funcionario(1, 'João', 'Gerente', 4400)

print("\nListar Funcionários após a atualização:\n")
listar_funcionario()

excluir_funcionario(2)
print("\nListar Funcionários após a exclusão:\n")
listar_funcionario()

print("\n-----------------------------------------\n")

def menu():
  print("1 - Criar Funcionário")
  print("2 - Listar Funcionários")
  print("3 - Atualizar Funcionário")
  print("4 - Excluir Funcionário")
  print("0 - Sair")
  opcao = int(input("Digite a opção desejada: "))
  return opcao

def main():
  criar_tabela()
  while True:
    opcao = menu()
    if opcao == 1:
      nome = input("Digite o nome do funcionário: ")
      cargo = input("Digite o cargo do funcionário: ")
      salario = float(input("Digite o salário do funcionário: "))
      criar_funcionario(nome, cargo, salario)
    elif opcao == 2:
      listar_funcionario()
      input("\nPressione ENTER para continuar...\n")
      os.system('clear')
      continue
    elif opcao == 3:
      funcionario_id = int(input("Digite o ID do funcionário: "))
      nome = input("Digite o nome do funcionário: ")
      cargo = input("Digite o cargo do funcionário: ")
      salario = float(input("Digite o salário do funcionário: "))
      atualizar_funcionario(funcionario_id, nome, cargo, salario)
    elif opcao == 4:
      funcionario_id = int(input("Digite o ID do funcionário: "))
      excluir_funcionario(funcionario_id)
    elif opcao == 0:
      print("Saindo...")
      break
    else:
      print("Opção inválida!")
      input("\nPressione ENTER para continuar...\n")
      os.system('clear')
      continue

if __name__ == '__main__':
  main()