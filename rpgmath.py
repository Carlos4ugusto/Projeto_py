import tkinter as tk
import random

# 🎭 Classe do Personagem
class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.nivel = 1
        self.pontos = 0
        self.vida = 100
        self.forca = 10 if classe == "Guerreiro" else 5
        self.magia = 10 if classe == "Mago" else 5
        self.agilidade = 10 if classe == "Arqueiro" else 5

    def upgrade(self):
        self.nivel += 1
        self.vida += 10
        self.pontos += 5
        if self.classe == "Guerreiro":
            self.forca += 5
        elif self.classe == "Mago":
            self.magia += 5
        elif self.classe == "Arqueiro":
            self.agilidade += 5

# 🧮 Banco de Perguntas
perguntas = [
    ("Quanto é 12 x 8?", "96"), ("Qual a raiz quadrada de 144?", "12"), ("Resolva: 5²", "25"),
    ("Quanto é 100 ÷ 4?", "25"), ("Resolva: 3³", "27"), ("Qual a fórmula da área do triângulo?", "base x altura ÷ 2"),
    ("Quanto é 15% de 200?", "30"), ("Resolva: 7 x 9", "63"), ("Quanto é 81 ÷ 9?", "9"),
    ("Qual a raiz cúbica de 27?", "3"), ("Resolva: 6²", "36"), ("Quanto é 11 x 11?", "121"),
    ("Resolva: 2³", "8"), ("Quanto é 25 ÷ 5?", "5"), ("Qual a fórmula da área do círculo?", "pi x raio²"),
    ("Quanto é 20% de 150?", "30"), ("Resolva: 9 x 6", "54"), ("Quanto é 64 ÷ 8?", "8"),
    ("Qual a raiz quadrada de 169?", "13"), ("Resolva: 4³", "64"), ("Quanto é 14 x 5?", "70"),
    ("Quanto é 90 ÷ 10?", "9"), ("Qual a raiz quadrada de 225?", "15"), ("Resolva: 10²", "100"),
    ("Quanto é 18 x 3?", "54"), ("Quanto é 72 ÷ 8?", "9"), ("Qual a raiz quadrada de 196?", "14"),
    ("Resolva: 8²", "64"), ("Quanto é 13 x 7?", "91"), ("Quanto é 120 ÷ 12?", "10"),
    ("Qual a raiz quadrada de 256?", "16"), ("Resolva: 9²", "81"), ("Quanto é 16 x 4?", "64"),
    ("Quanto é 100 ÷ 25?", "4"), ("Qual a raiz quadrada de 100?", "10"), ("Resolva: 5³", "125"),
    ("Quanto é 6 x 7?", "42"), ("Quanto é 81 ÷ 3?", "27"), ("Qual a raiz quadrada de 289?", "17"),
    ("Resolva: 11²", "121"), ("Quanto é 8 x 8?", "64"), ("Quanto é 144 ÷ 12?", "12"),
    ("Qual a raiz quadrada de 324?", "18"), ("Resolva: 12²", "144"), ("Quanto é 9 x 5?", "45"),
    ("Quanto é 36 ÷ 6?", "6"), ("Qual a raiz quadrada de 49?", "7"), ("Resolva: 7²", "49"),
    ("Quanto é 10 x 10?", "100"), ("Quanto é 30 ÷ 5?", "6")
]

# 🎮 Interface do Jogo
class JogoMatematica:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG de Matemática")
        self.root.geometry("800x600")  # 📐 Janela maior
        self.FONTE = ("Arial", 14)     # 🔠 Fonte padrão
        self.personagem = None
        self.pergunta_atual = None
        self.tempo_restante = 60
        self.timer_label = None
        self.timer_id = None
        self.frame_inicio()

    def frame_inicio(self):
        self.clear()
        tk.Label(self.root, text="Nome do personagem:", font=self.FONTE).pack(pady=5)
        self.nome_entry = tk.Entry(self.root, font=self.FONTE)
        self.nome_entry.pack(pady=5)

        tk.Label(self.root, text="Escolha sua classe:", font=self.FONTE).pack(pady=5)
        self.classe_var = tk.StringVar(value="Guerreiro")
        for classe in ["Guerreiro", "Mago", "Arqueiro"]:
            tk.Radiobutton(self.root, text=classe, variable=self.classe_var, value=classe, font=self.FONTE).pack()

        tk.Button(self.root, text="Iniciar Jogo", font=self.FONTE, command=self.iniciar_jogo).pack(pady=10)

    def iniciar_jogo(self):
        nome = self.nome_entry.get()
        classe = self.classe_var.get()
        self.personagem = Personagem(nome, classe)
        self.frame_jogo()

    def frame_jogo(self):
        self.clear()
        self.status_label = tk.Label(self.root, text=self.status_text(), font=self.FONTE)
        self.status_label.pack(pady=5)

        self.pergunta_atual = random.choice(perguntas)
        tk.Label(self.root, text=self.pergunta_atual[0], font=self.FONTE).pack(pady=10)
        self.resposta_entry = tk.Entry(self.root, font=self.FONTE)
        self.resposta_entry.pack(pady=5)
        tk.Button(self.root, text="Responder", font=self.FONTE, command=self.verificar_resposta).pack(pady=10)

        self.tempo_restante = 60
        self.timer_label = tk.Label(self.root, text=f"⏳ Tempo restante: {self.tempo_restante}s", font=self.FONTE)
        self.timer_label.pack(pady=5)
        self.atualizar_timer()

    def atualizar_timer(self):
        self.timer_label.config(text=f"⏳ Tempo restante: {self.tempo_restante}s")
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.timer_id = self.root.after(1000, self.atualizar_timer)
        else:
            self.verificar_resposta(timeout=True)

    def verificar_resposta(self, timeout=False):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        if timeout:
            self.personagem.vida -= 20
            resultado = f"⏰ Tempo esgotado! Resposta correta: {self.pergunta_atual[1]}"
        else:
            resposta = self.resposta_entry.get().strip().lower()
            correta = self.pergunta_atual[1].strip().lower()
            if resposta == correta:
                self.personagem.pontos += 10
                if self.personagem.pontos % 50 == 0:
                    self.personagem.upgrade()
                resultado = "✅ Correto!"
            else:
                self.personagem.vida -= 20
                resultado = f"❌ Errado! Resposta correta: {self.pergunta_atual[1]}"
        self.frame_resultado(resultado)

    def frame_resultado(self, resultado):
        self.clear()
        tk.Label(self.root, text=resultado, font=self.FONTE).pack(pady=10)
        tk.Label(self.root, text=self.status_text(), font=self.FONTE).pack(pady=5)
        if self.personagem.vida <= 0:
            tk.Label(self.root, text="💀 Game Over!", font=self.FONTE).pack(pady=10)
        else:
            tk.Button(self.root, text="Próxima Pergunta", font=self.FONTE, command=self.frame_jogo).pack(pady=10)

    def status_text(self):
        p = self.personagem
        return f"{p.nome} | Classe: {p.classe} | Nível: {p.nivel} | Pontos: {p.pontos} | Vida: {p.vida}"

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# 🚀 Executar o jogo
root = tk.Tk()
app = JogoMatematica(root)
root.mainloop()
