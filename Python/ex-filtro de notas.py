def filtrar_aprovados(lista_de_notas):
    aprovados=[]
    for nota in lista_de_notas:
        if nota >=7:
            aprovados.append(nota)
    return aprovados


notas_originais=[8.5,4.0,10,6.5,7]
print(listaA)
lista_filtrada = filtrar_aprovados(listaA)
print(lista_filtrada)