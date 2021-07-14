def game():
    secret = 10
    end_game = False
    ready = input('Welcome to the guessing game, you have three tries to guess the secret number! Are you ready? (y/n)\n')
    if ready == 'n':
        end_game = True
    while ready == 'y' and end_game == False:
        attempt = 1
        attempt_w = 'first'
        while guess != 10:
            guess = int(input(f'What is your {attempt_w} guess?\n'))
            if guess >= 11 and guess <= 20:
                print('Very Very Hot\n')
                attempt += 1                
            elif guess >= 21 and guess <= 99:
                print('Hot\n')
                attempt += 1
            elif guess >= 100:
                print('Very Cold\n')
                attempt += 1
            elif guess <= 9 and guess >= 0:
                print('Warm\n')
                attempt += 1
            elif guess <= -1 and guess >= -100:
                print('Very Cold\n')
                attempt += 1
            else:
                print('Very Very Cold\n')
                attempt += 1
        if attempt == 1:
            attempt_w = 'first'
        if attempt == 2:
            attempt_w = 'second'
        if attempt == 3:
            attempt_w = 'final'
        print('Congrats! You guessed the secret code!\nYou beat the game!')
    if end_game == True:
        print('Sorry to hear that :(. See you next time!')
    else:
        print('Invalid input. Ending Game.')
        
    
        
