#Média
# soma dos valores / numero de valores

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a primeira nota:"))

media = (nota1+nota2)/2

print("Sua média é %f" %(media))

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
