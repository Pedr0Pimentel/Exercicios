from random import randint
x=randint(0,10)
y=int(input('Tentativa 1: Digite um número de 0 a 10: '))

if y>=0 and y<=10:
    if y==x:
        print('Parabéns! Você acertou.')
    else:
        print('Você errou!')
        if y>x:
            print('O número é menor.')
        else:
            print('O número é menor.')
        y=int(input('Tentativa 2: Digite um número de 0 a 10: '))
        if y>=0 and y<=10:
            if y==x:
              print('Parabéns! Você acertou.')
            else:
                print('Você errou!')
                if y>x:
                    print('O número é menor.')
                else:
                    print('O número é maior')
                y=int(input('Tentativa 3: Digite um número de 0 a 10: '))
                if y>=0 and y<=10:
                    if y==x:
                        print('Parabéns! Você acertou.')
                    else:
                        print('Você errou! O número era {}'.format(x))
else:
    print('Por favor, digite um número válido. (o a 10)')

     