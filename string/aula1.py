
print("Esse é o registro do meu estudo em Python!")

#tipos de variaveis 
a = 10 #tipo inteiro
b = 1.2 #float
c = "Olá" #string
print(a,b,c)


#usuário atribuindo valor a uma variável
nome = input("Insira seu nome completo: ") #input sempre retorna em string


#como retornar dados do tipo inteiro ou float?
#convertendo o tipo do valor lido
idade = int(input("Qual a sua idade?"))

altura = float(input("Insira sua altura:"))

print("Dados do Atleta:","Nome:", nome, "Idade:", idade, "Altura:", altura)


#concatenar strings
a='Olá'
b='Mundo'
c= a+b
print (c)


#Manipulação de string
teste = "Apostila de Python"
print(len(teste)) #len() = tamanho da string

a= "isabele"
print(a.capitalize()) #capitalize() = retorna inicial maiuscula

b= "bebe"
print(b.count("b")) #count() = retorna qtd vezes que um caractere aparece

print(b.startswith("b")) #verifica se uma string inicia com uma sequencia

print(b.endswith("b")) #verifica fim da string

#isalnum() - verifica se a string possui alfanumerico

#isalpha() - verifica se a string possui apenas alfabetico

#islower() - verifica se toda a string é minuscula

#split() - transforma string em lista

#replace(s1, s2) - substitui uma string

#find() - retorna indice de um caractere, se o caractere não constar retorna -1


#Fatiamento de String
#Usado para extrair apenas uma parte dos elementos de uma String
#Sintaxe: Nome_String [Limite_Inferior : Limite_Superior]
#Retorna string com as posições do limite inferior até o limite superior -1
s = "Python"
print(s[1:4]) #seleciona posição 1, 2, 3
print(s[2:]) #elementos a partir da posição 2
print(s[:4]) #elementos até a posição 3

