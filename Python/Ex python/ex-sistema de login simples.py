usuario_correto = 'admin'
senha_correta = '12345'
usuario_digitado=str(input('Quem deseja efetuar login:  '))
senha_digitada=str(input('Por favor, digite a senha deste usuário:  '))
if usuario_correto == usuario_digitado.lower():
    if senha_correta == senha_digitada.lower():
        print('Login efetuado com sucesso!')
    else:
        print('Senha incorreta')
else:
    print('Usuário não encontrado.')