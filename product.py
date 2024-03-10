products = []
with open('products.csv', 'r') as f:
    for line in f:
        if '商品,價格\n' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

while True:
    name = input('please input product name: ')
    if name == 'q':
        break
    price = int(input('please input product price: '))
    products.append([name, price])
print(products)
print(products[0])
print(products[1])
for product in products:
    print(product[0], 'price is ', product[1])

with open('products.csv', 'w') as f:
    f.write('商品,價格\n')
    for product in products:
        f.write(product[0] + ',' + str(product[1]) + '\n')


