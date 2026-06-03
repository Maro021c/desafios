#VARIAVEL PARA DEFINIR A QUANTIDADE DE CLIENTES NA SESSÃO
clientes = int(input("quantos clientes serão cadastrados nessa sessão?:"))

#LISTAS PARA GUARDAR INFORMAÇÕES
nomes = []
valores = []
pipocas = []
idades = []

#INFORMAÇÕES DAS IDADES DOS CLIENTES

total_criança = 0
total_adolecente = 0
total_adulto = 0
total_idoso = 0
total_pipocas = sum(pipocas)

#PEGANDO INFORMAÇÕES DO CLIENTE
for cliente in range(clientes):

    nome = input("nome do cliente:")
    idade = input("idade do cliente:")
    valor = float(input("valor de ingresso:"))
    pipoca = int(input("quantas pipocas:"))
    nomes.append(nome)
    idades.append(idade)
    valores.append(valor)
    pipocas.append(pipoca)


#VERIFICAÇÃO DE IDADES     
for idade in range(idades):
    if idade < 12:
     total_criança += 1 
      
    elif idade >= 12 and idade <= 17:
     total_adolecente += 1
    
    elif idade >=18 and idade <=59:
     total_adulto += 1
    
    else:
     total_idoso += 1

#RELATÓRIO DE CLIENTES
print(f"Total de Clientes: {clientes}")

print(f"Total de crianças: {total_criança}, Total de adolescente: {total_adolecente}")

print(f"Total de adultos: {total_adulto}, Total de idosos: {total_idoso}")

#TOTAL DE PIPOCAS 
print(f"Total de pipocas: {total_pipocas}")
    