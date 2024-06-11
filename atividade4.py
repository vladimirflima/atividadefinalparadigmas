import tkinter as tk
from tkinter import ttk

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro Digital")

        self.tempo = 0
        self.executando = False

        self.label = ttk.Label(root, text=self.formatar_tempo(self.tempo), font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.botao_iniciar = ttk.Button(root, text="Iniciar", command=self.iniciar)
        self.botao_iniciar.pack(side="left", padx=20)

        self.botao_parar = ttk.Button(root, text="Parar", command=self.parar)
        self.botao_parar.pack(side="left", padx=20)

        self.botao_resetar = ttk.Button(root, text="Resetar", command=self.resetar)
        self.botao_resetar.pack(side="left", padx=20)

    def formatar_tempo(self, tempo):
        minutos = int(tempo / 60)
        segundos = int(tempo % 60)
        return f"{minutos:02}:{segundos:02}"

    def atualizar_tempo(self):
        if self.executando:
            self.tempo += 1
            self.label.config(text=self.formatar_tempo(self.tempo))
            self.root.after(1000, self.atualizar_tempo)

    def iniciar(self):
        if not self.executando:
            self.executando = True
            self.atualizar_tempo()

    def parar(self):
        if self.executando:
            self.executando = False

    def resetar(self):
        self.executando = False
        self.tempo = 0
        self.label.config(text=self.formatar_tempo(self.tempo))

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()
