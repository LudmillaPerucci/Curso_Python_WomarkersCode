'''Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho. Calcule o total do carrinho de compra.'''
produtos = {}

produtos ['Cadeira'] = 4
produtos ['Sofa'] = 1
produtos ['Geladeira'] = 1
produtos ['Fogão'] = 1
produtos ['Cama'] = 2

total = sum(produtos.values())

print(f'O total de itens no carrinho é: {total}')