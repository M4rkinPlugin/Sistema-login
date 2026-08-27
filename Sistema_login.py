
import time

print("Olá, Parece q é sua primeira vez usando esse sistema!")
print("")
o = input("Se vc deseja criar uma conta aperta o botão ENTER do seu teclado.")

print("Como você deseja que seja o nome do seu usuário?")
u = input("")

print("Agora Defina sua senha!")
s = input("")
time.sleep(0.5)
print("Espera uns segundos estamos salvando seus dados!")

user = {
    "user":f"{u}",
    "senha":f"{s}"
    
}

time.sleep(2)
print("Dados Salvos!")
time.sleep(0.4)
print("Seja Bem-Vindo ao menu principal!")

while True:
 print("======[ MENU ]======"),
 print(f"Olá, " + user["user"])
 print("1. ")
 print("2. ")
 print("3. Sair Da Conta")
 print("======[ MENU ]======")
 o = input("Opção: ")
 
 if o == "1":
     print("Informação opção 1")
 
 elif o == "2":
     print("informação opção 2")
 
 elif o == "3":
     print("saindo da conta...")
     break
 
 else:
     print("Opção Descolhecida")
