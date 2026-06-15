# 14) Escrever um algoritmo que leia as notas entre [0, 10]: AV1, AV2 e PF e faltas: TF de um (1) aluno 
# da UVV, sendo que: 
# E; exiba na tela seus Resultados: Parciais e Final (STATUS: Aprovado, Prova Final, Reprovado por Falta ou Reprovado).

try:
    status=''
    faltas_semestrais =  int(input('informe quantas faltas em que o aluno tem: '))
    if faltas_semestrais < 0:
        print('informação invalida')
    elif faltas_semestrais > 15:
        status='reprovado'
    else:
        status='aprovado1'

        primeiro_Bimestre = float(input('informe  a nota do primeiro bimestre: '))
        segundo_Bimestre = float(input('informe  a nota do segundo bimestre: '))
        
        media_do_aluno = (primeiro_Bimestre + segundo_Bimestre)
        if media_do_aluno < 0 or media_do_aluno> 10:
            print('informação invalida')
        else:
            if media_do_aluno < 3:
                status='reprovado'
                print(f'valor da nota: {media_do_aluno:.2f} ')
            elif media_do_aluno  >= 7:
                status='aprovado'
                print(f'valor da nota: {media_do_aluno:.2f} ')
            else:
                prova_final = float(input('informe a nota da prova final'))
                if prova_final > 10:
                    print('informacao invalida')
                else:
                    if prova_final >=5:
                        status ='aprovado'
                        print(f'valor da nota final:  {prova_final:.2f}')
                    else:
                        status='reprovado '
                        print(f'valor da nota final:  {prova_final:.2f}')
    print(f'{status}')

except Exception as e:
    print(f'erro {e}')

