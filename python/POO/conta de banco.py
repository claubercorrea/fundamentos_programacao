class Cliente:
    def __init__(self,nome,endereco):
        self._nome = nome
        self._endereco = endereco
    def imprime(self):
        print('Cliente:', self._nome, '(',type(self),')','\nEndereco:', self._endereco)

class ClientePF(Cliente):
    def __init__(self,nome,endereco,cpf,nascimento):
        super().__init__(nome,endereco)
        self._cpf = cpf
        self._nascimento = nascimento
    def imprime(self):
        print(self._nome, '\nCPF' +self._cpf,'\nNascimento' + self._nascimento)
class ClientePJ(Cliente):
    def __init__(self,nome,endereco,cnpj):
        super().__init__(nome,endereco)
        self._cnpj = cnpj
    def imprime(self):
        print(self._nome,'\nCNPJ:' +self._cnpj)
class conta:
    _quant = 0
    @classmethod 
    def adiciona_conta(cls):
        cls._quant+=1
    @classmethod
    def quantidade(cls):
        return cls._quant
    
    def __init__(self,numero,cliente):
        self.adiciona_conta()
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
    def imprime(self):
        print('Conta: ', str(self._numero),'\nSaldo:',str(self._saldo))
        self._cliente.imprime()
    def depositar(self,valor):
        self._saldo += valor
    def saldo(self):
        return self._saldo
    def sacar(self,valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False
    def tranferir(self,destino,valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False
class ContaInvestimento(conta):
    def depositar(self,valor):
        self._saldo += valor * 1.01
print('-----------conta1---------------')

cliente = ClientePF('Ana',' Rua Um','xxxxx.xxxx.xxxx.zz','1985-05-10')
conta1 =  conta(1111,cliente)
cliente = ClientePJ('Loja X','Parça central','xx.xxx.xxx/yyyy-zz')

print('Contas criadas: ', conta.quantidade())
print('conta1: ', conta1.saldo())
conta1.depositar(1000.00)
print('conta1 saldo: ', conta1.saldo())
print('\n-----------conta2---------------')
conta2 = conta(22222,cliente)
print('contas criadas:', conta.quantidade())
conta2.depositar(2000.00)
print('conta2 saldo: ', conta2.saldo())
 
print('\n-----------conta1-sacar---------------')
conta1.sacar(100)
print('conta1.saldo atual de  R$: ', conta1.saldo())

print('\n-----------sacar conta2---------------')
conta2.sacar(200)
print('conta2 saldo atual', conta2.saldo())

print('\n-----------Conta1-tranferencia---------------')

conta1.tranferir(conta2,100)
print('saldo atual após a tranferencia R$:', conta1.saldo())

print('\n-----------Conta2-tranferencia---------------')
conta2.tranferir(conta1,200)
print('saldo atual após a transferencia R$: ', conta2.saldo())
conta1.imprime()
print('')
conta2.imprime()