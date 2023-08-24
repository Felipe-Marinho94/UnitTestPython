'''
Caso de teste para a classe Calculadora
Autor:Felipe Pinto Marinho
Data:24/08/2023
'''

#Importando a classe Calculadora
from Calculadora import Calculadora
from test.add import AddOperationSpy
from test.sub import SubOperationSpy
from faker import Faker 

fake = Faker()

##Criando a função de teste
def test_add():
    addOperation = AddOperationSpy()
    calculadora = Calculadora(addOperation, SubOperationSpy())

    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculadora.add(number1, number2, True)
    
    #Teste de entrada
    assert addOperation.soma_attributer['number1'] == number1
    assert addOperation.soma_attributer['number2'] == number2

    #Teste de saída
    assert result is not None

def test_add_None():
    addOperation = AddOperationSpy()
    calculadora = Calculadora(addOperation, SubOperationSpy())

    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculadora.add(number1, number2, False)
    
    #Teste de entrada
    assert addOperation.soma_attributer == {}

    #Teste de saída
    assert result is None