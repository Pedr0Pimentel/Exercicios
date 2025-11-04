from random import randint
tentativas = 0
num=int(input('Faça um palpite de um número entre 1 e 10: '))
num_aleatorio= randint(1,10)
while num != num_aleatorio:
    if num>num_aleatorio:
        print('Número muito alto, tente um menor!')
    else:
        print('Número muito baixo, tente um maior!')
    tentativas=tentativas+1
    print('Está é a sua tentativa de número {}. Tente novamente!'.format(tentativas))
    num=int(input('Faça um palpite de um número entre 1 e 10: '))
tentativas=tentativas+1
print('Parabéns, você acertou. O número era {}, você conseguiu na tentativa de número {}'.format(num,tentativas))