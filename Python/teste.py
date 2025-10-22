notas = [8.5,4.0,10.0,6.5,7.0]
notas_aprovadas=[]
for nota in notas:
    if nota>=7.0:
        notas_aprovadas.append(nota)
print(notas_aprovadas)