
while True:
  #VARIAVEL PARA DEFINIR A QUANTIDADE DE CLIENTES NA SESSÃO 
  clientes = int(input("quantos clientes serão cadastrados nessa sessão?:"))
  
  #LISTAS PARA GUARDAR INFORMAÇÕES
  nomes = []
  valores = []
  pipocas = []
  idades = []

  #INFORMAÇÕES DO TOTAL DE CLIENTES
  total_criança = 0
  total_adolecente = 0
  total_adulto = 0
  total_idoso = 0
  
  #PEGANDO INFORMAÇÕES DO CLIENTE
  for cliente in range(clientes):

      nome = input("nome do cliente:")
      idade = int(input("idade do cliente:"))
      valor = int(input("valor de ingresso:"))
      pipoca = int(input("quantas pipocas:"))
      nomes.append(nome)
      idades.append(idade)
      valores.append(valor)
      pipocas.append(pipoca)
        
  #CONTABILLIDADE ETARIA      
  for idade in idades:

      if idade < 12:
       total_criança += 1 
        
      elif idade >= 12 and idade <= 17:
       total_adolecente += 1
      
      elif idade >=18 and idade <=59:
       total_adulto += 1
      
      else:
       total_idoso += 1

  #VARIAVEIS DE VALOR
  total_Economica = 0
  total_Normal = 0
  total_Premium = 0

  #CONTABILIDADE DE CLASSE
  for valor in valores:
    if valor <= 15.00:
     total_Economica += 1 
      
    elif valor >= 15.01 and valor <= 30.00:
     total_Normal += 1
    
    elif valor > 30.00:
     total_Premium += 1

  #RELATORIO DE INFORMAÇÕES
  
  
  #MEDIA DO VALOR DOS INGRESSOS VENDIDOS
  
  media_ingressos = sum(valores) / len(valores)   
 
  #TOTAL DE PIPOCAS 
  maior_valor = max(valores)
  menor_valor = min(valores)

  #RELATÓRIO DO TOTAL ARRECADADO NO FINAL DO DIA/SESSÃO
  total_pago = sum(valores)
  movimento = str(0)
  if total_pago <= 499.99:
    movimento = "fraco"
  elif total_pago >= 500.00 and total_pago <= 1499.99:
    movimento = "normal"
  elif total_pago >= 1500.00:
    movimento = "excelente"

  
  #VERIFICANDO A FAIXA ETÁRIA DOS CLIENTES
  faixa_etaria = max(total_adolecente, total_adulto, total_criança, total_idoso)
  if faixa_etaria == total_criança:
      maioria_idade = str("crianças")
  if faixa_etaria == total_adolecente:
      maioria_idade = str("adolecentes")
  if faixa_etaria == total_adulto:
      maioria_idade = str("adultos")
  if faixa_etaria == total_idoso:
      maioria_idade = str("idosos")
  
  #VERIFICANDO QUAIS CLIENTES COMPRARAM E QUAIS NÃO COMPRARAM PIPOCA
  n_comprou = []
  comprou = []

  for n in range(len(pipocas)):
    x = pipocas[n]
    n_comprou_pipoca = nomes[n]
    comprou_pipoca = nomes[n]
    if x == 0:
      n_comprou.append(n_comprou_pipoca)
    elif x >= 1:
    
      comprou.append(comprou_pipoca)


  #VERIFICANDO QUEM PAGOU MAIS E QUEM PAGOU MENOS
  pagaram_mais = []
  pagaram_menos = []


  for v in range (len(valores)):
    x = valores[v]
    pagou_mais = nomes[v]
    pagou_menos = nomes[v]

    if x >= 25:
      pagaram_mais.append(pagou_mais)
    elif x <= 10:
      pagaram_menos.append(pagou_menos)

  print(f''']
        //TABELA GERAL//

        a media de ingressos foi {media_ingressos} reais

        Total de Clientes: {clientes}

        Total de crianças: {total_criança}

        Total de adolescente: {total_adolecente}

        Total de adultos: {total_adulto}

        Total de idosos: {total_idoso}

        Total de pipocas: {sum(pipocas)}

        o maior valor pago foi de:{maior_valor} reais

        o menor valor pago foi de:{menor_valor} reais

        //RESUMO DE GANHOS//

        o total arrecadado foi de {total_pago} reais, o movimento foi {movimento}!

        //RESUMO DE PUBLICO//

        //FAIXA ETÁRIA//
        
        a faixa etária do dia foi de {maioria_idade}
        
        //VENDA DE PIPOCAS//''')
  
  if len(n_comprou) >= 1:
   print(f'''
         não compraram pipoca: {', '.join(n_comprou)}
  ''')
  if len(comprou) >= 1:
   print(f'''
         compraram pipoca: {', '.join(comprou)}
  ''')

  print(f'''
        //RELATORIO DE VALORES FINAIS//

        ''')
  
  if len(pagaram_mais) >= 1:
   print(f'''
         pagaram mais de 25 reais no ingresso:{', '.join(pagaram_mais)}
  ''')
  if len(pagaram_menos) >= 1:
   print(f'''
         pagaram menos de 10 reais no ingresso:{', '.join(pagaram_menos)}
  ''')

  print(f'''      
        //OUTRAS OPÇÕES//

        ''')

  #OPÇÃO DE REGISTRAR MAIS UMA SESSÃO/DIA
  escolha = input("quer registrar um novo dia/sessão? s/n:")
  if escolha == "s":
   break