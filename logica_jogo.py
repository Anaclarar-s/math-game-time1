import tkinter as tk
from utilitarios import resetaTela
import random

class DadosFuncionais:
    @staticmethod
    def gerarNumeros():
        return random.randint(1, 10), random.randint(1, 10)

    @staticmethod
    def selecionaOperador():
        return random.choice(['+', '-', 'x', '÷'])

    @staticmethod
    def calculaResultado(n1, n2, operador):
        if operador == '+':
            return n1 + n2
        elif operador == '-':
            return n1 - n2
        elif operador == 'x':
            return n1 * n2
        elif operador == '÷':
            return round(n1 / n2, 2) if n2 != 0 else 0

class FinalJogo:
    def __init__(self, root, pontos=0, acertos=0, partidas=0):
        self.root = root
        self.pontos = pontos
        self.acertos = acertos
        self.partidas = partidas

    def frameFimJogo(self):
        resetaTela(self.root)
        self.root.title("The Math Game")

        titulo = tk.Label(self.root, text="Fim do jogo!", font=("Arial", 24))
        titulo.pack(pady=50)

        texto = tk.Label(
            self.root,
            text=f"Parabéns pela partida!\nVocê marcou {self.pontos} pontos e acertou {self.acertos} de {self.partidas} partidas!",
            font=("Arial", 14)
        )
        texto.pack(pady=10)

        botao_play = tk.Button(
            self.root,
            text="Jogar Novamente",
            command=self.abrirTelaInstrucoes,
            font=("Arial", 16),
            width=15,
            height=2
        )
        botao_play.pack(pady=20)

        botao_sair = tk.Button(
            self.root,
            text="Sair do Jogo",
            command=self.sairJogo,
            font=("Arial", 16),
            width=15,
            height=2
        )
        botao_sair.pack(pady=10)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: \nMaria Luíza, Ana Clara e Gabriel(Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

    def abrirTelaInstrucoes(self):
        from tela_instrucoes import TelaInstrucoes
        TelaInstrucoes(self.root).frameTelaInstrucoes()

    def sairJogo(self):
        self.root.running = False
        self.root.destroy()
