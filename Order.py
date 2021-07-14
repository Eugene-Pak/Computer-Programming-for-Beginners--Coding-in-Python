app = input('Would you like the soup or salad?\n')
en = input('Would you like sushi or salmon?\n')
des = input('Would you like ice-cream or cake?\n')

soup_price = float(4.50)
salad_price = float(4.00)
sushi_price = float(12.00)
salmon_price = float(17.50)
icecream_price = float(5.50)
cake_price = float(10.00)
total = 0.00
order = app + en + des

if app == 'soup':
    order = 'soup'
    total = total + soup_price
elif app == 'salad':
    order = 'salad'
    total = total + salad_price
else:
    print('Invalid order, try again')
    
if en == 'sushi':
    order = order + ', sushi'
    total = total + sushi_price
elif en == 'salmon':
    order = order + ', salmon'
    total = total + salmon_price
else:
    print('Invalid order, try again')
    
if des == 'ice-cream':
    order = order + ', and ice-cream'
    total = total + icecream_price
elif des == 'cake':
    order = order + ', and cake'
    total = total + cake_price
else:
    print('Invalid order, try again')
    
confirm = input(f'Can you confirm that your order is: {order}? (y/n)\n')

if confirm == 'y':
    print(f'Your order has been confirmed, your total is ${total:.2f}')
else:
    print('We are sorry to hear that you canceled your order :(. Please come again!')
