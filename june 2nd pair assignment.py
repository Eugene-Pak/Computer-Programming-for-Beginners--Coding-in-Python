username = "username"
password = "password"
balance = 500000000

def login():
    user = input("Username: \n")
    while user != username:
        user = input("Incorrect username, try again. \n Username: \n ")
    attempt = 1
    while user == username:
        pword = ""
        while pword != password:
            pword = input("Password: \n")
            if pword == password:
                print("Login succesful")
                break
            elif pword != password and attempt <= 2:
                print("Incorrect password, try again.\n")
                attempt += 1
            else:
                print("Out of attempts.")
                break  
        break

def return_to_menu():
    quest = input("Would you like to return to the main menu? \n (yes or no) \n")
    while quest != 'yes':
        if quest == "no":
            print('Have a good day!')
        else:
            print("Invalid input")
        


def withdraw():
    num1 = int(input("How much would you like to withdraw? \n"))
    new_bal = balance - num1
    for i in range(balance, new_bal-1, -1):
        print(i)
    print(f'Your new balance is ${new_bal}')
    return_to_menu()
    return new_bal 

    
def deposit():
    num2= int(input("How much would you like to deposit?  \n"))
    new_bal = balance + num2
    for i in range (balance, new_bal+1):
        print(i)
    print(f'Your new balance is ${new_bal}')
    return_to_menu()
    return new_bal

        
def main_menu():
    balance= 500000000
    status = True
    while status == True:
        action = input("What would you like to do? \n 1) Display account balance \n 2) Withdraw \n 3) Deposit \n 4) Quit\n (1,2,3,4)\n") 
        if action == "1":
            print(f"Your current balance is ${balance}")
            return_to_menu()
        elif action == "2":
            withdraw()
        elif action == "3":
            deposit()
        elif action == "4":
            status = False
        else:
            print("Invalid response, try again")
            break
    while status == False:
            break
                    
        
def ATM():
    login()
    main_menu()
        
ATM()  
        
        
        
        
        
        
        
        
        
        
        
        
        