from Calculadora import Calculadora
from AddOperation import AddOperation
from SubOperation import SubOperation

calc = Calculadora(AddOperation(), SubOperation())
op1 = calc.add(2, 5, True)
op2 = calc.sub(5, 3, True)

print(op1)
print(op2)