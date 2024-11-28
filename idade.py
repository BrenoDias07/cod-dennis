nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print(f"Olá {nome}, Seja bem vindo(a)!!!")
else:
    print(f"Olá {nome}, você ainda é menor de idade! Tente novamente mais tarde")