# Importar a biblioteca de expressões regulares
import re

# Função para somar dois números


def soma(number_one, number_two):
    return number_one + number_two

# Função para subtrair dois números


def subtrai(number_one, number_two):
    return number_one - number_two

# Função para multiplicar dois números


def multiplica(number_one, number_two):
    return number_one * number_two

# Função para dividir dois números


def divide(number_one, number_two):
    return number_one / number_two

# Função para elevar um número a uma potência


def potencia(number_one, number_two):
    return number_one ** number_two

# Função para calcular a raiz quadrada de um número


def raiz_quadrada(number):
    return number ** 0.5

# Função para calcular o fatorial de um número


def fatorial(number):
    if number == 0:
        return 1
    else:
        return number * fatorial(number - 1)

# Função principal da calculadora


def calculator():
    print("Bem-vindo à [2;34mCalculadora[0m!")
    print("Digite '[2;34m[2;31mquit[0m[2;34m[0m' para sair")

    # Loop principal da calculadora
    while True:
        # Ler a expressão matemática do usuário
        express = input("Digite uma expressão matemática: ")

        # Sair se o usuário digitar 'quit'
        if express == 'quit':
            print("Até a próxima!")
            return

        # Remover espaços em branco da expressão
        express = express.replace(" ", "")

        # Usar expressões regulares para validar a expressão
        if not re.match("^[\d+\-*/^()!]+$", express):
            print("[2;31mExpressão inválida![0m")
            continue

        # Avaliar a expressão matemática
        try:
            result = eval(express)
            print("result: ", result)
        except ZeroDivisionError:
            print("Erro: [2;31mdivisão por zero![0m")
        except SyntaxError:
            print("[2;31mExpressão inválida![0m")
        except:
            print("[2;31mOcorreu um erro inesperado![0m")


# Chamar a função da calculator
calculator()
