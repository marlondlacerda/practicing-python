import re


def check_dot(numbers):
    """
    Check if the CPF has a valid format.
    """
    regex = re.compile(r"^(\d{3}\.){2}\d{3}-\d{2}$")
    return bool(re.match(regex, numbers))


def get_numbers(cpf):
    """
    Get the numbers from a CPF number ex("123.456.789-10").
    """
    numbers = cpf.replace(".", "").replace("-", "")
    return numbers


def multiply_numbers(numbers):
    """
    Multiply the numbers in a CPF number.
    """
    get_len = len(numbers) + 1
    result = 0

    for i, number in enumerate(range(get_len, 1, -1)):
        result += int(numbers[i]) * number

    return result


def get_last_two_digits(numbers):
    """
    Get the last two digits of a CPF number.
    """
    get_first_digit = multiply_numbers(numbers)
    first_digit = str(11 - (get_first_digit % 11))

    if int(first_digit) > 9:
        first_digit = "0"

    get_second_digit = multiply_numbers((numbers + first_digit))

    second_digit = str((11 - (get_second_digit % 11)))

    return first_digit + second_digit


def cpf_validate(numbers):
    """
    Validate a CPF number
    First, we need to check if the length is valid.and
    have a valid format.

    Then, we multiply the first nine digits

    Finally, we need to check if the last two digits are valid.

    and return a message if the CPF is valid or not.
    """
    if (len(numbers) != 14) or (check_dot(numbers) is False):
        return "CPF INVÁLIDO! - Tamanho ou formato incorreto"

    numbers = get_numbers(numbers)

    if numbers == numbers[0] * len(numbers):
        return "CPF INVÁLIDO! - Números iguais"

    last_two_digits = get_last_two_digits(numbers[:-2])

    if last_two_digits == numbers[-2:]:
        return "CPF VÁLIDO!"
    else:
        return "CPF INVÁLIDO!"
