"""
Lista 1, parte 1, exercício 9

Descrição: Este programa apresenta a resolução da questão 9 da parte 1 da lista 1 da cadeira de Economia Computacional
Autor:Arthur Kafrouni Tomazi
Data: 23/06/2023
Versão: 0.0.1
"""

# Problema: Resolva uma equação do segundo grau.

# Atribuição de variáveis

a = 0
b = 0
c = 0
x = 0
y1 = 0
y2= 0

# Entrada de dados

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
x = float(input("x: "))

# Processamento de dados

y1 = (-b + ((b**2) - 4*a*c)**(1/2)) / (2*a)
y2 = (-b - ((b**2) - 4*a*c)**(1/2)) / (2*a)

# Saída de dados

print(f'y1 é igual a {y1} e y2 é igual a {y2}')