import tkinter as tk

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return x / y

def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operacao = var_operacao.get()

    try:
        if operacao == 'soma':
            resultado = soma(num1, num2)
        elif operacao == 'subtracao':
            resultado = subtracao(num1, num2)
        elif operacao == 'multiplicacao':
            resultado = multiplicacao(num1, num2)
        elif operacao == 'divisao':
            resultado = divisao(num1, num2)
        else:
            resultado = "Operação inválida."
        
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError as e:
        label_resultado.config(text=e)

app = tk.Tk()
app.title("Calculadora")

label_num1 = tk.Label(app, text="Primeiro número:")
label_num1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_num1 = tk.Entry(app)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(app, text="Segundo número:")
label_num2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_num2 = tk.Entry(app)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operacao = tk.Label(app, text="Operação:")
label_operacao.grid(row=2, column=0, padx=10, pady=10, sticky="e")

var_operacao = tk.StringVar(app)
var_operacao.set("soma")

opcoes_operacoes = [
    ("Soma", "soma"),
    ("Subtração", "subtracao"),
    ("Multiplicação", "multiplicacao"),
    ("Divisão", "divisao")
]

for text, value in opcoes_operacoes:
    rb = tk.Radiobutton(app, text=text, variable=var_operacao, value=value)
    rb.grid(column=1, padx=10, pady=5, sticky="w")

botao_calcular = tk.Button(app, text="Calcular", command=calcular)
botao_calcular.grid(row=4, column=1, padx=10, pady=10, sticky="e")

label_resultado = tk.Label(app, text="")
label_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
