from PySimpleGUI import PySimpleGUI as simple
from barras import montaGraficoBarras
from pizza import montaGraficoPizza
from barras_horizontais import montaGraficoBarrasH
from barras_agrupadas import montaGraficoBarrasA
from tratamento import verificaExistencia,salvaGrafico,mostraGrafico
class Interface:

    def __init__(self,grafico=None,layout=None,janela=None):
        self.layout = layout
        self.janela = janela
        self.grafico = grafico

    def telaPricipal(self):
        flag = ''
        simple.theme('Reddit')
        layout = [
            [simple.Text('Aviso: Coloque os dados na pasta "Dados" na mesma pasta do programa em formato xslx.')],
            [simple.Text('(Lembre que cada coluna de seus dados devem ter titulo para que os dados sejam organizados corretamente)')],
            [simple.Text('Escolha qual tipo de gráfico deseja criar')],
            [simple.Button('Barras'), simple.Button('Pizza'), simple.Button('Barras horizontais'),simple.Button('Barras agrupadas')]
        ]

        janela = simple.Window('Tela principal',layout)

        while True:

            self.janela = janela

            eventos, valores = self.janela.read()

            if eventos == simple.WINDOW_CLOSED:
                break

            if eventos == 'Barras':
                self.janela.close()
                layout = [
                    [simple.Text('Nome do arquivo de dados'),simple.Input(key='nome',size=(20,1))],
                    [simple.Text('Titulo do gráfico'),simple.Input(key='titulo',size=(20,1))],
                    [simple.ButtonMenu('Cor do gráfico',[['Não serve para nada'],['blue','red','green','purple','pink','yellow','white','black','gray','orange','brown','silver','beige']],key='cor')],
                    [simple.Button('Visualizar gráfico'),simple.Button('Salvar gráfico'),simple.Button('Voltar')]
                ]
                janela = simple.Window('Configurações',layout)
                flag = 'Barras'

            if eventos == 'Pizza':
                self.janela.close()
                layout = [
                    [simple.Text('Nome do arquivo de dados'), simple.Input(key='nome', size=(20, 1))],
                    [simple.Text('Titulo do gráfico'), simple.Input(key='titulo', size=(20, 1))],
                    [simple.Button('Visualizar gráfico'), simple.Button('Salvar gráfico'), simple.Button('Voltar')]
                ]
                janela = simple.Window('Configurações', layout)
                flag = 'Pizza'

            if eventos == 'Barras horizontais':
                self.janela.close()
                layout = [
                    [simple.Text('Nome do arquivo de dados'), simple.Input(key='nome', size=(20, 1))],
                    [simple.Text('Titulo do gráfico'), simple.Input(key='titulo', size=(20, 1))],
                    [simple.ButtonMenu('Cor do gráfico', [['Não serve para nada'],
                                                          ['blue', 'red', 'green', 'purple', 'pink', 'yellow', 'white',
                                                           'black', 'gray', 'orange', 'brown', 'silver', 'beige']],
                                       key='cor')],
                    [simple.Button('Visualizar gráfico'), simple.Button('Salvar gráfico'), simple.Button('Voltar')]
                ]
                janela = simple.Window('Configurações', layout)
                flag = 'Barras horizontais'

            if eventos == 'Barras agrupadas':
                self.janela.close()
                layout = [
                    [simple.Text('Nome do arquivo de dados'), simple.Input(key='nome', size=(20, 1))],
                    [simple.Text('Titulo do gráfico'), simple.Input(key='titulo', size=(20, 1))],
                    [simple.Text('Titulo eixo x'), simple.Input(key='titulox', size=(20, 1))],
                    [simple.Text('Titulo eixo y'), simple.Input(key='tituloy', size=(20, 1))],
                    [simple.Button('Visualizar gráfico'), simple.Button('Salvar gráfico'), simple.Button('Voltar')]
                ]
                janela = simple.Window('Configurações', layout)
                flag = 'Barras agrupadas'

            if eventos == 'Visualizar gráfico':
                nome_teste = 'Dados/' + valores['nome'] + '.xlsx'
                if valores['titulo'] == '' or valores['nome'] == '' or verificaExistencia(nome_teste) == False:
                    layout_aux = [
                        [simple.Text('Você não preencheu todos os campos corretamente, ou o arquivo não existe na pasta dados. Favor tentar novamente')],
                        [simple.Button('Okey')]
                    ]
                    janela_aux = simple.Window('Tela principal', layout_aux)

                    eventos_aux, valores_aux = janela_aux.read()

                    if eventos_aux == simple.WINDOW_CLOSED:
                        janela_aux.close()

                    if eventos_aux == 'Okey':
                        janela_aux.close()

                else:
                    if flag == 'Barras':
                        self.grafico = montaGraficoBarras(valores['titulo'],valores['cor'],valores['nome'])
                        mostraGrafico(self.grafico)

                    if flag == 'Pizza':
                        self.grafico = montaGraficoPizza(valores['nome'])
                        mostraGrafico(self.grafico)

                    if flag == 'Barras horizontais':
                        self.grafico = montaGraficoBarrasH(valores['titulo'],valores['cor'],valores['nome'])
                        mostraGrafico(self.grafico)

                    if flag == 'Barras agrupadas':
                        self.grafico = montaGraficoBarrasA(valores['titulo'],valores['titulox'],valores['tituloy'],valores['nome'])
                        mostraGrafico(self.grafico)

            if eventos == 'Salvar gráfico':
                nome_teste = 'Dados/' + valores['nome'] + '.xlsx'
                if valores['titulo'] == '' or valores['nome'] == '' or verificaExistencia(nome_teste) == False:
                    layout_aux = [
                        [simple.Text('Você não preencheu todos os campos corretamente, ou o arquivo não existe na pasta dados. Favor tentar novamente')],
                        [simple.Button('Okey')]
                    ]
                    janela_aux = simple.Window('Tela principal', layout_aux)

                    eventos_aux, valores_aux = janela_aux.read()

                    if eventos_aux == simple.WINDOW_CLOSED:
                        janela_aux.close()

                    if eventos_aux == 'Okey':
                        janela_aux.close()

                else:
                    if flag == 'Barras':
                        self.grafico = montaGraficoBarras(valores['titulo'], valores['cor'], valores['nome'])
                        salvaGrafico(self.grafico,valores['titulo'])

                    if flag == 'Pizza':
                        self.grafico = montaGraficoPizza(valores['nome'])
                        salvaGrafico(self.grafico,valores['titulo'])

                    if flag == 'Barras horizontais':
                        self.grafico = montaGraficoBarrasH(valores['titulo'], valores['cor'], valores['nome'])
                        salvaGrafico(self.grafico,valores['titulo'])

                    if flag == 'Barras agrupadas':
                        self.grafico = montaGraficoBarrasA(valores['titulo'], valores['titulox'], valores['tituloy'],valores['nome'])
                        salvaGrafico(self.grafico,valores['titulo'])

                    self.janela.close()
                    layout = [
                        [simple.Text(
                            'Aviso: Coloque os dados na pasta "Dados" na mesma pasta do programa em formato xslx.')],
                        [simple.Text(
                            '(Lembre que cada coluna de seus dados devem ter titulo para que os dados sejam organizados corretamente)')],
                        [simple.Text('Escolha qual tipo de gráfico deseja criar')],
                        [simple.Button('Barras'), simple.Button('Pizza'), simple.Button('Barras horizontais'),
                         simple.Button('Barras agrupadas')]
                    ]
                    janela = simple.Window('Tela principal', layout)

            if eventos == 'Voltar':
                self.janela.close()
                layout = [
                    [simple.Text(
                        'Aviso: Coloque os dados na pasta "Dados" na mesma pasta do programa em formato xslx.')],
                    [simple.Text(
                        '(Lembre que cada coluna de seus dados devem ter titulo para que os dados sejam organizados corretamente)')],
                    [simple.Text('Escolha qual tipo de gráfico deseja criar')],
                    [simple.Button('Barras'), simple.Button('Pizza'), simple.Button('Barras horizontais'),
                     simple.Button('Barras agrupadas')]
                ]
                janela = simple.Window('Tela principal',layout)

