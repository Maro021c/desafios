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
movimento = str(0)
if total_pago <= 499.99:
  movimento = "fraco"
elif total_pago >= 500.00 and total_pago <= 1499.99:
  movimento = "normal"
elif total_pago >= 1500.00:
  movimento = "excelente"

print(f"o total arrecadado foi de {total_pago} reais, o movimento foi {movimento}!")

faixa_etaria = max(total_adolecente, total_adulto, total_criança, total_idoso)
if faixa_etaria == total_criança:
    print("a faixa etaria principal é: infantil")
if faixa_etaria == total_adolecente:
    print("a faixa etaria principal é: adolecentes")
if faixa_etaria == total_adulto:
    print("a faixa etaria principal é: adultos")
if faixa_etaria == total_idoso:
    print("a faixa etaria principal é: idosos")

n_comprou = []
comprou = []

for x in pipocas:
  if x == 0:
    n_comprou_pipoca = nomes[x]
    n_comprou.append(n_comprou_pipoca)
  elif x >= 1:
    comprou_pipoca = nomes[x]
    comprou.append(comprou_pipoca)

if len(n_comprou) >= 1:
 print(f"não compraram pipoca:{n_comprou}")
if len(comprou) >= 1:
 print(f"compraram pipoca:{comprou}")



pagaram_mais = []
pagaram_menos = []

for x in valores:
  if x >= 25:
    pagou_mais = nomes[int(x)]
    pagaram_mais.append(pagou_mais)
  elif x <= 10:
    pagou_menos = nomes[int(x)]
    pagaram_menos.append(pagou_menos)

if len(pagaram_mais) >= 1:
 print(f"pagaram mais de 25 reais no ingresso:{n_comprou}")
if len(pagaram_menos) >= 1:
 print(f"pagaram menos de 10 reais no ingresso:{pagaram_menos}")