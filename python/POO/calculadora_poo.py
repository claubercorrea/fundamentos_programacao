class CalculadoraSimples:
    def __init__(self):
        self.soma = 0
        self.subtracao = 0
        
class Calculo_entrada:
    def __init__ (self):
        
        self.n1=int(input('valor 1: 10'))
        self.n2=int(input('valor 2: '))
class Calculo_soma (CalculadoraSimples,Calculo_entrada):
    def __init__(self):
        CalculadoraSimples.__init__(self)
        Calculo_entrada.__init__(self)
        self.soma = self.n1+ self.n2
class Calculo_menos(CalculadoraSimples,Calculo_entrada):
    def __init__(self):
        CalculadoraSimples.__init__(self) 
        Calculo_entrada.__init__(self)
        try:
            self.subtracao = self.n1-self.n2
            if self.n2 < 0:
                print('valor invalido')
            
        except Exception as e:
            print(f'erro {e}') 
class Resultado_soma(Calculo_soma):
    def __init__(self):
        Calculo_soma.__init__(self)
        print(f'resultado da soma {self.soma}')
            
class Resultado_menos(Calculo_menos):
    def __init__(self):
        Calculo_menos.__init__(self)
        print(f'resultado da subtracação: {self.subtracao}')
        
Resultado_soma()
Resultado_menos()
    

