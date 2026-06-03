TIPOS_VALIDOS = {"int", "float", "string", "char", "bool"}

class TabelaDeSimbolos:
    def __init__(self):
        # Inicia a pilha já com o escopo global ativo
        self.escopos = [{}] 
        print("Escopo Global inicializado.")

    def entrar_escopo(self):
        self.escopos.append({})
        print("Novo escopo criado.")

    def declarar(self, variavel, tipo):

        # Verifica se existe escopo ativo
        if not self.escopos:
            print("Erro: nenhum escopo ativo.")
            return

        # Verifica se o nome é válido
        if not variavel.isidentifier():
            print("Erro: nome de variável inválido.")
            return

        # Verifica se o tipo existe
        if tipo not in TIPOS_VALIDOS:
            print(f"Erro: tipo '{tipo}' não é válido.")
            return

        escopo_atual = self.escopos[-1]

        # Verifica se já existe no mesmo escopo
        if variavel in escopo_atual:
            print(f"Erro: '{variavel}' já declarada neste escopo.")
            return

        escopo_atual[variavel] = tipo
        print(f"Declarada: {variavel} -> {tipo}")
    
    def buscar(self, variavel):
        for escopo in reversed(self.escopos):
            if variavel in escopo:
                return escopo[variavel]
        return None

    def mostrar(self):
        print("\nEscopos atuais:")
        for i, escopo in enumerate(self.escopos):
            print(f"Escopo {i}: {escopo}")
        print()

    def sair_escopo(self):
        # Garante que sempre restará pelo menos o escopo global (tamanho > 1)
        if len(self.escopos) > 1:
            self.escopos.pop()
            print("Escopo interno removido.")
        else:
            print("Erro: Não é possível remover o Escopo Global.")

tabela = TabelaDeSimbolos()

while True:
    print("\n=== MENU ===")
    print("1 - Adicionar  escopo")
    print("2 - Remover do escopo")
    print("3 - Declarar variável")
    print("4 - Buscar variável")
    print("5 - Mostrar tabela")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        tabela.entrar_escopo()

    elif opcao == "2":
        tabela.sair_escopo()

    elif opcao == "3":
        print("\nExemplos de nomes válidos:")
        print("x")
        print("idade")
        print("nome_cliente")
        print("_total")
        print("valor123")

        nome = input("\nNome da variável: ")
    
        print("\nTipos disponíveis:")
        print("int")
        print("float")
        print("string")
        print("char")
        print("bool")

        tipo = input("\nTipo da variável: ")

        tabela.declarar(nome, tipo)

    elif opcao == "4":
        nome = input("Variável a buscar: ")
        resultado = tabela.buscar(nome)

        if resultado:
            print(f"Tipo encontrado: {resultado}")
        else:
            print("Variável não encontrada.")

    elif opcao == "5":
        tabela.mostrar()

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")