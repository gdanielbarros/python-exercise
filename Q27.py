#! usr/bin/env python3

####################################################################################################################
#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#   Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#   Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
#receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos
#e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
####################################################################################################################


def calcular_precos():
  
    #variável
    count = 0
  
    #dados do produto.
    dados_produto = [("morango", 2.50, 2.20), ("maçã", 1.80, 1.50)]
    
    while True:
      
        #perguntar qual tipo de produto desejado.
        produto = input("Por favor, informe o produto desejado:")
        
        #verificar se tem o produto desejado
        if produto in dados_produto[count]:
            break
        
        else:
            #verificar se está acima de dois.
            if count > 2:
                print ("Valor inválido.")
                count = 0
    
    while True:
        
        #obter o peso do produto.
        peso = float(input("Por favor, informe o peso desejado:"))
        
        #verificar se o peso está acima de zero.
        if peso > 0:
            break
          
        else:
            continue
