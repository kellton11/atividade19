# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

n = int(input("digite um número para calcular seu fatorial: "))
c = n
f = 1
print("calculando {}! = ".format(n), end="")
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print("{}".format(f))
    
