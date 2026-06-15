try:

    numero_um = float(input("Informe o primeiro Número: ")) 
    numero_dois = float(input("Informe o segundo Número: ")) 
    
    soma          =  numero_um +  numero_dois
    subtracao     = numero_um - numero_dois
    multiplicacao = numero_um * numero_dois
    divisao       =  numero_um / numero_dois
    porcentagem   = (numero_um * numero_dois) / 100
        
    print(f'Resultado da soma:          {soma:.2f}')
    print(f'Resultado da subtração:     {subtracao:.2f}')
    print(f'Resultado da multiplicação: {multiplicacao:.2f}')
    print(f'Resultado da divisão:       {divisao:.2f}')
    print(f'Resultado da porcentagem:   {porcentagem:.2f}')
except ValueError:
    print("Erro: Só aceita valores númericos")
except ZeroDivisionError:
    print("Erro: Não existe divisor por zero")
    
    
    
    
