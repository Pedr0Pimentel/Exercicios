import math
inteiro=int(input('Digite um número inteiro: '))
print('[ 1 ] Para converter para BINÁRIO \n[ 2 ] Para converter para OCTAL \n[ 3 ] Para converter para HEXADECIMAL')
action=str(input('Sua opção:'))
if action == '1':
    binario=bin(inteiro)
    print('{} convertido para binário é igual a {}'.format(inteiro,binario[2:]))
elif action == '2':
    octal=oct(inteiro)
    print('{} convertido para octal é igual a {}'.format(inteiro,octal[2:]))
elif action == '3':
    hexadecimal=hex(inteiro)
    print('{} convertido para hexadecimal é igual a {}'.format(inteiro,hexadecimal[2:]))
else:
    print('Por favor, escolha uma opção válida')