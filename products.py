products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')	
	p = []
	p = [name, price]   # p.append(name)  p.append(price)
	products.append(p)	# 也可用products.append([name,price])	
print(products)	

products[0][0]   # prooducts清單中的第0格的第0個，第一項的name