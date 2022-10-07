import calendar
import datetime

# Função -> Mostrar cabeçalho ao iniciar programa
def peixes(): 
    print(f'''
     ___________________________
    |                           |
    |     Planner Estudantil    |
    |       Grupo Peixes        |
    |___________________________|
    ''')

# Função -> Mostrar calendário do mês atual e data atual ao iniciar programa
def calendario():
    atual = datetime.datetime.now() 

    ano =  atual.year
    mes = atual.month

    print(f'''
{'-'*45}
{calendar.month(ano, mes)}
    
{atual}
{'-'*45}''')
