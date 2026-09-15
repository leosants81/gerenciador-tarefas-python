class Tarefas:

    def __init__(self):
        self.tarefas = []
        self.tarefas_concluidas = []

    def adicionar_tarefa(self, *tarefas):
        tarefa_adicionada = []
        for tarefa in tarefas:
            if tarefa.strip() != "":
                self.tarefas.append(tarefa)
                tarefa_adicionada.append(tarefa)
        return tarefa_adicionada


    def remover_tarefa(self, indice):
        if not (0 <= indice < len(self.tarefas)):
            mensagem = (
            f'indice inválido: {indice}. '
            f'Existem {len(self.tarefas)} tarefa(s).'
        )
            raise IndexError(mensagem)
        self.tarefas.pop(indice)



    def concluir_tarefa(self, indice):
        if not (0 <= indice < len(self.tarefas)):
            mensagem = (
            f'indice inválido: {indice}. '
            f'Existem {len(self.tarefas)} tarefa(s).'
        )
            raise IndexError(mensagem)
        tarefa = self.tarefas.pop(indice)
        self.tarefas_concluidas.append(tarefa)
        return tarefa


    def listar_tarefas(self):
        return self.tarefas


    def listar_tarefas_concluidas(self):
        return self.tarefas_concluidas


