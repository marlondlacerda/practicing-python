from src.cpf.cpf_validate import cpf_validate, check_dot, get_numbers


def test_cpf_with_10_characters():
    report = cpf_validate("1234567891")
    assert report == "CPF INVÁLIDO! - Tamanho ou formato incorreto"


# TESTS FOR check_dot
def test_check_dot_with_correct_numbers():
    assert check_dot("123.456.789-10") is True


def test_check_dot_with_incorrect_numbers():
    assert check_dot("123.456789-11") is False
    assert check_dot("123.456.789.11") is False
    assert check_dot("123456.789-11") is False


def test_get_numbers_with_correct_numbers():
    assert get_numbers("123.456.789-10") == "12345678910"
    assert get_numbers("133.456.749-11") == "13345674911"


def test_cpf_with_correct_numbers():
    report = cpf_validate("451.653.312-02")
    assert report == "CPF VÁLIDO!"


def test_cpf_with_incorrect_numbers():
    report = cpf_validate("123.456.789-11")
    assert report == "CPF INVÁLIDO!"
