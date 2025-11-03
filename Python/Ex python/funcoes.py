def perigo():
    print('Cuidado, operação perigosa!!!')

def ceusius_para_fahrenheit(temp_ceusius):
    x=(temp_ceusius*9/5)+32
    return x

def classificador_de_renda(renda):
    if renda >= 4000:
        return 'Classe A'
    elif renda >= 1500:
        return 'Classe B'
    else:
        return 'Classe C'

def encontrar_palavra_mais_longa(lista_de_palavras):
    palavra_mais_longa=''
    for palavra in lista_de_palavras:
        if len(palavra)>len(palavra_mais_longa):
            palavra_mais_longa=palavra
    return palavra_mais_longa

