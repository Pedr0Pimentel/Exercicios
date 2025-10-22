valor_home=float(input('Valor do imóvel: '))
salario=float(input('Salário do comprador: '))
time=int(input('Quantos anos de financiamento: '))
custo_mensal=valor_home/float(time*12)
trinta_por_cento_do_salario=float((salario/10)*3)
print('Para pagar uma casa de R${} em {} anos a prestação será de R${}'.format(valor_home,time,round(custo_mensal,2)))
if custo_mensal>trinta_por_cento_do_salario:
    print('EMPRÉSTIMO NEGADO')
else:
    print('Empréstimo pode ser CONSEDIDO')