def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
        else:
            return n


def lin(tam=42):
    print('-' * tam)


def cabecalho(txt):
    lin()
    print(txt.center(42))
    lin()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[35m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    lin()
    opc = leiaInt('\033[35mSua Opção: \033[m')
    return opc
