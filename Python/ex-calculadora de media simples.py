x = float(input('Por favor, digite a primeira nota: '))
y = float(input('Por favor, digite a segunda nota: '))
z = float(input('Por favor, digite a terceira nota: '))
media=round(((x+y+z)/3),2)
print('A média das notas {},{} e {} é igual a {}'.format(x,y,z,media))
if media>= 7:
    print('Situação: Aprovado')
elif media>=5:
    print('Situação: Recuperação')
else:
    print('Situação: Reprovado')