from datetime import datetime as dt
from planner import Planner

listaEvento = []
listaTarefa = []

planner = Planner()


def menuAtividade():
    planner.escutarNotificacoes(listaEvento)

    while True:
        op = input(f'''\n
{'-'*45}
    |1| Atividade -> Evento
    |2| Atividade -> Tarefa
    |3| Sair
{'-'*45}
    >>> ''')

        if op == '1':
            menuEvento()

        elif op == '2':
            menuTarefa()
        elif op == '3':
            print('\nFinalizando programa... \n')
            exit()
        else:
            print('\nOpção inválida\n')


def menuEvento():
    # Menu -> Evento
    op = input(f'''\n
{'-'*45}
    O que deseja fazer?

    |1| Inserir evento
    |2| Atualizar Evento
    |3| Excluir Evento
    |4| Buscar Evento
    |5| Relatório de Evento
    |6| Countdown de Evento
    |7| Voltar
{'-'*45}
    >>> ''')

    # Inserir evento
    if op == '1':
        print('\n| Inserir Evento |\n')

        try:
            titulo = input('\nTítulo do evento: ')
        except:
            print('\nDigite valores válidos\n')

        try:
            descricao = input('Descrição do evento: ')
        except:
            print('\nDigite valores válidos\n')

        try:
            local = input('Local do evento: ')
        except:
            print('\nDigite valores válidos\n')

        try:
            data = dt.strptime(
                input('Data do evento (Exemplo: 10/11/12 13:14:15): '),
                '%d/%m/%y %H:%M:%S')
        except:
            print('\nDigite valores válidos\n(Exemplo: 10/11/12 13:14:15)\n')
            return

        try:
            listaEvento.append(
                planner.inserirEvento(titulo, descricao, local, data))
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

        else:
            print(f'\n| Evento cadastrado |\n')

    # Atualizar evento
    elif op == '2':
        print('\n| Atualizar Evento |\n')

        try:
            titulo = input('\nTítulo do evento que deseja alterar: ')
        except:
            print('\nDigite valores válidos\n')

        try:
            print(planner.atualizarEvento(listaEvento, titulo))
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Excluir evento
    elif op == '3':
        print('\n| Excluir Evento |\n')
        try:
            titulo = input('\nTítulo do evento que deseja excluir: ')
        except:
            print('\nDigite valores válidos\n')

        try:
            print(planner.excluirEvento(listaEvento, titulo))
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Buscar evento
    elif op == '4':
        print('\n| Buscar Evento |\n')

        try:
            titulo = input('\nTítulo do evento que deseja buscar: ')
        except:
            print('\nDigite valores válidos\n')

        try:
            planner.buscarEvento(listaEvento, titulo)
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Relatório de evento
    elif op == '5':
        print('\n| Relatório de evento |\n')
        try:
            planner.relatorioEvento(listaEvento)
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Countdown de evento
    elif op == '6':
        try:
            titulo = input(
                '\nTítulo do evento que deseja emitir o countdown: ')
        except:
            print('\nDigite valores válidos\n')

        try:
            planner.emitirCountdown(listaEvento, titulo)
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Voltar
    elif op == '7':
        menuAtividade()


def menuTarefa():

    # Menu -> Tarefa
    op = input(f'''\n
{'-'*45}
    O que deseja fazer?
    
    |1| Inserir Tarefa
    |2| Atualizar Tarefa
    |3| Excluir Tarefa
    |4| Buscar Tarefa
    |5| Relatório de Tarefa
    |6| Voltar
{'-'*45}
    >>> ''')

    # Inserir tarefa
    if op == '1':
        print('\n| Inserir Tarefa |\n')
        try:
            titulo = input('\nTítulo da tarefa: ')
        except:
            print('\nDigite valores válidos\n')
        try:
            descricao = input('Descrição da tarefa: ')
        except:
            print('\nDigite valores válidos\n')
        try:
            listaTarefa.append(planner.inserirTarefa(titulo, descricao))
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

        else:
            print(f'\n| Tarefa cadastrada |\n')

    # Atualizar tarefa
    elif op == '2':
        print('\n| Atualizar tarefa |\n')

        try:
            titulo = input('\nTítulo do tarefa que deseja alterar: ')
        except:
            print('\nDigite valores válidos\n')

        try:
            print(planner.atualizarTarefa(listaTarefa, titulo))
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Excluir tarefa
    elif op == '3':
        print('\n| Excluir tarefa |\n')

        try:
            titulo = input('\nTítulo do tarefa que deseja excluir: ')
        except:
            print('\nDigite valores válidos\n')

        try:
            print(planner.excluirTarefa(listaTarefa, titulo))
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Buscar tarefa
    elif op == '4':
        print('\n| Buscar tarefa |\n')

        try:
            titulo = input('\nTítulo do tarefa que deseja buscar: ')
        except:
            print('\nDigite valores válidos\n')

        try:
            planner.buscarTarefa(listaTarefa, titulo)
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Relatório de tarefa
    elif op == '5':
        print('\n| Relatório de tarefa |\n')
        try:
            planner.relatorioTarefa(listaTarefa)
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Voltar
    elif op == '6':
        menuAtividade()

    else:
        print('\nOpção inválida\n')
