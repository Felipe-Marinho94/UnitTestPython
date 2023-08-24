'''
Criação de espião para o método de diferença da classe SubOperation
Autor:Felipe Pinto Marinho
Data:24/08/2023
'''

#Importando pacotes
from faker import Faker

fake = Faker()

#Classe para a operação de soma
class SubOperationSpy:

    #Construtor
    def __init__(self):
        self.diferenca_attributer = {}

    def diferenca(self, number1, number2):
        self.diferenca_attributer['number1'] = number1
        self.diferenca_attributer['number2'] = number2
        return fake.random_number()