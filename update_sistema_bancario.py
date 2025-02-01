def menu():
    menu = '''\n
    =============== MENU ================
    [1]\tDeposito
    [2]\tSaque
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo usuário
    [0]\tSair
    =====================================
    => '''
    return input(menu)

def autenticar_usuario(cpf, senha, usuarios):
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario and usuario['senha'] == senha:
        return True
    else:
        print("=" * 40)
        print("CPF ou senha incorretos!")
        return False    

def depositar(saldo, valor, extrato, senha, usuarios, cpf, /):
    if not autenticar_usuario(cpf, senha, usuarios):
        print('Autenticação falhou! Deposito cancelado.')
        return saldo, extrato  

    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print('Deposito realizado com sucesso!')
    else:
        print("=" * 40)
        print('Operação falhou! Valor informado inválido!')
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numeros_saques, limite_saques, senha, usuarios, cpf):
    if not autenticar_usuario(cpf, senha, usuarios):
        print('\nAutenticação falhou! Saque cancelado.')
        return saldo, extrato

    execedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    excedeu_saque = numeros_saques >= limite_saques
   
    if execedeu_saldo:
        print('Operação falhou! Saldo insuficiente.')
    elif execedeu_limite:
        print('Operação falhou! O valor execede o limite.')
    elif excedeu_saque:
        print('Operação falhou! Número de saques exedido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numeros_saques += 1
        print('Saque realizado com sucesso!')
    else:
        print('Operação falhou! Valor informado é inválido.')
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(' EXTRATO '.center(40,"="))
    print('\nNão foram realizadas movimentações' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('=' * 40)

def criar_usuario(usuarios):
    print(" INFORME OS SEUS DADOS ".center(40, "="))
    cpf =  input('\nInforme o cpf (Apenas números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nJá existe um usuário com esse CPF!')
        return
    
    nome = input('\nInforme o nome completo: ')
    data_nascimento = input('\nInforme a data de nascimento (dd-mm-aa): ')
    endereco = input('\nInforme o endereço (logradouro, nro, bairro, cidade/sigla estado): ')
    senha = input('\nDefina uma senha para sua conta: ')

    usuarios.append({
        'nome': nome, 
        'data_nascimento': data_nascimento, 
        'cpf': cpf, 
        'endereco': endereco, 
        'senha': senha
    })
    print('\nUsuário criado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None 

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('\nInforme o CPF do usuario: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
        
    print('\nUsuário não encontrado, fluxo de criação de conta encerrado!')

def listar_contas(contas):    
    if not contas:
        print("\nNehuma conta cadastrada.")
        return 

    for conta in contas:
        linha = f'''\
            Agência:\t{conta["agencia"]}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta["usuario"]["nome"]}  
        '''
        print("=" * 40)
        print(linha)
          
def main():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            cpf = input("Informe seu CPF: ")
            senha = input("Informe sua senha: ")
            valor = float(input("Informe o valor do depósito: "))
            

            saldo, extrato = depositar(saldo, valor, extrato, senha, usuarios, cpf)

        elif opcao == '2':            
            valor = float(input('Informe o valor do saque: '))
            senha = input('Informe sua sengha: ')

            saldo, extrato =  sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeros_saques=numeros_saques,
                limite_saques=LIMITE_SAQUE,
                senha=senha,
                usuarios=usuarios,
                cpf=cpf
            )
         
        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == '5':
            print(' CONTAS CADASTRADAS '.center(30, "="))
            listar_contas(contas)

        elif opcao == '6':
            criar_usuario(usuarios)
        
        elif opcao == '0':
            break

        else:
            print('Operação falhou! Por favor selecione a operação desejada.')
        print()

main()