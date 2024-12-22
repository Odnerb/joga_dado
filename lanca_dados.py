"""
A biblioteca random trabalha com a geração de números aleatórios, existem diversas funções embutidas no pacote
para resolução dos mais variados tipos de problemas. Para esta simulação de lançamento de dados, será utilizado
a função randint(inicio, fim) que permite gerar números aleatórios de 1 a 6.
"""
import random


def jogar():
    """
    Toda vez que o usuário apertar o botão "jogar", a função irá imprimir na tela
    o valor em que o dado caiu para o jogador. Na função em questão, são impressos
    números de 1 a 6, sem excludentes, ou seja, o 6 não é excluido e nenhum número
    dele é retornado.
    :return: None
    """
    print(random.randint(1, 6))


if __name__ == '__main__':
    """Testando aplicabilidade"""
    lanca_dados: jogar()
