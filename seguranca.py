def adicionar_tarefa_segura(tf, *tarefa):
    '''tratando erro caso a tarefa nao seja um texto '''
    try:
        tarefa_adicionada = tf.adicionar_tarefa(*tarefa)
        print(f'Tarefa "{tarefa_adicionada}" adicionada')
        return tarefa_adicionada
    except TypeError as e:
        print(f'Error {e}')
        return None


def remover_tarefa_segura(tf, indice):
    '''removendo uma tarefa e tratando erro caso indice seja invalido'''
    try:
        tarefa = tf.remover_tarefa(indice)
        print(f'tarefa "{tarefa}" removida')
        return tarefa
    except IndexError as e:
        print(f'Error {e}')
        return None


def concluir_tarefa_segura(tf, indice):
    '''concluindo uma tarefa e tratando erro caso indice seja invalido'''
    try:
        tarefa = tf.concluir_tarefa(indice)
        print(f'tarefa "{tarefa}" concluida')
        return tarefa
    except IndexError as e:
        print(f'Error {e}')
        return None
