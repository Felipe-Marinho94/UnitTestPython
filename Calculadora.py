'''
Trabalhando com testes Unitários em Python
Autor:Felipe Pinto Marinho
Data:24/08/2023
'''
#Criando uma classe calculadora
class Calculadora:
    #Método de construção
    def __init__(self, adicao, subtracao):
        self.adicao = adicao
        self.subtracao = subtracao

    def add(self, number1, number2, op):
        if op:
            return self.adicao.soma(number1, number2)
        return None
    
    def sub(self, number1, number2, op):
        if op:
            return self.subtracao.diferenca(number1, number2)
        return None
        
