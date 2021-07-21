import matplotlib.pyplot as plt
from tratamento import tratamentoDados

class BarrasHorizontais:

    def __init__(self,titulo,cor,dados_x,dados_y,titulo_x,titulo_y):
        self.dados_y = dados_y
        self.dados_x = dados_x
        self.color_bar = cor
        self.title = titulo
        self.title_x = titulo_x
        self.title_y = titulo_y
        self.plt = plt

    def criaGrafico(self):
        self.plt.barh(self.dados_x,self.dados_y,color=self.color_bar)
        self.plt.ylabel(self.title_y)
        self.plt.xlabel(self.title_x)
        self.plt.title(self.title)
        return self.plt

def montaGraficoBarrasH(titulo,color,nome_arquivo):
    list,titulos = tratamentoDados('Dados/'+ nome_arquivo +'.xlsx')
    eixo_x = list[0]
    eixo_y = list[1]
    grafico = BarrasHorizontais(titulo,color, eixo_x, eixo_y,titulos[0],titulos[1]).criaGrafico()
    return grafico
