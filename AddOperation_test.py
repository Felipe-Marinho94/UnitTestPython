from AddOperation import AddOperation
from faker import Faker

fake = Faker()

def test_soma():
    addOperation = AddOperation()
    number1 = fake.random_number()
    number2 = fake.random_number()
    expected = number1 + number2
    result = addOperation.soma(number1, number2)

    print(expected)
    print(result)

    assert result == expected

