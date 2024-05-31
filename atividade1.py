def soma(x, y):
    return x + y

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida."

def exibir_menu():
    print("Selecione a operação desejada:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

while True:
    exibir_menu()
    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha in ['1', '2', '3', '4']:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"O resultado da soma é: {soma(x, y)}")
        elif escolha == '2':
            print(f"O resultado da subtração é: {subtrai(x, y)}")
        elif escolha == '3':
            print(f"O resultado da multiplicação é: {multiplica(x, y)}")
        elif escolha == '4':
            print(f"O resultado da divisão é: {divide(x, y)}")
    elif escolha == '5':
        print("Saindo do programa...")
        break
    else:
        print("Escolha inválida. Por favor, selecione uma opção de 1 a 5.")

    print()  # Linha em branco para melhorar a legibilidade do menu