list_tarefas = ['estudar python','varrer a casa' ]
print('Esta é a sua lista de tarefas atual: {}'.format(list_tarefas))
action=str(input('Você deseja adicionar ou remover uma tarefa?  '))
if action.lower() == 'adicionar':
    nova_tarefa=str(input('Qual tarefa você deseja adicionar?  '))
    list_tarefas.append(nova_tarefa)
    print('Nova tarefa foi adicionada')
elif action.lower() == 'remover':
    remove_tarefa=str(input('Qual tarefa você deseja remover?  '))
    if remove_tarefa.lower() in list_tarefas:
        list_tarefas.remove(remove_tarefa.lower())
        print('A tarefa {} foi removida da lista de tarefas'.format(remove_tarefa))
    else:
        print('A tarefa {} não existe na lista de tarefas'.format(remove_tarefa))
else:
    print('Comando inválido')
print('Está é a sua lista de tarefas {}'.format(list_tarefas))