usuarios = {
    "juliano@gmail.com": "juliano1234",
    "rosa-martins@hotmail.com": "Martins4321",
    "rodrigues@live.com": "rodri1998"
}
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#Verificando o Login
logado = False
while not logado:
    usuario = str(input("Informe o usuário: "))
    senha = str(input("Informe a senha: "))

    if usuario in usuarios and usuarios[usuario]:
        print("Login realizado com sucesso!\n")
        logado = True
    else:
        print("Usuário ou senha inválido! Tente novamente.\n")

while True:
    opcao = input(menu)
    
    #Verificação de Depósito
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        #Verificando se o valor a ser depósitado é realmente positivo. 
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else: 
            print("Operação falhou! O valor informado é inválido.")
        
    
    #Verificação de Saque.
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        #Verificando se o valor do saque é maior que o saldo.        
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        #Verificando se o valor do saque é maior que o limite do saque.
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        #Verificando se a quantidade de lnumeros de saques está utrapassando o limite dos saques.
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Numero de saques execedido.")
       
        #Verificando se está tentando sacar um valor negativo na conta.
        elif valor > 0:
            senha_saque = input("Confirme a senha: ")
            if usuarios[usuario] == senha_saque:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
        
        else:
            print("Operação falhou! O valor informado é invalido.")
    
    #Verificação de extrato. 
    elif opcao == "3":
        print(" EXTRATO ".center(40,"="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("="*40)
    
    #Verificação de Saída.
    elif opcao == "0":
        print("Obrigado por usar nosso sistema bancário! Até logo.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
    print() #Linha em branco