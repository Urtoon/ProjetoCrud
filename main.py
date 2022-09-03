from inicio import *
from objetos import *

temp = Arquivo('temp.txt')
if not Arquivo.arquivo_existe(temp):
    Arquivo.criar_arquivo(temp)

clientes = Arquivo('clientes.txt')
if not Arquivo.arquivo_existe(temp):
    Arquivo.criar_arquivo(clientes)

motos = Arquivo('motos.txt')
if not Arquivo.arquivo_existe(motos):
    Arquivo.criar_arquivo(motos)

vendas = Arquivo('vendas.txt')
if not Arquivo.arquivo_existe(vendas):
    Arquivo.criar_arquivo(vendas)

divisa('\033[4;33mLOJA DE MOTOS\033[m')

while True:

    resposta = menu('Menu', ['Listar clientes', 'Cadastro de clientes', 'Listar motos', 'Cadastro de motos', 'Registrar venda', 'Listar vendas', 'Sair'])

    if resposta == 1:
        Arquivo.ler_arquivo(clientes)

    elif resposta == 2:
        Arquivo.menu_cadastro_cli(clientes)

    elif resposta == 3:
        Arquivo.ler_arquivo(motos)

    elif resposta == 4:
        Arquivo.menu_cadastro_vei(motos)

    elif resposta == 5:
        Arquivo.registra_venda(temp)

    elif resposta == 6:
        Arquivo.ler_arquivo(vendas)
        venda = Arquivo.listar_venda(vendas)

    elif resposta == 7:
        break