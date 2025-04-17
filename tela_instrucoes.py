import tkinter as tk
from utilitarios import resetaTela
from tela_jogo import TelaJogo

class TelaInstrucoes:
    def __init__(self, root):
        self.root = root

    def frameTelaInstrucoes(self):
        resetaTela(self.root)
        self.root.title("The Math Game")

        titulo = tk.Label(self.root, text="Instruções do Jogo", font=("Arial", 24))
        titulo.pack(pady=50)

        texto = tk.Label(
            self.root,
            text="Clique na operação que corresponde ao resultado entre os dois números mostrados.\nOperações: |+|-|x|÷|",
            font=("Arial", 14),
            justify="center"
        )
        texto.pack(pady=10)

        botao_play = tk.Button(
            self.root,
            text="Jogar",
            font=("Arial", 16),
            width=10,
            height=2,
            command=self.abrirTelaJogo
        )
        botao_play.pack(pady=20)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: \nMaria Luíza, Ana Clara e Gabriel(Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

    def abrirTelaJogo(self):
        TelaJogo(self.root).frameTelaJogo()
