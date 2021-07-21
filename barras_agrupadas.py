import matplotlib.pyplot as plt
import numpy as np
from tratamento import tratamentoDados

class BarrasAgrupadas:

    def __init__(self,dados,names,identificadores,title,title_x,title_y,):
        self.dados = dados
        self.names = names
        self.identificadores = identificadores
        self.title = title
        self.title_x = title_x
        self.title_y = title_y
        self.bar_width = 0.8
        self.plt = plt

    def criaGrafico(self):
        n = len(self.dados)
        aux_identificadores = np.arange(len(self.identificadores))
        self.plt.figure(figsize=(15,6))
        for i in range (n):
            self.plt.bar(aux_identificadores - self.bar_width/2. + i / float(n) * self.bar_width,self.dados[i],width=self.bar_width/float(n),align="edge",label=self.names[i])
        self.plt.xticks(aux_identificadores,self.identificadores)
        self.plt.xlabel(self.title_x)
        self.plt.ylabel(self.title_y)
        self.plt.title(self.title)
        self.plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        return self.plt


def montaGraficoBarrasA(titulo,titulo_x,titulo_y,nome_arquivo):
    lista,titulos = tratamentoDados('Dados/'+ nome_arquivo +'.xlsx')
    dados = []
    names = []
    for i in range(len(lista)):
        if i != 0:
            dados.append(list(lista[i]))

    for nome in titulos:
        if nome != 'Unnamed: 0':
            names.append(nome)

    identificadores = lista[0]

    grafico = BarrasAgrupadas(dados,names,identificadores,titulo,titulo_x,titulo_y).criaGrafico()
    return grafico