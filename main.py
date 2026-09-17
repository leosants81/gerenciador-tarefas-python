from tarefas import Tarefas


def adicionar_tarefa_segura(tf, *tarefa):
    '''tartando erro caso a tarefa nao seja um texto '''
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


tf = Tarefas()
adicionadas = tf.adicionar_tarefa(
    'estudar', 'ler', 'dormir', 'trabalhar', 'jogar')
print('tarefas adicionadas', adicionadas)
print('tarefas pendentes', tf.listar_tarefas())


print('teste de erro com int')
adicionar_tarefa_segura(tf,'estudar',123,'dormir')

concluir_tarefa_segura(tf, 0)
remover_tarefa_segura(tf, 1)
print('Pendentes:', tf.listar_tarefas())
print('Concluídas:', tf.listar_tarefas_concluidas())