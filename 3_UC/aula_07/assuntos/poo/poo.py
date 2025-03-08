# aluno -> Nome, idade, endereço, cpf

class Aluno: # Utlizamos o padrão PascalCase para classes.
    
    def __init__(self, nome, idade, endereco, cpf):
        self.nome = nome
        self.idade = idade    
        self.endereco = endereco
        self.cpf = cpf
        self.matriculado = True  # default, Toda cópia da classe aluno vai ter essa caracteristica

    # Método que altera o status da matricula do aluno.
    def situacao(self):
        if self.matriculado == True: # == condição de igualdade
            self.matriculado = False  # = atribuição
        elif self.matriculado == False:
            self.matriculado = True

    # método que exibe as informações aluno
    def exibir_info(self):
        print( f'''
            DADOS DO ESTUDANTE 
        🤓 O nome do aluno(a) é {self.nome}
        📋 e o CPF é {self.cpf}
        ''')

# Criando cópias da classe aluno (instânciação)
a1 = Aluno("Ana", 22,"Rua 1", "123456")
a2 = Aluno("Bia", 20,"Rua 16", "654321")

print(a1)
a1.exibir_info()