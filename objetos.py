from inicio import *
from random import randint

class Arquivo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def arquivo_existe(self):
        try:
            a = open(self.nome_arquivo, 'rt')
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def criar_arquivo(self):
        try:
            a = open(self.nome_arquivo, 'wt+')
            a.close()
        except:
            print('\033[1:31:107mNão foi possível criar o arquivo\033[m')
        else:
            print(f'\033[32mO arquivo {self.nome_arquivo} foi criado com sucesso.\033[m')

    def ler_arquivo(self):
        try:
            a = open(self.nome_arquivo, 'rt')
        except:
            print('\033[1:31:107mNão foi possível ler o arquivo.\033[m')
        else:
            if self.nome_arquivo == 'clientes.txt':
                c = 0
                divisa(f'Arquivo {self.nome_arquivo}')
                for linha in a:
                    dado = linha.split(';')
                    dado[2] = dado[2].replace('\n', '')
                    print(f'{c} - ID:{dado[0]}{dado[1]:^15}{dado[2]:^15}{dado[3]:>3}')
                    c += 1
            elif self.nome_arquivo == 'motos.txt':
                c = 0
                divisa(f'Arquivo {self.nome_arquivo}')
                for linha in a:
                    dado = linha.split(';')
                    dado[2] = dado[2].replace('\n', '')
                    print(f'{c} - ID:{dado[0]}{dado[1]:^15}{dado[2]:^15}{dado[3]:>3}')
                    c += 1

            elif self.nome_arquivo == 'temp.txt':
                c = 0
                divisa(f'Arquivo {self.nome_arquivo}')
                for linha in a:
                    dado = linha.split(';')
                    dado[3] = dado[3].replace('\n', '')
                    print(f'{c} - ID:{dado[0]}{dado[1]:^30}{dado[2]:^30}{dado[3]:>3}')
                    c += 1

            elif self.nome_arquivo == 'vendas.txt':
                divisa(f'Arquivo {self.nome_arquivo}')
                print(f'{"-" * 20} Vendas {"-" * 20}'.center(50))
                c = 1
                for linha in a:
                    dado = linha.split(';')
                    dado[5] = dado[5].replace('\n', '')
                    print(f'Venda:')
                    print(f'{c} - Cliente:\n\t{dado[0]}\t{dado[1]:^10}\n\tMoto: {dado[5]}\t{dado[6]:^10}\t{dado[7]:^10}')
                    print('¨' * 50)
                    c += 1
        finally:
            a.close()

    def menu_cadastro_cli(self):
        print(linha())
        resposta = menu('Cadastro dos Clientes', ['Novo cadastro', 'Deletar Cliente', 'Voltar'])

        if resposta == 1:
            Cliente.__id = randint(1, 1000)
            Cliente.__nome = input(f'Qual o nome do cliente? ')
            Cliente.__idade = int(input(f'Qual é a idade do cliente? '))
            Cliente.__cidade = input(f'Qual é a cidade do cliente? ')
            cliente = Cliente(Cliente.__id, Cliente.__nome, Cliente.__idade, Cliente.__cidade)
            Cliente.cadastrar_cliente(cliente)

        elif resposta == 2:
            self.apagar_item()

        elif resposta == 3:
            return

    def menu_cadastro_vei(self):
        print(linha())
        resposta = menu('Cadastro das Motos', ['Novo cadastro', 'Deletar Moto', 'Voltar'])

        if resposta == 1:
            Moto.__id = randint(1001, 2000)
            Moto.__modelo = input(f'Qual é o modelo da moto? ')
            Moto.__placa = input(f'Qual é a placa da moto? ')
            Moto.__cor = input(f'Qual é a cor da moto? ')
            moto = Moto(Moto.__id, Moto.__modelo, Moto.__placa, Moto.__cor)
            Moto.cadastrar_moto(moto)

        if resposta == 2:
            self.apagar_item()

        if resposta == 3:
            return

    def apagar_item(self):
        id = False
        try:
            while True:
                excluir = input(f'Qual ID deseja deletar? ')
                if not excluir.isnumeric():
                    print('\033[1:31:107mDigite um número válido.\033[m')
                elif excluir == '0':
                    break
                with open(self.nome_arquivo, 'r') as ex:
                    linhas = ex.readlines()
                    for i in linhas:
                        if i.split(';')[0] == excluir:
                            id = True
                if id == True:
                    print(f'ID{excluir} encontrado.')
                    id = False
                    break
                else:
                    print('\033[1:31:107mID inexistente.\033[m')

            certeza = input(f'Você deseja deletar o ID {excluir}? [sim] ou [nao] ').lower()
            if certeza == 'nao':
                return
            with open(self.nome_arquivo, 'r+') as f:
                linhas = f.readlines()
                f.seek(0)
                for l in linhas:
                    if excluir not in l:
                        f.write(l)
                    else:
                        print(f'Deletado com sucesso!')
                f.truncate()

                if not certeza == 'nao':
                    print('Deletado com sucesso')
                    print()
                else:
                    print(f'\033[1:31:107mERROR\033[m')
        except:
            print(f'\033[1:31:107mERROR\033[m')


    def registra_venda(self):
        id = False
        while True:
            cliente = input('Digite o ID do comprador [0] para a compra: ')
            if cliente == '0':
                break
            with open ('clientes.txt', 'r') as cli:
                linhas = cli.readlines()
                for i in linhas:
                    if i.split(';')[0] == cliente:
                        id = True
            if id == True:
                print('Cliente associado a lista de venda.')
                id = False
                break
            else:
                print('ID inexistente.')

        while True:
            if cliente == '0':
                break
            moto = input('Digite o ID da moto [0] para a compra: ')
            if moto == '0':
                break
            with open('motos.txt', 'r') as vei:
                linhas = vei.readlines()
                for i in linhas:
                    if i.split(';')[0] == moto:
                        id = True
            if id == True:
                print('Moto associada a lista de venda.')
                id = False
                break
            else:
                print('ID inexistente.')
        try:
            if cliente == '0':
                return
            if moto == '0':
                return

            with open('clientes.txt', 'r') as comprador_file:
                linhas = comprador_file.readlines()
                comprador_file.seek(0)
                with open('temp.txt', 'a') as temp:
                    for l in linhas:
                        if cliente in l:
                            temp.write(f'{l};'.replace('\n', ''))


            with open('motos.txt', 'r+') as motos_file:
                linhas = motos_file.readlines()
                motos_file.seek(0)
                with open('temp.txt', 'a') as temp:
                    for l in linhas:
                        if moto in l:
                            temp.write(l)
                    temp.truncate()

                motos_file.seek(0)
                for l in linhas:
                    if moto not in l:
                        motos_file.write(l)
                    else:
                        print('Item deletado.')

                motos_file.truncate()

            with open(self.nome_arquivo, 'r') as temp:
                linhas = temp.readlines()
                temp.seek(0)
                with open('vendas.txt', 'a') as vendas:
                    for l in linhas:
                        vendas.write(l)

        except:
            print('\033[1:31:107mNão foi possível registrar a venda.\033[m')
        else:
            print('Venda registrada com sucesso.')

        a = open(self.nome_arquivo, 'w+')
        a.close()

    def listar_venda(self):
        try:
            listar = int(input('Listar venda pelo número: '))
            with open('vendas.txt', 'r') as vendas:
                linhas = vendas.readlines()
                det_compra = linhas[listar-1].split(';')
                det_compra[5].replace('\n', '')
                print('-' * 50)
                print(f'\033[3:36mA compra {listar} foi feita for \033[34m{det_compra[1]}\033[3;36m'
                      f'\nA moto é uma \033[34m{det_compra[5]}\033[3;36m da placa \033[34m{det_compra[6]}\033[3;36m e cor \033[34m{det_compra[7]}\033[3;36m'
                      f'\nObrigado pela compra e volte sempre!\033[m')
                input('Pressione ENTER para dar continuidade')
        except:
            print('\033[1:31:107mVenda escolhida inválida.\033[m')

