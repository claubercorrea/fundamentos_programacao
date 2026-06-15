class Produto:
    def __init__(self, descricao, preco):
        self._descricao = descricao
        self._preco = preco

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):
        self._descricao = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        self._preco = valor

    def __str__(self):
        return f'{self._descricao} (${self._preco:0.2f})'

class ProdutoEstoque(Produto):
    def __init__(self, descricao, preco):
        super().__init__(descricao, preco)
        self._estoque = 0.0

    def entrada(self, quantidade):
        self._estoque += quantidade

    def saida(self, quantidade):
        if quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        return False

    def __str__(self):
        texto = super().__str__()
        return f'{texto}, Estoque: {self._estoque:0.3f}'

class ProdutoVenda(Produto):
    def __init__(self, descricao, preco, quantidade):
        super().__init__(descricao, preco)
        self._quantidade = quantidade 

    @property
    def total(self):
        return self._quantidade * self._preco

    def __str__(self):
        texto = super().__str__()
        return f'{texto}, Qtde: {self._quantidade:0.3f}, Total: ${self.total:0.2f}'

class Venda:
    def __init__(self):
        self._produtos = []
        self._total = 0.0

    @property
    def total(self):
        return self._total

    @property
    def numero_produtos(self):
        return len(self._produtos)
    
    def adiciona_produto(self, produto):
        self._produtos.append(produto)
        self._total += produto.total

    def __str__(self):
        texto = '\n' + '-'*50
        texto += '\nProdutos:'
        for produto in self._produtos:
            texto += f'\n{produto}'
        texto += '\n' + '-'*50
        texto += f'\nTotal da venda: ${self._total:0.2f}'
        texto += '\n' + '-'*50
        return texto

# Funções auxiliares movidas para fora das classes ou tratadas como estáticas
def pergunta(mensagem, tipo=int):
    while True:
        try:
            resp = input(mensagem)
            return tipo(resp)
        except ValueError:
            print('Valor inválido! Informe novamente.')

def confirma(mensagem, resposta_esperada):
    texto = input(mensagem).strip()
    return texto.lower() == resposta_esperada.lower()

class Caixa:
    def __init__(self):
        self._produtos = {}
        self._vendas = []

    def menu(self):
        print('\n' + '*' * 30)
        print('*' + ' ' * 8 + 'CAIXA' + ' ' * 13 + '*')
        print('*' * 30)
        print('(C) Cadastrar/Atualizar produto')
        print('(E) Entrada de estoque')
        print('(V) Vender')
        print('(R) Relatório de vendas')
        print('(S) Sair')
        return input('Informe sua opção: ').upper()

    def busca_produto(self):
        if not self._produtos:
            print('Nenhum produto cadastrado!')
            return None
        
        print('\nProdutos disponíveis:')
        for cod, produto in self._produtos.items():
            print(f'Código {cod}: {produto}')
        
        codigo = pergunta('Código do produto: ', int)
        return self._produtos.get(codigo)

    def cadastro_produto(self):
        codigo = pergunta('Informe o código para cadastrar/alterar: ', int)
        produto = self._produtos.get(codigo)

        if produto:
            print(f'Produto encontrado: {produto}')
            if confirma('Deseja alterar? (S/N): ', 'S'):
                desc, preco = self.dados_produtos()
                produto.descricao = desc
                produto.preco = preco
        else:
            if confirma('Produto não existe. Incluir? (S/N): ', 'S'):
                desc, preco = self.dados_produtos()
                novo_produto = ProdutoEstoque(desc, preco)
                self._produtos[codigo] = novo_produto

    def dados_produtos(self):
        print('\nInforme os dados:')
        descricao = input('Descrição: ')
        preco = pergunta('Preço: ', float)
        return descricao, preco

    def entrada_estoque(self):
        produto = self.busca_produto()
        if produto:
            qtd = pergunta('Quantidade')