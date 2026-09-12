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


    def remover_tarefas(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)


    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas.pop(indice)
            self.tarefas_concluidas.append(tarefa)
            return tarefa
        return None
    

    def listar_tarefas(self):
        return self.tarefas



tf1 = Tarefas()
tf1.adicionar_tarefa('estudar', 'tomar banho', 'arrumar para o trabalho')

tf1.remover_tarefas(0)


print(tf1.listar_tarefas())