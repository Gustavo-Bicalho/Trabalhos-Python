lista = []
print('BEM VINDO AO SAAS MARKET')
itens = 0
while True:
    try:
        itens = int(input('Digite a quantidade de itens que deseja adicionar: '))
        if itens <= 0:
            print('A quantidade de itens deve ser um número positivo.')
        else:
            break
    except ValueError:
        print('Por favor, digite um número válido para a quantidade de itens.')
for item in range(itens):
    while True:
        nome = input('Digite o nome dos itens: ')
        if not nome:
            print('O nome do item não pode ser vazio! Por favor digite um nome válido')
        else:
            lista.append(nome)
            lista.sort()
            lista.count
            break

print('\nItens adicionados:')
for item in lista:
    print(item)
print(f'A lista possui {itens} itens')
    