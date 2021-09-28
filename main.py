# 1 - imports - bibliotecas
import pytest


# 2 - class - classe


# TDD : Desenvolvimento Direcionado pelo Testes
# - Criar o esqueleto de classes, funções e métodos logo no início da Sprint
# - Criar pelo 1 teste (feliz) para todas as funções e métodos
# - Executar todos os testes unitários diariamente para medir o progresso

@pytest.mark.parametrize('numero1, numero2',[
    # valores
    (5, 4), # teste 1
    (3, 2), # teste 2
    (10, 6) # teste 3
])

# 3 - definitions - definições = métodos e funções
def print_hi(name):
    print(f'Oi, {name}')


def somar(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    if num2 == 0:
        return print("Não pode dividir por zero")

    else:
        return num1 / num2


def teste_somar():
    # 1 Configura / Prepara

    num1 = 8
    num2 = 5
    resultado_esperado = 13

    # 2 Executa

    resultado_atual = somar(num1, num2)

    # 3 - Check / Valida
    assert resultado_esperado == resultado_atual


def teste_somar_compacto():
    assert somar(5, 8) == 13


def teste_subtrair():
    assert subtrair(4, 5) == -1


def teste_multiplicar():
    assert multiplicar(3, 7) == 21


if __name__ == '__main__':
    print_hi('Jose')

    resultado = somar(1, 2)
    print(f'O resultado da soma: {resultado}')

    resultado = subtrair(5, 3)
    print(f'O resultado da subtração: {resultado}')

    resultado = multiplicar(2, 4)
    print(f'O resultado da multiplicação: {resultado}')

    resultado = dividir(12, 4)
    print(f'O resultado da divisão: {resultado}')
