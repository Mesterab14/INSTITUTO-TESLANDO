import math

try:
    numero_inicial = float(input("Digite o número inicial: ").replace(",", "."))
    numero_final = float(input("Digite o número final: ").replace(",", "."))
    incremento = float(
        input("Digite de quantos em quantos números: ").replace(",", ".")
    )

    if incremento <= 0:
        print("O incremento deve ser maior que zero.")

    elif numero_inicial > numero_final:
        numero_atual = numero_inicial
        while numero_atual >= numero_final and not math.isclose(numero_atual, numero_final):
            print(f"{numero_atual:g}")
            numero_atual -= incremento
            
    else:
        numero_atual = numero_inicial

        while numero_atual <= numero_final or math.isclose(
            numero_atual, numero_final
        ):
            print(f"{numero_atual:g}")
            numero_atual += incremento
except ValueError:
    print("Digite apenas números válidos.")
except EOFError:
    print("Nenhum valor foi informado.")