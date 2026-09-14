#LS, CAT, ECHO, TEE e RM

import os


# ls
def ls():
    print("\n--- Conteúdo da pasta atual ---")
    try:
        for item in os.listdir("."):
            if os.path.isdir(item):
                print(f"[PASTA]   {item}")
            else:
                print(f"[ARQUIVO] {item}")
    except Exception as e:
        print(f"Erro ao listar pasta atual: {e}")

    caminho = input(
        "\nDigite o caminho de outra pasta (ou aperte ENTER para manter a atual): "
    )

    if caminho.strip() == "":
        caminho = "."

    try:
        itens = os.listdir(caminho)
        print(f"\n--- Conteúdo de '{caminho}' ---")
        for item in itens:
            # olha se é pasta ou arquivo
            if os.path.isdir(os.path.join(caminho, item)):
                print(f"[PASTA]   {item}")
            else:
                print(f"[ARQUIVO] {item}")

        resposta = (
            input("\nDeseja ler algum arquivo listado agora? (s/n): ")
            .strip()
            .lower()

        #vai pro cat
        )
        if resposta == "s":
            cat(diretorio=caminho)

        #outra coisa

    except FileNotFoundError:
        print("\nEssa pasta não existe!")
    except PermissionError:
        print("\nSem permissão para acessar a pasta!")


# cat
def cat(diretorio="."):
    print(f"\n--- Arquivos disponíveis para leitura em '{diretorio}' ---")
    arquivos_encontrados = False
    try:
        for item in os.listdir(diretorio):
            caminho_item = os.path.join(diretorio, item)
            if os.path.isfile(caminho_item):
                print(f" - {item}")
                arquivos_encontrados = True

        if not arquivos_encontrados:
            print(" (Nenhum arquivo encontrado)")
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")

    arquivo = input("\nDigite o nome/caminho do arquivo para ler: ")

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
            print("\nConteúdo do Arquivo:\n")
            print(conteudo)
            print("\n---------------------------")
    except FileNotFoundError:
        print("\nArquivo não encontrado!")
    except IsADirectoryError:
        print("\nO caminho informado é uma pasta, não um arquivo.")


# echo
def echo():
    texto = input("\nDigite o texto que deseja exibir: ")
    print("\n" + texto)


# tee
def tee():
    arquivo = input("\nDigite o nome do arquivo para salvar: ")
    modo = (
        input(
            "Se deseja apagar o conteúdo e escrever algo novo digite S e se deseja adicionar texto digite A: "
        )
        .strip()
        .lower()
    )

    if modo == "s":
        tipo_abertura = "w"
    else:
        tipo_abertura = "a"

    texto = input("Digite o texto a ser gravado: ")

    try:
        with open(arquivo, tipo_abertura, encoding="utf-8") as f:
            f.write(texto + "\n")

        print("\n[Saída do Tee]: " + texto)
        print(f"Texto gravado com sucesso no arquivo '{arquivo}'!")
        
    except Exception as e:
        print(f"\nErro ao escrever no arquivo: {e}")

# rm
def rm():
    caminho = input("\nDigite o nome/caminho do arquivo ou pasta a ser removido: ").strip()

    if not caminho:
        print("\nCaminho inválido!")
        return

    try:
        if os.path.isfile(caminho):
            confirmacao = input(f"Tem certeza que deseja apagar o arquivo '{caminho}'? (s/n): ").strip().lower()
            if confirmacao == "s":
                os.remove(caminho)
                print(f"\nArquivo '{caminho}' removido com sucesso!")
            else:
                print("\nOperação cancelada.")
                
        elif os.path.isdir(caminho):
            confirmacao = input(f"Tem certeza que deseja apagar a pasta vazia '{caminho}'? (s/n): ").strip().lower()
            if confirmacao == "s":
                os.rmdir(caminho)
                print(f"\nPasta '{caminho}' removida com sucesso!")
            else:
                print("\nOperação cancelada.")
                
        else:
            print("\nO caminho especificado não existe!")

    except PermissionError:
        print("\nSem permissão para remover este arquivo ou pasta!")


# codigo inteiro
def menu():

    while True:
        print("\n   COMANDOS DO TERMINAL\n   ")
        print("1. Listar arquivos e pastas (ls)")
        print("2. Ler conteúdo de um arquivo (cat)")
        print("3. Imprimir texto na tela (echo)")
        print("4. Gravar texto em arquivo e exibir (tee)")
        print("5. Remover arquivo ou pasta (rm)")
        print("6. Sair")

        opcao = input("\nEscolha uma opção (1-6): ")

        if opcao == "1":
            ls()
        elif opcao == "2":
            cat()
        elif opcao == "3":
            echo()
        elif opcao == "4":
            tee()
        elif opcao == "5":
            rm()
        elif opcao == "6":
            break
        else:
            print("\nOpção inválida! Escolha um número de 1 a 6.")

menu()