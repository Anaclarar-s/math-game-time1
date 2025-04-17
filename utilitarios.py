# utilitarios.py
def resetaTela(root):
    for widget in root.winfo_children():
        widget.destroy()

# Este módulo contém funções auxiliares utilizadas em diferentes partes do jogo.
# A função resetaTela limpa todos os widgets da janela principal para permitir a troca de telas.
