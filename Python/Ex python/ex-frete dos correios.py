print('Olá, bom dia')
peso=float(input('Qual o peso da carta que você deseja enviar? Em gramas por favor '))
if peso>200:
    print('Peso excedido. Envio por pacote recomendado')
elif peso>100:
    print('O custo de envio da sua carta será de R$4,00')
elif peso>50:
    print('O custo de envio da sua carta será de R$2,50')
else:
    print('O custo de envio da sua carta será de R$1,50')

