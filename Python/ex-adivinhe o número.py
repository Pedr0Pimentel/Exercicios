from random import randint
x=randint(0,10)
y=int(input('Escolha um número de 0 a 10: '))

if y>=0 and y<=10:
    if y ==x:
        print('Parabéns, você acertou!')
    else:
        print('Você errou! O número era {}'.format(x))
else:
    print('Digite um algarismo válido.')
