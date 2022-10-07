# Módulo -> Menu principal do arquivo menu
from menu import menuAtividade
# Módulo -> Verifica o e-mail
import re

# Módulo -> Ocultar senha
import pwinput

# Regex
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#Dicionário de usuários cadastrados
usuarios = {}


# Classe -> Usuário
class Usuario:

    # Construtor da classe
    def __init__(self):
        pass

    # Função -> Cadastrar usuário
    def cadastro(self):
        print('\n| Realizar Cadastro |\n')
        simbolos = ['!', '@', '#', '$', '%', '&', '*', '¨', '(', ')']
        status = False

        while status == False:
            print('-' * 45)

            try:
                usuario = str(input('Usuário:\n>>> '))

            except ValueError:
                print('\nDigite valores válidos\n')

            if usuario in usuarios.keys():
                print('\nUsuário já existe\n')

            elif not any(caracter.isalpha() for caracter in usuario):
                print('\nNome de Usuário deve conter letras\n')

            else:
                # Quebra o loop do nome de usuário
                status = True
                statusS = False
                print(
                    '\n| A senha deve conter uma combinação de letras, números e símbolos |\n'
                )

                while statusS == False:
                    print('-' * 45)

                    try:
                        senha = pwinput.pwinput(prompt='Senha:\n>>> ')

                    except:
                        print('\nDigite valores válidos\n')

                    # Verifica se a senha contém números
                    if not any(caracter.isdigit() for caracter in senha):
                        print('\nSenha deve conter números\n')

                    # Verifica se a senha contém letras
                    elif not any(caracter.isalpha() for caracter in senha):
                        print('\nSenha deve conter letras\n')

                    # Verifica se a senha contém simbolos
                    elif not any(caracter in simbolos for caracter in senha):
                        print('\nSenha deve conter símbolos\n')

                    else:

                        # Verifica se a senha contém 8 ou mais caracteres
                        if len(senha) >= 8:
                            usuarios[usuario] = senha
                            print('\n| Cadastrado com sucesso |\n')

                            # Quebra o loop da senha
                            statusS = True
                            self.info(usuario, senha)

                        else:
                            print('\nSenha deve conter 8 ou mais caracteres\n')

    # Função -> Cadastra as informações do usuário
    def info(self, usuario, senha):
        print('\n| Cadastrar dados do Usuário |\n')
        print('-' * 45)

        while True:

            try:
                nome = str(input('Nome:\n>>> '))
                if not nome.isalpha():
                    raise ValueError('\nDigite valores válidos\n')

            except ValueError:
                print('\nDigite valores válidos\n')
                continue
            else:
                if not (verificarNome(nome) and len(nome) >= 3):
                    print(
                        '\nNome de usuário deve conter apenas letras e ser maior ou igual a 3 letras\n'
                    )
                    continue

            statusE = False
            while statusE == False:
                print('-' * 45)

                try:
                    email = str(input('E-mail\n>>> '))

                except ValueError:
                    print('\nDigite valores válidos\n')

                else:
                    # Verifica o e-mail
                    if (re.search(regex, email)):
                        # Quebra o loop do e-mail
                        statusE = True

                    else:
                        print('\nE-mail Inválido\n')

            statusT = False
            while statusT == False:
                print('-' * 45)

                try:
                    tel = str(input('Telefone\n>>> '))

                except ValueError:
                    print('\nDigite valores válidos\n')

                else:
                    #verifica se o telefone tem 11 digitos
                    if len(tel) > 11 or len(tel) < 11:
                        print(
                            '\nO número de telefone deve conter 11 dígitos\n')

                    else:
                        # Quebra o loop do telefone
                        statusT = True

            # Exibe pro usuário as informações
            print(
                f'\n| Informações do Usuário |\nNome: {nome}\nUsuário: {usuario}\nE-mail: {email}\nTelefone: {tel}\nSenha: {len(senha) * "*"}'
            )
            self.menuLogin()

    # Função -> Faz o login do usuário
    def login(self):
        print('\n|  Opção escolhida: Efetuar Login |\n')

        status = False
        while status == False:
            print('-' * 45)

            try:
                usuario = str(input('Usuário:\n>>> '))
            except ValueError:
                print('\nDigite valores válidos\n')
            else:

                #verifica se usuário está cadastrado
                if usuario in usuarios.keys():
                    status = True
                    statusSenha = False

                    while statusSenha == False:

                        try:
                            senha = pwinput.pwinput(prompt='Senha:\n>>> ')
                        except:
                            print('\nDigite valores válidos\n')

                        #verifica se a senha está correta
                        if senha == usuarios[usuario]:
                            print('\n| Logado com sucesso |')
                            statusSenha = True
                            menuAtividade()

                        else:
                            print('\nSenha incorreta\n')

                else:
                    print('\nUsuário não encontrado\n')

    def menuLogin(self):

        while True:
            opcao = input(f'''
{'-'*45}
    O que deseja fazer?

    |1| Realizar Cadastro
    |2| Efetuar Login
{'-'*45}
    >>> ''')
            if opcao == '1':
                self.cadastro()

            elif opcao == '2':
                self.login()

            else:
                print('\nDigite uma opção válida!\n')


# Função -> Verifica o nome do usuário
def verificarNome(str):
    return all(char.isalpha() or char.isspace() for char in str)
