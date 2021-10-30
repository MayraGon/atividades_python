import datetime


def obter_limite():
    print("*************************************************")
    print("** Bem vindo (a), à LOJA MAIS BONITA DA CIDADE **")
    print("*************************************************\n")

    print(
        "Aqui quem fala é Mayra Cristina Gonçalves, sua assistente virtual. Para verificar seu limite de crédito, preciso de alguns dados.\n",
        "Vamos começar!\n")

    cargo = input("Qual cargo você exerce atualmente? ")
    salario = float(input("E qual é seu salário atual? "))
    nascimento = int(input("Por fim, informe o ano de nascimento: "))

    year = datetime.date.today().year
    idade = year - nascimento

    print(
        "Você tem aproximadamente {} anos, e trabalha como {} e recebe um salário de R$ {:.2f}.\n".format(idade, cargo,
                                                                                                          salario))
    limite = float(((salario * (idade / 1000)) + 100))
    return limite, idade


limite, idade = obter_limite()
print(
    "De acordo com seus dados, verifiquei que você tem um limite de {:.2f} para utilizar em nossa loja.".format(limite))


def verificar_produto(limite):
    produto = input("Qual o produto desejado? ")
    preco_produto = float(input("Qual seu valor? R$ "))
    percentual_produto = float((preco_produto) / (limite)) * 100

    print("Você deseja comprar um(a) {} com o valor R$ {:.2f} ".format(produto, preco_produto))

    if percentual_produto <= 60:
        print("Compra liberada!")
    elif 60 < percentual_produto < 90:
        print("Compra liberada para parcelamento em 2 (duas) vezes.")
    elif 90 < percentual_produto < 100:
        print("Compra liberada para parcelamento em 3 (três) vezes.")
    else:
        print("Limite excedido! Compra bloqueada.")

    meu_nome = ("MayraCristinaGoncalves")
    numeros_nome = len(meu_nome)
    primeiro_nome = ("Mayra")
    numero_primeiro_nome = float(len(primeiro_nome))
    soma_idade_nome = int((idade) + (numero_primeiro_nome))
    desconto = float((preco_produto) - (numero_primeiro_nome))
    if preco_produto <= soma_idade_nome:
        print("Você ganhou um desconto de R$ {:.2f}. Agora sua compra é de R$ {:.2f}.".format(numero_primeiro_nome,
                                                                                              desconto))
    return preco_produto


quantidade_produtos = int(input("Deseja cadastrar quantos produtos?"))

soma = 0

for n in range(0, quantidade_produtos):
    preco_produto = verificar_produto(limite)
    soma = soma + preco_produto
    sobra_limite = limite - soma

    if sobra_limite >= 0:
        print('Restam R${} em seu limite de compras'.format(sobra_limite))
    else:
        print('Seu limite foi ultrapassado.')
        break

print("A LOJA MAIS BONITA DA CIDADE AGRADECE SUA PREFERÊNCIA. VOLTE SEMPRE!")
