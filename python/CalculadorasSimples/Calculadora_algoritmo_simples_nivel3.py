

def mostrar_menu():
    print("\n--- MENU DE OPERAÇÕES ---")
    print("1: Soma | 2: Subtração | 3: Multiplicação | 4: Divisão")

def obter_escolha():
    while True:
        try:
        
            op = int(input("Escolha uma opção (1-4): "))
            if op < 1 or op > 4:
                print("Erro: Opção inválida! Escolha entre 1 e 4.")
            else:
                return op 
        except ValueError:
            print("Erro: Digite apenas o número da opção.")

def calcular():
    mostrar_menu()
    opcao = obter_escolha() 
    
    try:
        n1 = float(input("Informe o primeiro número: "))
        n2 = float(input("Informe o segundo número: "))

        if opcao == 1:   print(f" Resultado: {n1 + n2}")
        elif opcao == 2: print(f" Resultado: {n1 - n2}")
        elif opcao == 3: print(f" Resultado: {n1 * n2}")
        elif opcao == 4: print(f" Resultado: {n1 / n2}")

    except ZeroDivisionError:
        print(" Erro: Não existe divisão por zero.")
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")


calcular()

