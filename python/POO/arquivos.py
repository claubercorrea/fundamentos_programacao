print('Informe os dados de cada contato para gravação')
print('deixe em branco para parar')
arq = open('contato.text','w')
while True:
    contato = input('contato: ')
    if contato=='':
        break
    arq.write(contato+'\n')
    arq.close()
    
    print('contatos cadastrados:')
    arq= open('contatos.text')
    linhas = arq.readlines()
    for contato in linhas:
        print(contato.strip())
arq.close()
print('_'*50)
arq= open('contatos.text')
print(arq.read().strip())
arq.close()
import os 
if not os.path.ifile('contato.text'):
    print('Arquivo não encontrado ')

else:
    print('contatos cadastrados: ')
    arq = open('contatos.text')
    linhas = arq.readlines()
    for contato in linhas>
    print(contato.strip())
    arq.close()
