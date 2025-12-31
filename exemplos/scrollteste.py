import tkinter as tk

janela = tk.Tk()
janela.title("Scrollbar")

frame = tk.Frame(janela)
frame.pack(fill=tk.BOTH, expand=True)


text = tk.Text(frame, wrap=tk.WORD)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text.configure(yscrollcommand=scrollbar.set)


for i in range(50):
    text.insert(tk.END, f"Linha {i + 1}\n")

janela.mainloop()