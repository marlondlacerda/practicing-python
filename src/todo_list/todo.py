
def add(value):
    with open('lista.txt', 'a+') as file:
        file.write(f'{value}\n')


def remove():
    with open('lista.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        last_line = lines[-1]

        with open('lista_backup.txt', 'w+') as file_backup:
            file_backup.write(lines.pop())

        for i in lines:
            if i != last_line:
                file.write(i)

        file.truncate()


def refazer():
    with open('lista_backup.txt', 'r+') as file_backup:
        line = file_backup.readline()

        if len(line) > 0:
            with open('lista.txt', 'a+') as file:
                file.write(line)
                file_backup.seek(0)
                file_backup.truncate()
        else:
            print('Não há nada para refazer')


while True:
    todo_command = input(
        """
Digite uma das opções abaixo:
1 - Adicionar
2 - Remover
3 - Refazer
"""
    )

    if todo_command == '1':
        add(input('Digite o que você quer adicionar: '))
    elif todo_command == '2':
        remove()
    elif todo_command == '3':
        refazer()
    else:
        print('Comando inválido')
        break
