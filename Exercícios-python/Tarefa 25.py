#Tarefa 25 / Menor número da lista =====================
print('================= #Tarefa 25 ====================')

numeros = [10, 25, 7, 40, 15]
menor = numeros[0]
for numero in numeros:
    if numero < menor:
        menor = numero
        
        
print('Esse é o menor número da lista', menor)