products = []
while True:
	name =  input('Please enter product name: ')
	if name == 'q':
		break
	price = input('Please input product price: ')
	p = []
	p.append(name)
	p.append(price)
# line 7,8,9 merge into p = [name, price]
	products.append(p)
# Also, eliminate line 7,8,9 and use products.append(name, price)

print(products)
for p in products:
	print(p)
	print(p[0])
