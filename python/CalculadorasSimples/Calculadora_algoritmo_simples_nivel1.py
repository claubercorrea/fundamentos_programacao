
try:
    numero_um = float(input("Informe o primeiro Número: ")) 
    numero_dois = float(input("Informe o primeiro Número: ")) # <--ERRO DE INICIANTE
    
    adicao = numero_um+numero_dois
    subtracao =  numero_um-numero_dois
    multiplicacao = numero_um*numero_dois
    divisao = numero_um/numero_dois
    porcentagem = (numero_um*numero_dois)/100  

    
    print("Adicão: ",adicao)
    print("Subtracão: ",subtracao)
    print("Multiplicacao: ",multiplicacao)
    print("divisão: ", divisao)
    print("Porcentagem: ", porcentagem)
except Exception as e:
    print("Erro: Dados Invalidos")