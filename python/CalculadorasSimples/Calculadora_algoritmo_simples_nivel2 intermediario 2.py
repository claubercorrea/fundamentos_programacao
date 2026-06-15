try:

    print("EScolha uma  das opções abaixo: ")
    print("Adição : + ")
    print("Subtração : - ")
    print("Multiplicação: * ")    
    print("Divisão : /")
    print("porcentagem: %")
    
    operacao     = input("Digite o simbolo do operador: ")
    numero_um    = float(input("Informe o primeiro Número: ")) 
    numero_dois  = float(input("Informe o segundo Número: "))
        
    if(operacao !="+" and operacao !="-" and operacao !="*" and operacao !="/" and operacao !="%"):
        print(" Erro: Operação invalida:")
    else:
        if(operacao =="+"):
            soma      = numero_um + numero_dois
            print(f"Resultado da Subtração: {soma:.2f}")
            
        elif(operacao =="-"):
            subtracao = numero_um - numero_dois
            print(f"Resultado da Subtração: {subtracao:.2f}")
            
        elif(operacao =="/"):
            divisao   = numero_um /numero_dois
            print(f"Resultado da Divisão: {divisao:.2f}")
                    
        elif(operacao =="%"):
            porcentagem   = (numero_um * numero_dois) / 100
            print(f"Resultado da Porcentagem: {porcentagem:.2f}")
        else:
            print(" Erro: Operação invalida renicie e tente novamente: ")
except ValueError:
    print(" Erro: Só aceita valores númericos")
except ZeroDivisionError:
    print(" Erro: Não existe divisão por zero")