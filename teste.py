ingr_type = input("Arquibancada(A),\nCadeira Lateral(CL)\nCadeira Central(CC) \n \nReservar ingressos para?: ")

ingr_quant = int(input("Quantos Ingressos Comprar?: "))

if(ingr_type == "A"):
    price = 30
    disp = 150
    if(ingr_quant <= disp):
        cost = ingr_quant * price
        can_buy = True
    else:
        print(f"Estão disponivies {disp} ingressos, {ingr_quant - disp} ingressos indisponíveis")
        can_buy = False

elif(ingr_type == "CL"):
    price = 50
    disp = 100
    if(ingr_quant <= disp):
        cost = ingr_quant * price
        can_buy = True
    else:
        print(f"Estão disponivies {disp} ingressos, {ingr_quant - disp} ingressos indisponíveis")
        can_buy = False

elif(ingr_type == "CC"):
    price = 80
    disp = 50
    if(ingr_quant <= disp):
        cost = ingr_quant * price
        can_buy = True
    else:
        print(f"Estão disponivies {disp} ingressos, {ingr_quant - disp} ingressos indisponíveis") 
        can_buy = False

else:
    print("Tipo de Ingresso Inválido.")
    can_buy = False

if (can_buy == True):
    if(ingr_quant > 4):
        totalcost = cost *0.85
    else:
        totalcost = cost

    print(f"O valor a pagar é: {totalcost} R$")
    print("Reserva confirmada!")

else:
    print()