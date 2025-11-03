#lados dos triângulos
a=int(input('Digite o lado A: '))
b=int(input('Digite o lado B: '))
c=int(input('Digite o lado C: '))

#condição de existência e verificação de tipo de triângulo
if a+b>c and a+c>b and b+c>a:
    if a==b and a==c:
     print('É um triângulo equilátero.')
    elif a==b!=c or b==c!=a or a==c!=b:
       print('É um triângulo isósceles.')
    else:
       print('É um triângulo escaleno.')
else:
   print('Esses lados não formam um triângulo.')
