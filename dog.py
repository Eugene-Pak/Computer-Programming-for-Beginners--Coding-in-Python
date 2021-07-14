class Dog: #create dog class
    
    def __str__(self):
        return f'This is my dog {self.name}!'
    
    def __init__(self, name, age): #assigns attributes
        self.name = name
        self.age = age
    
    def information(self):
        print(f'{self.name} is {self.age} years old.')
        
    def speak(self, sound):
        print(f'{self.name} says {sound}!')
        
class GoldenRetriever(Dog):
    def speak(self, sound = 'Woof'):
        return f'{self.name} says {sound}'
    
    def rollover(self):
        print(f'{self.name} rolled over!')


class Samoyed(Dog):
    def speak(self, sound = 'arf'):
        return f'{self.name} says {sound}'
    
    def rollover(self):
        print(f'{self.name} cannot roll over.')
    
my_dog = Dog('Joe', 4)
mom_dog = GoldenRetriever('Candice', 6)
your_dog = Samoyed('Mike', 2)


# class restaurant:
#     def __init__ (self, n, c, l, p):
#         self.name = n
#         self.cuisine = c
#         self.location = l
#         self.capacity = p
#         
#     def description(self, desc):
#         print(f'{self.name} is {desc}')
#     
#     def status(self, stat):
#         print(f'{self.name} is currently {stat}')
#     
#     def prep(self, course):
#         print(f'We are currently preparing {course}')
#         
#     def customer(self, cust):
#         self.customer = cust + 1
#         print(f'{self.name} currently has {self.customer} inside.')
#         
# class fast_food(restaurant):
#     def status(self, stat = 'open 24/7'):
#         print(f'{self.name} is {stat}!')
#         
#     def prep(self, course = "Ma'am, this is a Wendys"):
#         print(f'{course}')
# 
# 
# class steakhouse(restaurant):
#     def status(self, stat = 'closed'):
#         print(f'{self.name} is currently {stat}')
#     
#     def prep(self, course = 'the steak'):
#         print(f'We are currently preparing {course}')
#         
#         
# class Koreanbbq(restaurant):
#     def status(self, stat = 'open'):
#         print(f'{sel.name} is {stat} as of this moment.')
#     
#     def prep(self, course = 'sides'):
#         print(f'We will present the {course} while you await your order.')
#         
# res = restaurant('Nobu', 'Japanese', 'somewhere', 1)
# mcdonald = fast_food('McDonald', 'Fast Food', 'Literally everywhere', 100000)
# steak = steakhouse('Texas Steakhouse', 'Steak', 'Texas?', 20)
# bbq = Koreanbbq('Korean BBQ', 'Korean Meat', 'Korea?', 30)

# def info():
#     name = input('What is your full name?\n')
#     email = input('What is your email address?\n')
#     def split(word):
#             return [char for char in word]
#     temp = split(email)
#     x = temp.index('@')
#     username = email.split('@')[0]
#     print(f'User: {name.capitalize()}\nEmail: {email}\nUsername: {username}')
#     
# info()

# def pig():
#     word = []
#     word = list(input('Input a word that you want to be translated into Pig Latin.\n'))
#     move = word.pop(0)
#     stay = []
#     for i in word:
#         stay += i
#     stay.append(move)
#     stay.append('ay')
#     final_word = ''
#     for i in stay:
#         final_word += i
#     print(final_word)
#     
# pig()
    
















