import re


def check_dot(numbers):
    """
    Check if the CNPJ has a valid format.
    """
    regex = re.compile(r"^((\d{2}).(\d{3}).(\d{3})/(\d{4})-(\d{2}))*$")
    return bool(re.match(regex, numbers))


def get_numbers(cnpj):
    """
    Get the numbers from a cnpj number ex("123.456.789-10").
    """
    numbers = cnpj.replace(".", "").replace("-", "").replace("/", "")
    return numbers


def create_multiply(numbers=9):
    """
    Create the numbers to multiply.
    """
    return [number for i, number in enumerate(range(numbers, 1, -1))]


def multiply_numbers(numbers):
    """
    Multiply the numbers in a CNPJ number.
    """
    get_len = len(numbers) - 8 + 1
    numbers_for_multiply = create_multiply(get_len) + create_multiply()

    result = list(map(lambda x, y: x * int(y), numbers_for_multiply, numbers))

    return sum(result)


def get_last_two_digits(numbers):
    """
    Get the last two digits of a CNPJ number.
    """
    get_first_digit = multiply_numbers(numbers)
    first_digit = str(11 - (get_first_digit % 11))

    if int(first_digit) > 9:
        first_digit = "0"

    get_second_digit = multiply_numbers((numbers + first_digit))

    second_digit = str((11 - (get_second_digit % 11)))
    if int(second_digit) > 9:
        second_digit = "0"

    return first_digit + second_digit


def cnpj_validate(numbers):
    """
    Validate a CNPJ number
    First, we need to check if the length is valid.and
    have a valid format.

    Then, we multiply the first nine digits

    Finally, we need to check if the last two digits are valid.

    and return a message if the CNPJ is valid or not.
    """
    if (len(numbers) != 18) or (check_dot(numbers) is False):
        return "CNPJ INVÁLIDO! - Tamanho ou formato incorreto"

    numbers = get_numbers(numbers)

    if numbers == numbers[0] * len(numbers):
        return "CNPJ INVÁLIDO! - Números iguais"

    last_two_digits = get_last_two_digits(numbers[:-2])

    if last_two_digits == numbers[-2:]:
        return "CNPJ VÁLIDO!"
    else:
        return "CNPJ INVÁLIDO!"


print(cnpj_validate("85.730.042/0001-30"))
