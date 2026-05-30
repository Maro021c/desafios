numero = int(input("escolha seu numero:"))
soma = 0
for x in range(numero + 1):
    print(x)
    resultado = x % 2
    if resultado == 0:
        soma += x
print(soma)