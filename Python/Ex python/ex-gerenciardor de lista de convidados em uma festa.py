convidados = ['Ana', 'Bruno']
capacidade_máxima = 5
nome_convidado = str(input('Qual o nome do seu convidado? '))
idade_convidado = int(input('Quantos anos {} tem?'.format(nome_convidado)))
if idade_convidado>=18:
    if len(convidados)<capacidade_máxima:
        convidados.append(nome_convidado)
        print('Bem-vindo {}, você foi adicionado a festa'.format(nome_convidado))
    else:
        print('Desculpe, {}. A lista de convidados já está cheia.'.format(nome_convidado))
else:
    print('Desculpe,{}, a festa é apenas para maiores de idade'.format(nome_convidado))
cond=str(input('Deseja removar o Bruno da festa? (s/n)'))
cond=cond.lower()
if cond == 's':
    convidados.remove('Bruno')
print('----Lista final da festa----')
print(convidados)

