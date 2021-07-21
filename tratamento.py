import pandas as pd
import os.path

def tratamentoDados(banco_de_dados_em_excel):

    df = pd.read_excel(banco_de_dados_em_excel)
    colunas = len(df.columns)
    valoresColunas = []
    nomesColuna = []
    for i in range(colunas):
        nomesColuna.append(df.columns[i])
        valoresColunas.append(df[nomesColuna[i]].values)

    return valoresColunas,nomesColuna

def verificaExistencia(arquivo):
    valor = os.path.isfile(arquivo)
    return valor

def salvaGrafico(grafico,nome):
    nome_teste1 = 'Graficos/' + nome + '.png'
    teste1 = verificaExistencia(nome_teste1)
    nome_teste2 = 'Graficos/' + nome + '(1)' + '.png'
    teste2 = verificaExistencia(nome_teste2)
    if teste1 == True:
        number = 1
        if teste2 == False:
            nome = nome + f'({number})'
        else:
            nome = nome + '(1)'
            number = 2
            while True:
                if teste2 == False:
                    break
                nome = nome.replace(f'({number - 1})','')
                nome = nome + f'({number})'
                nome_teste2 = 'Graficos/' + nome + '.png'
                teste2 = verificaExistencia(nome_teste2)
                number = number + 1

        grafico.savefig('Graficos/' + nome + '.png', format='png')

    else:
        grafico.savefig('Graficos/' + nome + '.png', format='png')

def mostraGrafico(grafico):
    grafico.show()