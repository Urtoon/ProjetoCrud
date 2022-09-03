def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1:31;107m404ERROR. O número digitado é inválido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1:31;107m404ERROR. Nenhum número foi digitado.\033[m')
            return
        else:
            return n

def linha(obj= '~', tam=50):
    return (obj * tam)

def divisa(txt):
    print(linha())
    print(txt.center(50))
    print(linha())

def menu(msg, lista):
    divisa(f'\033[32m\t{msg}\033[m')
    c = 1
    for item in lista:
        print(f'\033[1;34m{c} -\t\033[m \033[1;35m{item}\033[m')
        c += 1
    print(linha())
    escolha = leiaInt('\033[1;34mO que você quer fazer? \033[m')
    return escolha