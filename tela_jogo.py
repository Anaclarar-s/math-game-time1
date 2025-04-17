import tkinter as tk
import time
from utilitarios import resetaTela
from logica_jogo import DadosFuncionais, FinalJogo

class TelaJogo:
    def __init__(self, root):
        self.root = root
        self.tempo = 30
        self.timer_id = None
        self.pontos = 0
        self.acertos = 0
        self.partida_atual = 1

    def frameTelaJogo(self):
        resetaTela(self.root)
        self.root.title("The Math Game")

        self.num1, self.num2 = DadosFuncionais.gerarNumeros()
        self.operador_correto = DadosFuncionais.selecionaOperador()
        self.resultado = DadosFuncionais.calculaResultado(self.num1, self.num2, self.operador_correto)

        cabecalho = tk.Frame(self.root)
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Partida:").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, text=f"{self.partida_atual}/20").grid(row=0, column=1, padx=10)

        tk.Label(cabecalho, text="Pontuação:").grid(row=0, column=2, padx=10)
        tk.Label(cabecalho, text=str(self.pontos)).grid(row=0, column=3, padx=10)

        tk.Label(cabecalho, text="Tempo:").grid(row=0, column=4, padx=10)
        self.tempo_label = tk.Label(cabecalho, text=str(self.tempo), font=("Arial", 16))
        self.tempo_label.grid(row=0, column=5, padx=10)

        botao_parar = tk.Button(cabecalho, text="Parar", command=self.pararJogo)
        botao_parar.grid(row=0, column=6, padx=10)

        numeros_frame = tk.Frame(self.root)
        numeros_frame.pack(pady=40)
        tk.Label(numeros_frame, text=str(self.num1), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text="?", font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text=str(self.num2), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text="=", font=("Arial", 32)).pack(side="left", padx=10)
        tk.Label(numeros_frame, text=str(self.resultado), font=("Arial", 32)).pack(side="left", padx=10)

        operacoes_frame = tk.Frame(self.root)
        operacoes_frame.pack(pady=30)

        for op in ['+', '-', 'x', '÷']:
            tk.Button(
                operacoes_frame,
                text=op,
                font=("Arial", 16),
                width=5,
                height=2,
                command=lambda o=op: self.processarResposta(o)
            ).pack(side="left", padx=10)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: \nMaria Luíza, Ana Clara e Gabriel(Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

        self.contagemRegressiva()

    def contagemRegressiva(self):
        if self.tempo > 0:
            self.tempo -= 1
            self.tempo_label.config(text=str(self.tempo))
            self.timer_id = self.root.after(1000, self.contagemRegressiva)
        else:
            self.avancarPartida()

    def processarResposta(self, resposta):
        if resposta == self.operador_correto:
            self.pontos += 100
            self.acertos += 1
        self.avancarPartida()

    def avancarPartida(self):
        self.root.after_cancel(self.timer_id)
        if self.partida_atual < 20:
            self.partida_atual += 1
            self.tempo = 30
            self.frameTelaJogo()
        else:
            FinalJogo(self.root, self.pontos, self.acertos, self.partida_atual).frameFimJogo()

    def pararJogo(self):
        self.root.after_cancel(self.timer_id)
        FinalJogo(self.root, self.pontos, self.acertos, self.partida_atual).frameFimJogo()
