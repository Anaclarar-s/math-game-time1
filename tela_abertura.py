import tkinter as tk
from utilitarios import resetaTela
from tela_instrucoes import TelaInstrucoes

class TelaInicial:
    def __init__(self, root):
        self.root = root

    def frameTelaInicial(self):
        resetaTela(self.root)
        self.root.title("The Math Game")

        titulo = tk.Label(self.root, text="The Math Game", font=("Arial", 32))
        titulo.pack(pady=60)

        botao_jogar = tk.Button(
            self.root,
            text="Jogar",
            font=("Arial", 16),
            width=15,
            height=2,
            command=self.abrirTelaInstrucoes
        )
        botao_jogar.pack(pady=10)

        botao_sair = tk.Button(
            self.root,
            text="Sair",
            font=("Arial", 16),
            width=15,
            height=2,
            command=self.root.destroy
        )
        botao_sair.pack(pady=10)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: \nMaria Luíza, Ana Clara e Gabriel(Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

    def abrirTelaInstrucoes(self):
        TelaInstrucoes(self.root).frameTelaInstrucoes()
