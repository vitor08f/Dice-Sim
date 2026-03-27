defi = input("Você quer rolar dano(d) ou rolar teste(t)?: ")

dado = int(input("Escolha a quantia de lados do dado: "))
c = 0
num_dados = int(input("Quantos dados rolar?: "))
import random

#rolagem de testes
if(defi == "t"):
   roll = (input("Você quer rolar, vantagem(v) destvantagem(dv) ou outro (o)?: " ))
   teste = []
   for x in range(num_dados):
        x = random.randint(1,dado)
        teste.append(x);
   
   if(roll == "v"):
            if (max(teste) == dado):
              print(f"Sucesso Extremo:")

            elif (max(teste) == 1):
             print(f"Desastre:")

            print(f"você rolou um {max(teste)}, seus valores foram {teste}")
            
        
   elif(roll == "dv"):
      if (min(teste) == dado):
            print(f"Sucesso Extremo:")

      elif (min(teste) == 1):
             print(f"Desastre:")
             
      print(f"você rolou um {min(teste)}, seus valores foram {teste}")
      

   elif(roll == "o"):
           print(f"você rolou: {teste}")
           
#rolagem de dano
if(defi == "d"):
      dano = []
      for x in range (num_dados):
        x = random.randint(1,dado) 
        dano.append(x)
      print(f"você rolou {(dano)} e seu dano foi {sum(dano)}")
      