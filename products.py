# 讀取檔案
products = []
with open('products.csv', 'r', encoding= 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue        # 繼續
		name, price = line.strip().split(',')   # 先用strip()把換行符號去掉；再用line.split，以','當切割標準
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')	
	price = int(price) 
	p = [name, price]   # p.append(name)  p.append(price)
	products.append(p)	# 也可用products.append([name,price])	
print(products)	

# 印出所有購買紀錄
for p in products:
	print(p[0],'的價格是', p[1])    # p[0] 每一個小清單的第0格  /  p[1]每一個小清單的第1格

# 寫入檔案
with open('products.csv', 'w', encoding= 'utf-8') as f:  
# 用寫入模式打開products.csv，並作為f(之後用到該檔案都以f代稱)
# 因為是寫入模式w,若原本products.csv這個檔案，會自動創一個。
# encoding= 'utf-8'   用該寫入模式
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  #\n 換行符號
		# 用+來結合不同字串，變成一個大字串，並寫入f
		# 因p[1]是整數(見line7)，所以要轉換成字串str(p[1])
		# 在p[0]跟str(p[1])兩種不同屬性中間以','做區隔，寫入後才不會擠在一起