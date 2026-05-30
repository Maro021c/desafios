numero = int(input("qual número quer saber a tabuada?"))

for x in range (1, 11):
    resultado = numero * x
    print(f"{numero} x {x} = {resultado}")