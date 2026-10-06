#Tarefa 9 / Conversão de temperatura ==========================================
print('==================== #Tarefa 9 / Conversão de temperatura ==========================================')

Celsius = (float(input('Digite a temperatura de hoje: ')))
Fahrenheit = (Celsius *  9/5) + 32
Kelvin = ((Fahrenheit - 32) * 5/9 + 273.15)
print('A temperatura em Fahrenheit é de',Fahrenheit,'F')
print('A temperatura em Kelvin é de',Kelvin,'K')