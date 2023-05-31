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


for p in products:
	print(p)
	print(p[0],'的價格是', p[1])
	# p[0] 每一個小清單的第0格  /  p[1]每一個小清單的第1格