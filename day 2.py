# def hms(S):
#     def h(H):
#         h = S // 3600
#         return h
#     def m(M):
#         m = (S - h * 3600) // 60
#         return m
#     def s():
#         s = S - h * 3600 - m * 60
#         return s
#
# def register():
#     total = float(input('How much money are you putting in?\n'))
#     hundred = total // 100
#     fifty = (total - hundred * 100) // 50
#     twenty = (total - hundred * 100 - fifty * 50) // 20
#     ten = (total - hundred * 100 - fifty * 50 - twenty * 20) // 10
#     five  = (total - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10) // 5
#     one = (total - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10) // 1
#     quarter = (total - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1) // 0.25
#     dime = (total - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1 - quarter * 0.25) // 0.1
#     nickel = (total - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1 - quarter * 0.25 - dime * 0.1) // 0.05
#     penny = (total - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1 - quarter * 0.25 - dime * 0.1 - nickel * 0.05) // 0.01
#     print(f"You have {hundred:.0f} hundreds, {fifty:.0f} fifties, {twenty:.0f} twenties, {ten:.0f} tens, {five:.0f} fives, {one:.0f} ones, {quarter:.0f} quarters, {dime:.0f} dimes, {nickel:.0f} nickels, and {penny:.0f} pennies\n")
# 
# 
# import math

# count = 0
# while count < 3:
#     print(f'count equals {ccount}')
#     count += 1
#     print('Done!')
    
# def parrot():
#     message = input('Tell me something and I will repeat it.\n')
#     print(message)


# def pizza():
#     commence = True
#     while commence == True:
#         pizza_toppings = input('What pizza toppings would you like?\n')
#         toppings = pizza_toppings
#         ready = input(f'So a {toppings} pizza so far. Is that all? (y/n)\n')
#         if ready == 'y':
#             break
#             commence = False
#         elif ready == 'n':
#             more_toppings = input('What other toppings would you like?\n')
#             toppings = toppings + more_toppings
#         else:
#             print('Invalid input. Please try again.')
#             break
#

# def cubed():
#     num1 = input('Input number:\n')
#     num2 = 1
#     while num2 != num1:
#         
#         print(f'{num2} squared is {num2 ** num2}')
#         num2 += 1
#         

# def countdown():
# 

# def count(num1, num2):
#     while num1 != num2:
#         if num1 >= num2:
#             print(f'{num1}\n')
#             num1 -= 1
#         else:
#             print(f'{num1}\n')
#             num1 += 1
#     if num1 >= num2:
#         print(f'{num1}\n')
#     else:
#         print(f'{num1}\n')
#             

# def convert_in_to_mm(start, end, incriment):
#     for i in range(start, end, incriment):
#         print(f'{i:.2f} inches\n')
#         print(f'{i*25.4:.2f} mm\n')
        
def factorial(num1):
    total = 1
    for i in range(1, num1+1):
        total = total * i  
    return total
        
def fib(num1)
    












    









































