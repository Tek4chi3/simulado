nome_funcionario= str(input("Digite o nome do funcionário:"))
quantidade_de_vendas= int(input("Digite quantas vendas o funcionário fez:"))
soma_vendas=0
for c in range(1,quantidade_de_vendas+1):
    vendas_loop=float(input(f"Digite o valor da venda {c}:"))
    soma_vendas+=vendas_loop
    media= soma_vendas/quantidade_de_vendas
print(f"A soma de todas as vendas deu R${soma_vendas}. Assim, a média das vendas é R${media}")
if media>=100000:
    print(f"O funcionário {nome_funcionario} atingiu a meta")
elif media<100000:
    print(f"O funcionário {nome_funcionario} NÃO atingiu a meta")