class Cliente(Arquivo):
    def __init__(self, id, nome, idade, cidade, nome_arquivo='clientes.txt'):
        super().__init__(nome_arquivo)
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__cidade = cidade

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def cidade(self):
        return self.__cidade

    @id.setter
    def id(self, id):
        self.__id = id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    def compra(self, moto):
        pass

    def cadastrar_cliente(self):
        try:
            a = open(self.nome_arquivo, 'at')
        except:
            print('\033[1:31:107mErro no arquivo.\033[m')
        else:
            try:
                a.write(f'{self.__id};{self.__nome};{self.__idade};{self.__cidade}\n')
            except:
                print('\033[1:31:107mErro no arquivo.\033[m')
            else:
                print(f'Registro de {self.__nome} adicionado com sucesso.')
            finally:
                a.close()

class Moto(Arquivo):
    def __init__(self, id, modelo, placa, cor, nome_arquivo='motos.txt'):
        super().__init__(nome_arquivo)
        self.__id = id
        self.__modelo = modelo
        self.__placa = placa
        self.__cor = cor

    @property
    def id(self):
        return self.__id

    @property
    def modelo(self):
        return self.__modelo

    @property
    def placa(self):
        return self.__placa

    @property
    def cor(self):
        return self.__cor

    @id.setter
    def id(self, id):
        self.__id = id

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    def cadastrar_moto(self):
        try:
            a = open(self.nome_arquivo, 'at')
        except:
            print('\033[1:31:107mErro no arquivo.\033[m')
        else:
            try:
                a.write(f'{self.__id};{self.__modelo};{self.__placa};{self.__cor}\n')
            except:
                print('\033[1:31:107mErro no arquivo.\033[m')
            else:
                print(f'Registro da moto de ID {self.__id} adicionado com sucesso.')
            finally:
                a.close()






