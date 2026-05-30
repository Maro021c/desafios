#pede uma palavra para o usuário
palavra = str(input("fale uma palavra:"))
#
vogais = "aeiou"
contador = 0
for x in palavra:
    for a in vogais:
        if x == a:
            contador += 1

print(contador)