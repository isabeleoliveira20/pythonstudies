#Os quatro tipos numéricos simples, utilizados em Python, são números inteiros (int),
#números longos (long), números decimais (float) e números complexos (complex).

#Exercicios Operadores Numéricos

#1 - Qual resultado da equação Z = (x²+y²)/((x-y)²) ?

x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

valor1 = (x ** 2 + y ** 2)  
valor2 = (x-y)**2

z = valor1/valor2

print("O valor final da equação Z = (x²+y²)/((x-y)²) é igual a = ", z)



#2 - Escreva um programa que receba o salário de um funcionário (float), 
#e retorne o resultado do novo salário com reajuste de 35%.

salario = float(input("Insira seu salário atual: "))
novo_salario = salario + (salario * 0.35)

print("Seu salário com reajuste de 35% ficará em: R$", novo_salario)