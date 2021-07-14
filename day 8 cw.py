# my_list = ['hello', 'pear', 'Columbia', 1, 5, 12, [1, 4, 5, 10]]
# print(my_list)
# 
# my_list.append(8)
# print(my_list)
# 
# my_list.remove(8)
# print(my_list)
# 
# for i in my_list:
#     if type(i) == str:
#         my_list[my_list.index(i)] = i + '!'
#         print(my_list)
# 
# for i in my_list:
#     if type(i) == int:
#         my_list[my_list.index(i)] = i + 1
# 
# for i in my_list:
#     if type(i) == list:
#         for v in i:
#             if type(v) == int:
#                 print(v)
#     
# hello_list = ['hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello']  
# for i, e in enumerate(hello_list):
#     if i % 2 != 0:
#         hello_list = e + '!'
# print(hello_list)
# 
# hello_list = []
# 
# for i in range(0, 50):
#     hello_list.append('hello')

# for i, e in enumerate(hello_list):
#     if i%2 != 0:
#         hello_list[i] = e + "!"
# print(hello_list)
# for i, e in enumerate(hello_list):
#     if '!' in e:
#         hello_list[i] = e[0] + 'i' + e[-1]
# print(hello_list)

# def tup_func():
#     a = 1
#     b = 'hi'
#     c = ['a', 'b', 'c']
#     return a, b, c

# my_tup_list = []
# for i in range(0,3):
#     my_tup_list.append(tup_func())
# print(my_tup_list)
# 
# for i in my_tup_list:
#     for v in i:
#         if type(v) == int:
#             print(v)

# def grocery():
#     g = input('Grocery: \n')
#     q = input('Quantity: \n')
#     return g, q
# 
# cart = {}
# for i in range(0,3):
#     c = grocery()
#     cart[c[0]] = c[1]
# print(cart)

#     rand_list = [1,2,3]
# for i in range(0,5):
#     try:
#         index = input('Choose an index number:\n(reminder to press q to end loop)\n')
#         if index == 'q':
#             print('Code was forcefully ended')
#             break
#         if index < 0:
#             raise Exception
#         x = rand_list[index]
#     except IndexError:
#         print('Invalid index value')
#     except ValueError:
#         print('Input a number')
#     except Exception:
#         print('Positive numbers and 0 allowed only')
#     else:
#         print(x)
                
# def convert(x):
#     new_list = []
# 
#     for i in x:
#         new_list.append(i)
#     return type(x), new_list

# def check(list1, list2):
#     count = 0
#     for i in list1:
#         for v in list2:
#             if i == v:
#                 count += 1
#                 if count == 2:
#                     return True
#     return False

# tup1 = [(1,1,1,1,1)]
# tup2 = [(2,1,1,1,1)]
# def tuple_check():
#     count = 0
#     for i in tup1:
#         for j in i:
#             for v in tup2:
#                 for k in v:
#                     if j == k:
#                         count += 1
#                         if count == len(i):
#                             return True
#                     else:
#                         break
#     return False
# 
# tuple_check()

# def check_tup_for(color):
#     tup = [('Red', 'Orange', 'Yellow'), ('Green', 'Blue', 'Purple'), ('White', 'Black', 'Brown')]
#     tup_count = 0
#     index_count = 0
#     for i in tup:
#         for v in i:
#             try:
#                 v.index(color)
#             except ValueError:
#                 index_count += 1
#                 if index_count == 3:
#                     tup_count += 1
#                     index_count = 0
#             else:
#                 break
#     print(f'{color} is located at Tuple #{tup_count}, Index #{index_count}')
# 
# check_tup_for('White')

# def check_tuples(word):
#     random_list = [('Red', 'Orange', 'Yellow'), ('Green', 'Blue', 'Purple'), ('White', 'Black', 'Brown')]
#     for i, e in enumerate(random_list):
#         if word in e:
#             return (f"{word} is located in tuple #{i + 1} at index {e.index(word)}")
# 
#     return (f"{word} is not located in this tuple of tuples")
# 
# check_tuples('White')

# def merge():
#     tup = []
#     tup.append(input('Input a list of numbers:\n'))
#     try:
#         for i in tup:
#             for k in i:
#                 if type(k) == int:
#                     print(k,i)
#                 else:
# 
# merge()

# def total():
#     total = 0
#     cart = {'Bananas': [2,1.58], 'Eggs': [1,4.25], 'Ice Cream': [3,2.99]}
#     for i,v in cart.values():
#         total += i * v
#     print(f'Your total is: ${total:.2f}')
#     total = 0
#     cart['Eggs'] = [2,4.25]
#     cart['Ice Cream'] = [4,2.99]
#     for i,v in cart.values():
#         total += i * v
#     print(f'Your new total after changing the quanitites is: ${total:.2f}')
# total()     












    
    
    
    
    
    
    
    
    
    


