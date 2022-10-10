import random
import PySimpleGUI as sg

class SimuladorDeDado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'

        # layout
        self.layout = [
            [sg.Text('Você Gostaria de Jogar?')],
            [sg.Button('Sim'),sg.Button('Não')]
        ]
        
    def iniciar(self):
        # janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler os eventos da tela
        self.eventos,self.valores = self.janela.Read()
        try:
                if self.eventos == 'Sim' or self.eventos == 's':
                    self.gerarvalordodado()
                elif self.eventos == 'Não' or self.eventos == 'n':
                    print('Agradecemos sua participação!')
                else:
                    print('Por favor digite sim ou não')
        except:
                print('Ocorreu um erro ao receber sua resposta')

    def gerarvalordodado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.iniciar()

