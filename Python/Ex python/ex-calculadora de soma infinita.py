soma_total=0
num_usados=0
while True:
    num=int(input('Digite um número (ou 0 para encerrar a soma): '))
    if num==0:
        num_usados=num_usados+1
        break
    elif num!=0:
        soma_total=soma_total+num
        num_usados=num_usados+1
print('A soma total de todos os números é igual a {}'.format(soma_total))
media=float((soma_total/num_usados))
print('A média é igual a {}'.format(round(media,2)))