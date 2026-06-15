# 11) Escrever um algoritmo que leia de apenas um (1) veículo de um estacionamento do shopping: 
# ➢ Hora de Entrada: formato HH:MM 
# ➢ Hora de Saída: formato HH:MM 
# ➢ Valor pago a cada 30 Minutos: R$__?__ / 30 Minutos; 
# E, exiba na tela o Total a Pagar (R$), levando em consideração: 
# ➢ Tolerância: Carência gratuita de 30 Minutos. 
# ➢ Considerar que o veículo não permutará no shopping. (Tempo de permanência ≤ 24 Horas)  
from datetime import datetime
total_minutos = 0
try:
    valor_tempo = float(input('informe o valor de 30 minuto'))
    entrada_do_estacionamento = input('Hora de Entrada: (HH:MM):  ')
    saida_do_estacionamento = input('Hora de Entrada: (HH:MM):  ')
    
    formato = "%H:%M"
    h_entrada =datetime.strptime(entrada_do_estacionamento,formato)
    h_saida = datetime.strptime(saida_do_estacionamento, formato)

    diferenca = h_entrada - h_saida
    total_minutos += diferenca .total_seconds() / 60

    if total_minutos < 0:
        total_minutos = 1400
    if   total_minutos  <=30:
        print('insento de pagar o valor')
    bloco_de_30 = total_minutos //30
    if total_minutos %30 >0:
        bloco_de_30+=1
    total_pagar =  bloco_de_30 * valor_tempo
    print(f'valor a pagar {total_pagar:.2f} R$:')   
except Exception as e:
    print(f'invalido {e}')
