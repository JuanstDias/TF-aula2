inventario = {}

def adicionar_produto(nome, preco, quantidade):
    inventario[nome] = {'preco': preco, 'quantidade': quantidade}
    print(f"Produto {nome} adicionado com sucesso!")

def remover_produto(nome):
    if nome in inventario:
        del inventario[nome]
        print(f"Produto {nome} removido com sucesso!")
    else:
        print(f"Produto {nome} não encontrado no inventário.")

def listar_produtos():
    if inventario:
        print("Inventário de Produtos:")
        for nome, detalhes in inventario.items():
            print(f"Nome: {nome}, Preço: R${detalhes['preco']:.2f}, Quantidade: {detalhes['quantidade']}")
    else:
        print("O inventário está vazio.")

def main():
    while True:
        print("\n1. Adicionar Produto\n2. Remover Produto\n3. Listar Produtos\n4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Produto: ")
            preco = float(input("Preço do Produto: "))
            quantidade = int(input("Quantidade do Produto: "))
            adicionar_produto(nome, preco, quantidade)
        elif opcao == '2':
            nome = input("Nome do Produto a ser removido: ")
            remover_produto(nome)
        elif opcao == '3':
            listar_produtos()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
