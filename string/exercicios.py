
#Exercícios string

#1Considere a string A = "Um elefante incomoda muita gente". 
#Que fatia corresponde a "elefante incomoda"?


a = "Um elefante incomoda muita gente"
print(a[3:20])


#2 - Escreva um programa que solicite uma frase ao usuário e 
#escreva a frase toda em maiúscula e sem espaços em branco.

frase = input("Insira uma frase:")

print(frase.replace(" ", ""))

frase_maiuscula = frase
print(frase_maiuscula.upper())


#3 - Dada a string frase2 = "Aprender Python é divertido",
#escreva um código que conte quantas vezes aparece a letra "r".

frase2 = "Aprender Python é divertido"
print(frase2.count("r"))


#4 - Dada a string texto = "Eu gosto de programar", produza uma nova string 
#onde as palavras aparecem invertidas, ficando "programar de gosto Eu".

texto = "Eu gosto de programar"
a = "Eu"
b = "Gosto"
c = "de"
d = "programar"

texto_novo = d + " " + c + " " + b + " " + a

print(texto_novo)


#resolução menos manual
texto = "Te amo"

lista = texto.split()
inversao = lista[::-1]
texto_novo = " ".join(inversao)

print(texto_novo)


#5 - Na string mensagem = "O céu está azul", substitua "azul" por "vermelho".

mensagem = "O céu está azul"
print(mensagem)

nova_mensagem = mensagem.replace("azul", "vermelho")
print(nova_mensagem)


