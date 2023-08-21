import math

salarioB = float(input("Digite o salário: "))


vale =  input("Descontar o Vale Transporte? ")
if vale == ('nao'):
    print ('não haverá desconto de vale-transporte')
elif vale == ('sim'):
    vale = salarioB*0.06
    print ('o desconto de vale-transporte foi de',vale)

if salarioB <1302.00:
    inss = salarioB*0.075
    print (f"Calculo do INSS R${inss}")
    print ("Seu salário liquído sem INSS é de: R$", (salarioB-inss))
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB <2571.29:
    inss = salarioB*0.09
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído é de: R$", (salarioB-inss))
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB <3856.94:
    inss = salarioB*0.12
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído é de: R$", (salarioB-inss))
elif salarioB <7507.50:
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)