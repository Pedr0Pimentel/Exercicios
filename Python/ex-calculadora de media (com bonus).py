notas_originais = [8.5, 9.5, 10.0, 7.0, 9.0, 6.5]
novas_notas = []
for nota in notas_originais:
    if nota <=9.5 and nota>=9.0:
        nota = nota + 0.5
        novas_notas.append(nota)
    else:
        novas_notas.append(nota)
print(novas_notas)
print('A média das notas da turma com o bônus é: {}'.format(round((sum(novas_notas)/(len(novas_notas))),2)))
