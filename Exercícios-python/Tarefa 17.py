#Tarefa 17 / Tabuada =======================================
print('==================== #Tarefa 17 / Tabuada =======================================')

number = int(input('Digite um número: '))

for i in range(1,11):                   #info o comando for i in range() conta até um número antes do último
    resultado = number * i              #info exemplo for i in range(1, 11) ele vai contar do 1 ao 10 apenas
    print(number, 'x', i, '=', resultado)