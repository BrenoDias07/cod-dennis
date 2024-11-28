import random as rd

nomes = ("dennis", "pablo", "matheus", "joão")

sorteio = rd.choice(nomes)
print("Olá, tente adivinhar qual nome eu vou sortear.")
print(nomes)

users_tentativa = input("Qual nome vai ser sorteado? :").lower()
if users_tentativa == sorteio:
    print(f"Parabéns, você acertou o nome era {sorteio}")
else:
    print(f"Poxa não foi dessa vez! você disse {users_tentativa} e o nome era {sorteio}")