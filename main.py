from tarefas import Tarefas


def remover_tarefa_segura(tf, indice):
    '''removendo uma tarefa e tratando erro caso indice seja invalido'''
    try:
        tf.remover_tarefa(indice)
        print(f'tarefa no indice {indice} removida')
        return True
    except IndexError as e:
        print(f'Error {e}')
        return False


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
tf.adicionar_tarefa('estudar', 'ler', 'dormir')
remover_tarefa_segura(tf, 0)      
concluir_tarefa_segura(tf, 0)   

print('tarefa pendente', tf.listar_tarefas())       
print('tarefa concluida', tf.listar_tarefas_concluidas())