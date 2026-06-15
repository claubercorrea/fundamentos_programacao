
class Calculadora:
    def __init__(self):
        pass
    def soma(self, primeiroNumero, segundoNumero):
        return primeiroNumero + segundoNumero
    
    def subtracao(self, primeiroNumero, segundoNumero):
        return primeiroNumero - segundoNumero
    
    def multiplicacao(self, primeiroNumero, segundoNumero):
        return primeiroNumero * segundoNumero
    
    def divisao(self, primeiroNumero, segundoNumero):
        if  segundoNumero ==0:
            raise ZeroDivisionError("não existe divião de zero")
        return primeiroNumero / segundoNumero
    def porcentagem(self, primeiroNumero, segundoNumero):
        return (primeiroNumero * segundoNumero) /100
class InterfaceCalculadora:
    def __init__(self):
        self.calc = Calculadora()
    def mostra_menu(self):
        print("escolha uma das opções  a baixo: ")
        print("1: Soma") 
        print("2: Subtração") 
        print("3: Multiplicação") 
        print("4: Divisão") 
        print("5: Porcentagem")
    def obter_escolha(self):
        escolha = [1,2,3,4,5] 
        while True:
            try:
                opcao = int(input("Escolha uma opção de  1 - 5"))
                if opcao not in escolha:
                    print("opção invalida tente novamente:") 
                    continue
                return opcao
            except ValueError:
                print("Erro: Opção não encontrada")
    def executar(self):
        while True:
            self.mostra_menu()
            opcao = self.obter_escolha()
            if opcao == 0:
                print("Encerrado... até mais ")
                break
            try:
                
                primeiroNumero = float(input("Informe  o primero número"))
                segundoNumero  =  float(input("Informe o segundo número"))
                
                print("_" * 30)
                if opcao == 1:   print(f"O resultado da soma       : {self.calc.soma(primeiroNumero, segundoNumero)}")
                elif opcao == 2: print(f"O resultado da subtração  : {self.calc.subtracao(primeiroNumero, segundoNumero)}")
                elif opcao == 3: print(f"O resultado da subtração  : {self.calc.multiplicacao(primeiroNumero, segundoNumero)}")
                elif opcao == 4: print(f"O resultado da divisão    : {self.calc.divisao(primeiroNumero, segundoNumero)}")
                elif opcao == 5: print(f"O resultado da porcentagem:{self.calc.porcentagem(primeiroNumero, segundoNumero)}")
                print("_" * 30)
                
            except ZeroDivisionError as e:
                print(f"Erro: {e}")
            except ValueError:
                print("Erro: Informe apenas valores numericos para calculo. ")
if __name__=="__main__":
    programa = InterfaceCalculadora()
    programa.executar()