hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h > 40:
    hr2 = h-40
    hrrt =  hr2 * (r * 1.5)
    
    HRN = ((h-hr2) * r)
    
    print(HRN + hrrt)
else:   
    hrrt = 0
    print(h * r)


    #Escreva um programa para solicitar ao usuário as horas e a taxa por hora 
    #usando a entrada para calcular o pagamento bruto. 
    # Pague a taxa horária para as horas de até 40 e 1,5 vezes a taxa horária para todas as horas trabalhadas acima de 40 horas. 
    # #Use 45 horas e uma taxa de 10,50 por hora para testar o programa (o pagamento deve ser 498,75).
    # # Você deve usar input para ler uma string e float () 
    # #para converter a string em um número. Não se preocupe com a verificação de erros da entrada do usuário - suponha que o usuário digite os números corretamente.