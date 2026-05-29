#pergunta o número que a pessoa quer saber se é primo
numero = int(input("qual numero quer saber?"))
#variável de controle
veredito = 0
#repete o codígo de acordo com o número inserido, começando pelo 1
for x in range (1, numero):
    #salva a sobra da divisão do número escolhido pelo número da tentativa (x)
    resultado = numero % x
    #verifica se o resultado é igual a 0 
    if resultado == 0:
        #se o resultado for igual a 0 adiciona 1 na variavel de controle
        veredito = veredito + 1
#se "veredito" for igual ou menor que 1 significa que o número é primo
if veredito <= 2:
    print(f"{numero} é primo!")
#caso "veredito" seja maior que 2 significa que i número nao é primo
else:
    print(f"{numero} não é primo!")