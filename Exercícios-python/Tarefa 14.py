#Tarefa 14 / Aprovação do aluno ============================
print('============= Tarefa 14 / Aprovação do aluno ===================')

media = float(input("Digite a média do aluno: "))

if media >= 7:
    print("Parabéns você foi aprovado!")

elif media >= 5:
    print("Você está de recuperação, estude mais um pouco!")

else:
    print("Infelizmente você foi reprovado!")