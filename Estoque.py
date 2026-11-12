ativo = True
while ativo:
    produto = {"nome","qnt_caixa","quantidade"}
    categorias = ["CANECA","CAMISETA","CERAMICA","INSUMO"]
# MENU INICIAL
    print("---- SISTEMA DE ESTOQUE ----")
    print("1. Resgistro de mercadoria")
    print("2. Saida de mercadoria")
    print("3. Entrada de mercadoria")
    print("4. Checar estoque")
    print("5. Sair")
    menu = input("Selecione a opção desejada:" )

#RESGISTRAR NOVO ITEM
    print("Categorias:")
    print(categorias)
    menu_categoria = input("Selecione a categorias: ").upper()

    if menu_categoria in categorias:
        print (menu_categoria)
        nome = input("Digite o nome do Item: ").upper()

        #CHECAR SE JA EXISTE ITEM COM ESSE NOME
        with open(f"{menu_categoria}.txt","r") as ler:
            linhas = ler.readlines()
            for i in linhas:
                if i.strip().split(";")[0] == nome:
                    print("erro")
                    print("O item já esta registrado")
                    break
                
        qnt_caixa = int(input("Digite a quantidade de itens por caixa: "))
        quantidade = 0
        with open(f"{menu_categoria}.txt", "a") as arquivo_estoque:
            conteudo = f"{nome};{qnt_caixa};{quantidade}\n"
            arquivo_estoque.write(conteudo)
    else :
        print("Categoria Inexistente")
    break
#REGISTRAR ENTRADA


#REGISTRAR SAIDA


#CHECAR ESTOQUE
