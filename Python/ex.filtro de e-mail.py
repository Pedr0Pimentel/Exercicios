lista_email = ["ana@gmail.com", "bruno@hotmail.com", "visitante@temp-email.com", "carlos@gmail.com", "admin@yahoo.com", "maria@hotmail.com", "fake@spam.com"]
lista_email_confiavel = []
for correio in lista_email:
    if '@gmail.com' in correio:
        lista_email_confiavel.append(correio)
    elif '@hotmail.com' in correio:
        lista_email_confiavel.append(correio)
print(lista_email_confiavel)