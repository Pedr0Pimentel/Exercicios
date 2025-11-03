
num = [10,-5,0,22,-1,3,0,-8]
positivo=[]
negativo=[]
zeros=[]
print('Estes são os númeos não tratados {}'.format(num))
for numero in num:
    if numero > 0:
        positivo.append(numero)
    elif numero < 0:
        negativo.append(numero)
    else:
        zeros.append(numero)
print('Estes são os números tratados {},{} e {}'.format(positivo, negativo, zeros))

