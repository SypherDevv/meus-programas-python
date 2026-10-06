#Tarefa 24 / Maior número da lista =====================
print('================= #Tarefa 24 ====================')

numeros = [10, 25, 7, 40, 15]
maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
        
        
print('Esse é o maior número da lista', maior)