n1=float(input('Digite o primeiro número: '))
n2=float(input('Digite o segundo número: '))
ope=input('Escolha a operação desejada (+,-,/,*): ')
if ope== '+':
    x = n1 + n2
    print('Resultado: {} + {} = {}'.format(n1, n2,x))
elif ope== '-':
    x = n1 - n2
    print('Resultado: {} - {} = {}'.format(n1,n2,x))
elif ope== '*':
    x = n1 * n2 
    print('Resultado: {} * {} = {} ' .format(n1,n2,x))
elif ope== '/':
    if  n2 == 0:
        print('Erro, divisão por 0')
    else:
        x = n1 / n2
        print('Resultado: {} / {} = {}'.format(n1,n2,x))
else:
    print('Erro! Digite uma operação dentre as permititidas: +, -, *, /')