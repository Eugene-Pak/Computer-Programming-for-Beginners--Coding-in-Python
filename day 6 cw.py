# x = [(1,2),(2,3),(3,4)]
# def convert(x):
#     convert = []
#     for i in x:
#         convert.append(list(i))
#     print(convert) 
# convert(x)

# def month():
#     month = input('Input a month')
#     no_space = month.strip()
#     abbr = no_space[0:3]
#     print(abbr.title() + '.') 

# grocery_list = {'Banana':5, 'Orange':2, 'Apple':4, 'Pear':4}
# print(grocery_list)     

# hero = {'HP':100, 'ATK':20, 'MAG':15, 'DEF':10, 'RES':10}
# hero['LUCK'] = 5
# hero['INFO'] = ('wqjkl;ef', 'BARD')
# print(hero)

# for fruit, quantity in grocery_list.values():
#     print(f'{quantity}{fruit}')

# guest_list = {'Sarah': 'Theodore', 'Maxin': 'Stacy', 'Doug': 'Genevieve', 'Marion': 'Anthony', 'Jean': 'Jeannette'}
# vip_list = {'Sarah', 'Doug', 'Jean'}
# for host, guest in guest_list.items():
#     if host in vip_list:
#         print(f'Hi {host} and your guest {guest}! Welcome to the VIP section.')
#     else:
#         print(f'Hi {host} and your guest {guest}! Welcome to the party.')

# hero = {'HP':100, 'ATK':20, 'MAG':15, 'DEF':10, 'RES':10}
# hero['LUCK'] = 5
# hero['INFO'] = ('wqjkl;ef', 'BARD')
# for stat, desc in hero.items():
#     print(f'Main:{stat} | Description: {desc}')
# for i in hero.keys():
#     print(i)
# for i in hero.values():
#     print(i)

# grocery_list = {'Bananas':float(1.58), 'Strawberries':4.99, 'Eggs':4.25, 'Bread':3.89, 'Milk':2.50, 'Yogurt':2.90, 'Tomatoes':2.00, 'Broccoli':3.26, 'Ice Cream':2.99, 'Paper Towels':5.99}
# for product, price in grocery_list.items():
#     print(f'${price}:{product}')
# total = 0
# for price in grocery_list.values():
#     total += price
# print(f'Total is ${total}')
# grocery_list['Flowers'] = 6.99
# del grocery_list['Tomatoes']
# total = 0
# for price in grocery_list.values():
#     total += price
# print(f'Total is ${total}')

# cart = {'Bananas':[2, 1.58], 'Eggs':[1,4.25], 'Ice Cream':[3,2.99]}
# total = 0
# for quantity, price in cart.values():
#     total += quantity * price
# print(f'{total:.2f}')
# cart['Eggs'][0] = 2
# print(cart)
# total = 0
# for quantity, price in cart.values():
#     total += quantity * price
# print(f'{total:.2f}')
# cart['Ice Cream'][0] = 4
# print(cart)
# total = 0
# for quantity, price in cart.values():
#     total += quantity * price
# print(f'{total:.2f}')

cards = {'A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
card_dic = {}
card_list = []
suits = ['d','c','h','s']
for i in cards:
    card_dic[i] = [suits]
    for j in suits:
        card_list.append(i+j)

import random

draw = random.choice(card_list)
if len(draw) == 3:
    r = draw[0] + draw[1]
    s = draw[-1]
else:
    r = draw[0]
    s= draw[-1]
    print(r,s)
    
# city = open('Cities.txt', 'r+')
# print(city.readable())
# print(city.readline())
# city.write('\nDubia - India')
# city.close()

# while True:
#     try:
#         num1 = input('Num 1 is\n')
#         if num1 == 'quit':
#             print('Secret code to end process inputted!\nEnding task.')
#             break
#         num2 = input('Num 2 is \n')
#         if num2 == 'quit':
#             print('Secret code to end process inputted!\nEnding task.')
#             break
#         result = int(num1)/ int(num2)
#         print(result)
#     except ZeroDivisionError:
#         print('Sorry, cannot divide by 0.\nPlease try again')
#     except ValueError:
#         print('Input real numbers.\nPlease try again')
#     else:
#         print('Passed all exceptions')





















