# Aluno: Maria Eduarda Sanches de Oliveira Lima - Questão: Intervalo
# Explicação: Primeiro coloquei uma variável com input para o usuário colocar o valor,
# depois usei o if, elif e else para verificar qual é o intevalo do valor, se o valor estiver dentro de
# um intervalo o programa imprime qual o intervalo do valor, caso o valor não estiver dentro de nem um
# intervalo o programa imprimirá "Fora de intervalo" como é pedido na atividade
v = float(input("Digite o valor: "))

if v >= 0 and v <= 25:
    print("Intervalo (0,25]")
elif v > 25 and v <= 50:
    print("Intervalo (25,50]")
elif v > 50 and v <= 75:
    print("Intervalo (50,75]")
elif v > 75 and v <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")