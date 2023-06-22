# Aluno: Maria Eduarda Sanches de Oliveira Lima - Questão: A Resposta de Theon
# Explicação:Primeiro coloquei uma variável com input para o usuário colocar o
# número de pessoas e outra variável com input e split para colocar o número de cada pessoa,
# split para separar os número.Depois criei um for para percorrer a quantidade de numero
# de cada pessoas, e criei uma lista onde ia adiconando os valores do número de cara pessoas,
# fiz uma variável com o metodo min para colocar o menor número da lista e por fim fiz outa variável
# para mostras a posição e imprimi a posição mais um, porque começa com 0.
n = int(input("Digite o número de pessoas: "))
pessoas = []

for c in range(0,n):
    t = int(input("Digite o número de cada pessoas: "))
    pessoas.append(t)
menor = min(pessoas)
posicao = pessoas.index(menor)
print("Posição: ",posicao+1)

