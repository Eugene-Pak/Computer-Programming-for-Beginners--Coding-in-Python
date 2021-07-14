secret = float(10)
correct = 'n'
ready = input('You have 3 guesses to find the secret number! Are you ready? (y/n)\n')
if ready == 'y':
    g_1 = input('What is your first guess?\n')
else:
    print('Sorry to hear that you do not want to play. We hope you enjoy your day!')

if g_1 == 10:
    print('Congrats! You guessed the secret code!\n')
    correct = 'y'
    print('You beat the game!')
elif g_1 >= 11 and <= 20 :
    print('Very Very Hot\n')
elif g_1 >= 21 and <= 99 :
    print('Hot\n')
elif g_1 >= 100:
    print('Very Cold\n')
elif g_1 <= '9' and >= '0' :
    print('Warm\n')
elif g_1 <= '-1' and >= '-100' :
    print('Very Cold\n')
else:
    print('Very Very Cold\n')

ready = 'n'

ready = input('Are you ready for your second guess?(y/n)\n')

if ready == 'y':
    g_1 = input('What is your second guess?\n')
else:
    print('Sorry to hear that you do not want to play. We hope you enjoy your day!\n')

if g_1 == '10':
    print('Congrats! You guessed the secret code!\n')
    correct = 'y'
elif g_1 >= '11' and <= '20' :
    print('Very Very Hot\n')
elif g_1 >= '21' and <= '99' :
    print('Hot\n')
elif g_1 >= '100' :
    print('Very Cold\n')
elif g_1 <= '9' and >= '0' :
    print('Warm')
elif g_1 <= '-1' and >= '-100' :
    print('Very Cold\n')
else:
    print('Very Very Cold\n')
    

ready = 'n'

ready = input('Are you ready for your last guess?(y/n)\n')

if ready == 'y':
    g_1 = input('What is your final guess?\n')
else:
    print('Sorry to hear that you do not want to play. We hope you enjoy your day!\n')

if g_1 == '10':
    print('Congrats! You guessed the secret code!\n')
    correct = 'y'
elif g_1 >= '11' and <= '20' :
    print('Very Very Hot\n')
elif g_1 >= '21' and <= '99' :
    print('Hot\n')
elif g_1 >= '100' :
    print('Very Cold\n')
elif g_1 <= '9' and >= '0' :
    print('Warm')
elif g_1 <= '-1' and >= '-100' :
    print('Very Cold\n')
else:
    print('Very Very Cold\n')
    
if correct == 'y':
    print('You win!')
else:
    print('You lose :(. Try again!')