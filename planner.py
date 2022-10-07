from datetime import date, datetime as dt, timedelta
from threading import Thread
import time
from evento import Evento
from tarefa import Tarefa


class Planner():
    # Atividade -> Evento

    # Função -> Inserir evento
    def inserirEvento(self, titulo, descricao, local, data):
        return Evento(titulo, descricao, local, data)

    # Função -> Atualizar evento
    def atualizarEvento(self, listaEvento, titulo):

        try:
            novoTitulo = input('\nNovo título do evento: ')
        except ValueError:
            print('\nDigite valores válidos\n')
        try:
            novaDescricao = input('Nova descrição do evento: ')
        except ValueError:
            print('\nDigite valores válidos\n')
        try:
            novoLocal = input('Novo local do evento: ')
        except ValueError:
            print('\nDigite valores válidos\n')
        try:
            novaData = dt.strptime(
                input('Nova data do evento (exemplo: 10/11/12 13:14:15): '),
                '%d/%m/%y %H:%M:%S')
        except:
            print('\nDigite valores válidos\n')

        try:
            for evento in listaEvento:

                if evento.getTitulo() == titulo:
                    evento.setTitulo(novoTitulo)
                    evento.setDescricao(novaDescricao)
                    evento.setLocal(novoLocal)
                    evento.setData(novaData)

        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

        else:
            print(f'\n| Evento atualizado |\n')

    # Função -> Excluir evento
    def excluirEvento(self, listaEvento, titulo):

        if len(listaEvento) != 0:
            cont = 0

            for evento in listaEvento:

                try:
                    if evento.getTitulo() == titulo:
                        listaEvento.pop(cont)
                        print(f"\n| Evento '{titulo}' excluido |\n")

                    else:
                        print(f"\n| Evento '{titulo}' não encontrado |\n")
                except Exception:
                    print(
                        "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
                    )

        else:
            print(f'\n| Não há eventos cadastrados |\n')

    # Função -> Buscar evento
    def buscarEvento(self, listaEvento, titulo):
        cont = 0
        print('\n| Eventos encontrados |\n')

        try:
            for evento in listaEvento:

                if evento.getTitulo() == titulo:
                    print(f'''
        | Título do evento: {evento.getTitulo()}
        | Descrição do evento: {evento.getDescricao()}
        | Local do evento: {evento.getLocal()}
        | Data do evento: {evento.getData()}''')
                    break
                cont += 1
        except Exception as erro:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Função -> Relatório do evento
    def relatorioEvento(self, listaEvento):

        try:
            for evento in listaEvento:
                print(f'''
    | Título do evento: {evento.getTitulo()}
    | Descrição do evento: {evento.getDescricao()}
    | Local do evento: {evento.getLocal()}
    | Data do evento: {evento.getData()}''')
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Função -> Countdown do evento
    def emitirCountdown(self, listaEvento, titulo):

        cont = 0
        print('\n| Countdown de Eventos encontrados |\n')
        try:
            for evento in listaEvento:

                if evento.getTitulo() == titulo:

                    atual = dt.now()
                    diferenca = evento.getData() - atual
                    segundos = diferenca.seconds
                    total = diferenca.days

                    dias = (segundos / 60 / 60) // 24
                    horas = ((segundos - dias * 24 * 60 * 60) / 60) // 60

                    print(f'''
    | Título do evento: {evento.getTitulo()}
    | Descrição do evento: {evento.getDescricao()}
    | Local do evento: {evento.getLocal()}
    | Data do evento: {evento.getData()}
    | O evento será em: {total} dias e {horas} horas''')
                    break
                cont += 1
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )


# Atividade -> Tarefa

# Função -> Inserir tarefa

    def inserirTarefa(self, titulo, descricao):
        return Tarefa(titulo, descricao)

    # Função -> Atualizar tarefa
    def atualizarTarefa(self, listaTarefa, titulo):
        try:
            novoTitulo = input('\nNovo título do evento: ')
        except ValueError:
            print('\nDigite valores válidos\n')
        try:
            novaDescricao = input('Nova descrição do evento: ')
        except ValueError:
            print('\nDigite valores válidos\n')

        try:
            for tarefa in listaTarefa:
                if tarefa.getTitulo() == titulo:
                    tarefa.setTitulo(novoTitulo)
                    tarefa.setDescricao(novaDescricao)
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

        else:
            print(f'\n| Tarefa atualizada |\n')

    # Função -> Excluir tarefa
    def excluirTarefa(self, listaTarefa, titulo):

        if len(listaTarefa) != 0:
            cont = 0

            try:
                for tarefa in listaTarefa:
                    if tarefa.getTitulo() == titulo:
                        listaTarefa.pop(cont)
                        print(f'\n| Tarefa {titulo} excluida |\n')

                    else:
                        print(f'\nTarefa {titulo} não encontrada\n')
            except Exception:
                print(
                    "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
                )

        else:
            print('\n| Não há tarefas cadastradas |\n')

    # Função -> Buscar tarefa
    def buscarTarefa(self, listaTarefa, titulo):
        cont = 0
        print('\n| Tarefas encontradas |\n')
        try:
            for tarefa in listaTarefa:
                if tarefa.getTitulo() == titulo:
                    print(f'''
        | Título da tarefa: {tarefa.getTitulo()}
        | Descrição da tarefa: {tarefa.getDescricao()}''')
                    break
                cont += 1
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )

    # Função -> Relatório da tarefa
    def relatorioTarefa(self, listaTarefa):
        try:
            for tarefa in listaTarefa:
                print(f'''
        | Título da tarefa: {tarefa.getTitulo()}
        | Descrição da tarefa: {tarefa.getDescricao()}''')
        except Exception:
            print(
                "\nOcorreu um erro, não se preocupe não foi culpa sua, já fomos notificados ^^'\n"
            )
