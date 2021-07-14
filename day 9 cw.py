import time

class restaurant:
    def __init__ (self, n, o, y, l):
        self.name = n
        self.owner = o
        self.year = y
        self.location = l
        self.ot = '1200'
        self.ct = '2200'
        self.starters = {'Soup': 4, 'Salad': 4, 'French Onion Soup': 10}
        self.entrees = {'Steak': 15, 'Smoked Salmon': 12, 'Lobster': 20}
        self.desert = {'Lava Cake': 7, 'Creme Brulee': 10, 'Ice Cream': 5}

    def description(self):
        print(f'{self.name}, founded by {self.owner} in the year {self.year}, is currently located at {self.location}.')

    def status(self):
        self.time = int(input('Welcome, what is your time of arrival?\n'))
        if self.time <= 2200 and self.time >= 1200:
            print(f'Welcome to {self.name}! We will now take you to your seats.')
        else:
            print(f'Sorry, but we are only open from {self.ot} to {self.ct}. Please come back during operation hours.')
            
    def menu(self):
        s_menu = list(self.starters.keys())
        e_menu = list(self.entrees.keys())
        d_menu = list(self.desert.keys())
        print(f'Please choose a starter from our menu. Our starter menu includes: {s_menu}')
        print(f'Please choose an entree from our menu. Our entree menu includes: {e_menu}')
        print(f'Please choose a desert from our menu. Our desert menu includes: {d_menu}')
        
    def server(self):
        count = 0
        server = 'Joe'
        print(f'Hi, my name is {server} and I will be serving you today. Here are our menu options for this evening:')
        self.menu()
        for i in range(0, 3):
            if i == 0:
                ready = False
                while ready == False:
                    s_order = input(f'What would you like to order for starters?\n')
                    for s in list(self.starters.keys()):
                        if s != s_order:
                            count += 1
                            if count == 3:
                                print(f'{s_order} is not in the menu. Please try again.')
                                count = 0
                        else:
                            count = 0
                            ready = True
            elif i == 1:
                ready = False
                while ready == False:
                    e_order = input(f'What would you like to order as your entree?\n')
                    for e in list(self.entrees.keys()):
                        if e != e_order:
                            count += 1
                            if count == 3:
                                print(f'{e_order} is not in the menu. Please try again.')
                                count = 0
                        else:
                            count = 0
                            ready = True
            elif i == 2:
                ready = False
                while ready == False:
                    d_order = input(f'What would you like to order for desert?\n')
                    for d in list(self.desert.keys()):
                        if d != d_order:
                            count += 1
                            if count == 3:
                                print(f'{d_order} is not in the menu. Please try again.')
                                count = 0
                        else:
                            count = 0
                            ready = True
        return s_order, e_order, d_order
    
    def cook(self, order):
        print(f'The chef is now preparing the {order}')
        for i in range(3,0,-1):
            print(f'{i}...')
            time.sleep(1)
        print(f'{order} done.')
        
    def eat(self, order):
        time.sleep(2)
        print(f'The customer is eating their {order}')
        time.sleep(3)
        print(f'The customer has finished eating their {order}')
        
    def chef(self):
        st_order, en_order, de_order = self.server()
        for i in range(0,3):
            if i == 0:
                order = st_order
                self.cook(order)
                self.eat(order)
            elif i == 1:
                order = en_order
                self.cook(order)
                self.eat(order)
            else:
                order = de_order
                self.cook(order)
                self.eat(order)
        return st_order, en_order, de_order
    
    def total(self):
        s_order, e_order, d_order = self.chef()
        total = 0
        for k,v in self.starters.items():
            if k == s_order:
                total += 1*v
        for k,v in self.entrees.items():
            if k == e_order:
                total += 1*v
        for k,v in self.desert.items():
            if k == d_order:
                total += 1*v
        new_total = total
        total += total * 0.11
#         tax
        total += new_total * 0.18
#         tip
        print(f'Your total is ${total:.2f}')

# class
    
my_restaurant = restaurant('Pacel', 'Eugene', '2021', 'Somewhere')
# my_restaurant.chef()
my_restaurant.total()








