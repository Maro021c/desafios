#Variavel para 
clientes = int(input("quantos clientes serão cadastrados nessa sessão?:"))

nomes = []
valores = []
pipocas = []
idades = []

total_criança = 0
total_adolecente = 0
total_adulto = 0
total_idoso = 0
for cliente in range(clientes):

    nome = input("nome do cliente:")
    idade = int(input("idade do cliente:"))
    valor = float(input("valor de ingresso:"))
    pipoca = int(input("quantas pipocas:"))
    nomes.append(nome)
    idades.append(idade)
    valores.append(valor)
    pipocas.append(pipoca)
       
for idade in idades:

    if idade < 12:
     total_criança += 1 
      
    elif idade >= 12 and idade <= 17:
     total_adolecente += 1
    
    elif idade >=18 and idade <=59:
     total_adulto += 1
    
    else:
     total_idoso += 1

#feito por txt a partit daqui
total_pago = sum(valores)

print(total_pago)

faixa_etaria = str()

print(faixa_etaria)

n_comprou = []
comprou = []

for x in pipocas:
  if pipocas[x] == 0:
    n_comprou_pipoca = nomes[x]
    n_comprou.append(n_comprou_pipoca)
  else:
    comprou_pipoca = nomes [x]
    comprou.append(comprou_pipoca)

print(f"não compraram pipoca:{n_comprou}")
print(f"compraram pipoca:{comprou}")