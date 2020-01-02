
#a2 + bx + c
# (-b +- sqrt(b2-4ac))/2

from math import sqrt

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)

x1 = (-b + raiz_delta)/(2*a)
x2 = (-b - raiz_delta)/(2*a)

print("x1 = %f" %x1)
print("x2 = %f" %x2)

#nos prints colocando %d aparece número decimal
#se trocar pelo %f aparece número em float. Nesse caso a conta deu certo colocou parenteses no (2*a)






