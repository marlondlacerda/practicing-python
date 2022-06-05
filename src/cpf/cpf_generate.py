from random import randint
from cpf_validate import cpf_validate


def multiply_numbers(numbers):
    """
    Multiply the numbers in a CPF number.
    """
    get_len = len(numbers) + 1
    result = 0

    for i, number in enumerate(range(get_len, 1, -1)):
        result += int(numbers[i]) * number

    return result


def create_last_two_digits(numbers):
    """
    Create the last two digits of a CPF number.
    """
    get_first_digit = multiply_numbers(numbers)
    first_digit = str(11 - (get_first_digit % 11))

    if int(first_digit) > 9:
        first_digit = "0"

    get_second_digit = multiply_numbers((numbers + first_digit))

    second_digit = str((11 - (get_second_digit % 11)))

    return first_digit + second_digit


def generate_cpf():
    """
    Generate a random CPF number.
    """
    get_random_numbers = str(randint(100000000, 999999999))
    last_two_digits = str(create_last_two_digits(get_random_numbers))

    cpf = (
        ".".join(
            [
                get_random_numbers[:3],
                get_random_numbers[3:6],
                get_random_numbers[6:],
            ]
        )
        + "-"
        + last_two_digits
    )

    return cpf


def generate_only_valid_cpf():
    """
    Generate a valid CPF number.
    """
    while True:
        cpf = generate_cpf()
        if cpf_validate(cpf) == "CPF VÁLIDO!":
            return cpf


result = generate_only_valid_cpf()
print(result)
print(cpf_validate(result))


def func(*kargs):
    print(kargs)


func({
    "nome": "João",
    "idade": "20",
})


algumacoisa = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print([11, 12, 13, 14, *algumacoisa])
