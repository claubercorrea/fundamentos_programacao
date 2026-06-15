# 13) Escrever um algoritmo em C que leia três (3) números reais quaisquer e exiba o cubo da média deles 
# se está média estiver fora do intervalo fechado [10𝞥, 200𝞥]. Caso contrário, exiba a própria média. 
# Valor de 𝞥 (PHI = 11.52743: Use 5 casas decimais: ":5"
# import math

# try:
#   n1 = int(input('informe o 1° numero: '))
#   n2 = int(input('informe o 2° numero: '))
#   n3 = int(input('informe o 3° numero: '))
  
#   media =  (n1+n2+n3) / 3
#   limiteInferior = 10*math.pi
#   limite_superior = 200*math
#   if media <  limiteInferior or media >  limite_superior:
#       resultado = math.pow(media, 3)
#       print(f'media fora do intervalo fora do  cubo{resultado:.5f}')
      
#   else:
#     print(f'media dentro do intervalo {media:.5f}')
# except Exception as e:

#   print('erro', e)

import math
try:
  n1 = int(input('informe o 1° numero: '))
  n2 = int(input('informe o 2° numero: '))
  n3 = int(input('informe o 3° numero: '))

  media =  (n1+n2+n3) / 3
  if media <10 or media >200:
    media  = math.pi
    print(f'media fora do parametro {media:.5f}')
  else:
     print(f'media dentro do paramentro {media:.5f}')
except Exception as e:
  print(' erro', e )