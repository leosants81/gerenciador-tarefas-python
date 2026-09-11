class Tarefas:

    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        if tarefa.strip() != "":
            self.tarefas.append(tarefa)
            return True
        return False

    def remover_tarefas(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)

    def listar_tarefas(self):
        return self.tarefas


tf1 = Tarefas()
tf1.adicionar_tarefa('desenhar')
tf1.adicionar_tarefa('estudar')
tf1.adicionar_tarefa('academia')
tf1.remover_tarefas(0)
tf1.adicionar_tarefa('trabalhar')

print(tf1.listar_tarefas())