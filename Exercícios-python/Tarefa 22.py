#Tarefa 22 / Somando números com while =========================
print('===================== Somando números com while =========================')

soma = 0
numeral = 1

while numeral != 0:
    numeral = int(input('Digite um número para somar: '))
    soma = soma + numeral

print(soma)