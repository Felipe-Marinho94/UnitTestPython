'''
Criação de espião para o método de adição da classe AddOperation
Autor:Felipe Pinto Marinho
Data:24/08/2023
'''

#Importando pacotes
from faker import Faker

fake = Faker()

#Classe para a operação de soma
class AddOperationSpy:

    #Construtor
    def __init__(self):
        self.soma_attributer = {}

    def soma(self, number1, number2):
        self.soma_attributer['number1'] = number1
        self.soma_attributer['number2'] = number2
        return fake.random_number()