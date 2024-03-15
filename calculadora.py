from tkinter import *

janela = Tk()

numero1 = ""
numero2 = ""

janela.title("Calculadora")
janela.geometry("420x355")
janela.configure(background=("white"))
janela.resizable(0,0)

e = Entry(janela, width=15, borderwidth=4, relief=FLAT, fg="black", bg="#EEEEEE", font=("futura", 25, "bold"), justify=CENTER)

e.grid(row=0, column=0, columnspan=4, pady=2)


def botao_click(num):
    e.insert(END, num)
    return


def botaoDivisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)


divisao = Button(janela, text="÷", padx=40, pady=20, command=botaoDivisao, bg='white', relief=FLAT, font=("futura", 12, "bold"))
divisao.grid(row=0, column=4)


def botaoSoma():
    global numero1
    global soma
    soma = TRUE
    numero1 = e.get()
    e.delete(0, END)


soma = Button(janela, text="+", padx=40, pady=20, command=botaoSoma, bg='white', relief=FLAT, font=("futura", 12, "bold"))
soma.grid(row=3, column=4)


def botaoSubtracao():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)


subtracao = Button(janela, text="–", padx=40, pady=20, command=botaoSubtracao, bg='white', relief=FLAT, font=("futura", 12, "bold"))
subtracao.grid(row=2, column=4)


def botaoMulticacao():
    global numero1
    global multiplicacao
    multiplicacao = TRUE
    numero1 = e.get()
    e.delete(0, END)


multiplicacao = Button(janela, text="x", padx=40, pady=20, command=botaoMulticacao, bg='white', relief=FLAT, font=("futura", 12, "bold"))
multiplicacao.grid(row=1, column=4)


def botaoIgual():
    global soma
    global subtracao
    global divisao
    global multiplicacao
    numero2 = e.get()
    e.delete(0, END)
    if soma == TRUE:
        e.insert(0, float(numero1) + float(numero2))
        soma = FALSE
    elif subtracao == TRUE:
        e.insert(0, float(numero1) - float(numero2))
        subtracao = FALSE
    elif multiplicacao == TRUE:
        e.insert(0, float(numero1) * float(numero2))
        multiplicacao = FALSE
    elif divisao == TRUE:
        e.insert(0, float(numero1) / float(numero2))
        divisao = FALSE


igual = Button(janela, text="=", padx=40, pady=20, command=botaoIgual, bg='white', relief=FLAT, font=("futura", 12, "bold"))
igual.grid(row=4, column=4)


def botaoClear():
    e.delete(0, END)


clear = Button(janela, text="AC", padx=40, pady=20, command=botaoClear, bg='white', relief=FLAT, font=("futura", 12, "bold"))
clear.grid(row=4, column=2)

# Botão Vírgula (,)
virgula = Button(janela, text=",", padx=40, pady=20, command=lambda: botao_click(
    "."), bg='white', relief=FLAT, font=("futura", 12, "bold"))
virgula.grid(row=4, column=1)

# Botão 1
um = Button(janela, text="1", padx=40, pady=20, command=lambda: botao_click(
    1), bg='white', relief=FLAT, font=("futura", 12, "bold"))
um.grid(row=1, column=0)

# Botão 2
dois = Button(janela, text="2", padx=40, pady=20, command=lambda: botao_click(
    2), bg='white', relief=FLAT, font=("futura", 12, "bold"))
dois.grid(row=1, column=1)

# Botão 3
tres = Button(janela, text="3", padx=40, pady=20, command=lambda: botao_click(
    3), bg='white', relief=FLAT, font=("futura", 12, "bold"))
tres.grid(row=1, column=2)

# Botão 4
quatro = Button(janela, text="4", padx=40, pady=20, command=lambda: botao_click(
    4), bg='white', relief=FLAT, font=("futura", 12, "bold"))
quatro.grid(row=2, column=0)

# Botão 5
cinco = Button(janela, text="5", padx=40, pady=20, command=lambda: botao_click(
    5), bg='white', relief=FLAT, font=("futura", 12, "bold"))
cinco.grid(row=2, column=1)

# Botão 6
seis = Button(janela, text="6", padx=40, pady=20, command=lambda: botao_click(
    6), bg='white', relief=FLAT, font=("futura", 12, "bold"))
seis.grid(row=2, column=2)

# Botão 7
sete = Button(janela, text="7", padx=40, pady=20, command=lambda: botao_click(
    7), bg='white', relief=FLAT, font=("futura", 12, "bold"))
sete.grid(row=3, column=0)

# Botão 8
oito = Button(janela, text="8", padx=40, pady=20, command=lambda: botao_click(
    8), bg='white', relief=FLAT, font=("futura", 12, "bold"))
oito.grid(row=3, column=1)

# Botão 9
nove = Button(janela, text="9", padx=40, pady=20, command=lambda: botao_click(
    9), bg='white', relief=FLAT, font=("futura", 12, "bold"))
nove.grid(row=3, column=2)

# Botão 0
zero = Button(janela, text="0", padx=40, pady=20, command=lambda: botao_click(
    0), bg='white', relief=FLAT, font=("futura", 12, "bold"))
zero.grid(row=4, column=0)

janela.mainloop()