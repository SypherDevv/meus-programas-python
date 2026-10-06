#Tarefa 18 / Soma de 1 ao 100 =================================
print('==================== #Tarefa 18 / Soma de 1 ao 100 =================================')

contador = 1
soma = 0
                                        #info o comando 'end='serve para definir o que o print() vai colocar no final da mensagem, 
                                        #info em vez de pular automaticamente para a próxima linha.
while contador <= 100:
    print(contador, end=' + ')

    soma = soma + contador
    contador = contador + 1

print('= ', soma)