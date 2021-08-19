# Ler um valor em reais e mostrar a cotação em dólar
# Desafio 10 da aula 7

"""
Nessa atividade utilizamos API. O import da biblioteca 'requests' serve para poder usar o comando 'get'.
O import do modulo JSON serve para poder manipular a resposta da requisição dentro do Python
"""
import requests
import json

def req():

    # O URL vai servir para acessar o link da API
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BRL-USD,BRL-EUR,USD-BRLT"

    # A variável 'requisicao' serve para buscar na URL as informações
    requisicao = requests.get(url)

    # Na variável 'cotacao' transformamos a resposta da requisição numa JSON que pode ser lida no Python
    cotacao = requisicao.json()
    return requisicao, cotacao

def cotBR_US():  # Converter REAL para Dólar
    """
    A variável 'dolar' esta sendo utilizada para mostrar uma mensagem mostrando o valor da cotação de modo mais tradicional, onde R$ 1 real == X dólares
    A 'conversao' está fazendo já a transformação de Real -> USD. Esse valor é mostrado no print com o resultado
    A variável 'real' é um float que recebe os valores do usuário
    """
    dolar = cotacao['USDBRL']['bid']
    conversao = float(cotacao['BRLUSD']['bid'])
    real = float(input('Digite o valor em REAIS: R$ '))

    print(f'A cotação atual do dólar é de R$ {dolar}')
    print(
        f'\nO valor de R$ {real} reais em dólar na cotação atual, onde R$ 1 real equivale a aproximadamente U$ {conversao:.2f} dólares americanos, é de U$ {real * conversao:.2f} dólares')


def cotUS_BR():  # Converter DÓLAR para REAL
    """
    A variável 'real' nessa função já está com o valor da cotação tradicional, ou seja, 1 real == X dólares
    A variável 'dólar' recebe a entrada do usuário.
    """

    real = float(cotacao['USDBRL']['bid'])
    dolar = float(input('Digite o valor em DÓLARES AMERICANOS: U$ '))

    print(f'A cotação atual do dólar é de R$ {real}')
    print(
        f'\nO valor de U$ {dolar} dólares na cotação atual onde U$ 1 dólar equivale a aproximadamente R$ {real:.2f} reais, é de R${dolar * real:.2f}')


def main():
    opcao = int(input('Digite a opção desejada:\n1 - Cotar Real -> Dólar.\n2 - Cotar Dólar -> Real: '))

    if opcao == 1:
        br_us = cotBR_US()
    if opcao == 2:
        us_br = cotUS_BR()
    if opcao != 1 and opcao != 2:
        print('\nPor gentileza, escolha opção 1 ou 2')
        main()

#main()
cotBR_US()