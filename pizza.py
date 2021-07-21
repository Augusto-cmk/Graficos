import matplotlib.pyplot as plt
from tratamento import tratamentoDados

class Pizza:

    def __init__(self,names,informacoes):
        self.nomes = names
        self.informacoes = informacoes
        self.plt = plt

    def criaGrafico(self):
        fig,plotagem = self.plt.subplots()
        plotagem.pie(self.informacoes,labels = self.nomes,autopct='%1.1f%%',shadow=True,startangle=90)
        plotagem.axis('equal')
        return self.plt

def montaGraficoPizza(nome_arquivo):#relação de 1 para 1
    lista,titulos = tratamentoDados('Dados/'+ nome_arquivo +'.xlsx')
    nomes = lista[0]
    informacoes = lista[1]
    grafico = Pizza(nomes,informacoes).criaGrafico()
    return grafico

