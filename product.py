import os

def read_file(filename):
    products = []
    with open(filename, 'r') as f:
        for line in f:
            if '商品,價格\n' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
    return products

def user_input(products):
    while True:
        name = input('please input product name: ')
        if name == 'q':
            break
        price = int(input('please input product price: '))
        products.append([name, price])
    print(products)
    print(products[0])
    print(products[1])
    return products

def print_file(products):
    for product in products:
        print(product[0], 'price is ', product[1])

def write_file(filename, products):
    with open(filename, 'w') as f:
        f.write('商品,價格\n')
        for product in products:
            f.write(product[0] + ',' + str(product[1]) + '\n')
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('I find the file!')
        products = read_file(filename)
    else:
        print('I can not find the file')

    products = user_input(products)
    print_file(products)
    write_file(filename, products)

main()
