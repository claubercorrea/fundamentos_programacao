def menu():
    print("escolha uma das opções  a baixo: ")
    print("Escolha uma das opções abaixo: ") 
    print("1: Soma") 
    print("2: Subtração") 
    print("3: Multiplicação") 
    print("4: Divisão") 
    print("5: Porcentagem")


def opera():
    escolha = [1,2,3,4,5]
    while True:
        try:
            opcao = int (input("escolha uma das opções a cima: "))
            if opcao not in escolha:
                print("Erro: opção invalida tente novamente: ")
            
                continue
            return opcao
        except ValueError:
            print("Erro: so aceita opcoes numericas descrita no menu")
        except Exception as e:
            print(f"erro {e}")
        
def calcular():
    menu()
    opcao = opera()
    if  opcao is None:return
    try:
        f'{opera}'
        n1 = float(input("Informe o primeiro numero: "))
        n2 = float (input("Informe o segundo numero: "))
        if opcao   == 1: print(f'soma =       {n1+n2}')
        elif opcao == 2: print(f'subtração     {n1-n2}')
        elif opcao == 3: print(f'multiplicação {n1*n2}')
        elif opcao == 4: print(f'Divisão       {n1/n2:.2f}')
        elif opcao == 5: print(f'porcentagem   {(n1*n2) / 100:.2f}')  
    except ValueError:
        print('Erro operação invalida')
    except ZeroDivisionError:
        print("Erro: É impossivel fazer divisão por zero")
    except Exception as e:
        print(f" Erro: Erro Inesperado {e}")
while True:
    
    calcular()  
    continuar = input("Deseja realizar outra operacao matamatica s/n ").lower()
    if continuar != "s":
        print("Encerrado até logo! ")
        break
        