import random

def cards():
    card_dic = {}
    card_list = []
    cards = {'A', 'J', 'Q', 'K', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
    suits = ['💎','☘','❤','♤']
    for i in cards:
        card_dic[i] = suits
        for j in suits:
            card_list.append(i+j)
    return card_dic, card_list, i, j
    
def player_count():
    player_count = int(input('How many players are participating in the game?\n(Max Player Count 4)\n'))
    return player_count

def filter_players():
    ready = False
    player_num = player_count()
    while ready == False:
        if player_num == '1':
            print('Not enough players, at least 2 players are needed to start the game.\nTry again.')
            break
        elif player_num == '2' or player_num == '3' or player_num == '4':
            print(f'Starting the game with {player_num} players. Have fun!')
            break
        else:
            print('Invalid value inputted. Remember, there can only be up to 4 players!')
            break
    return player_num
    
def deck():
    card_dic, card_list, r, s = cards()
    hand = []
    player_1 = {}
    player_2 = {}
    player_3 = {}
    player_4 = {}
    players = player_count()
    for i in range (0, players):
        player = {'A': [], 'J': [], 'Q': [], 'K': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': []}
        player[r] = []
        for e in range (1,8):
            card_draw = random.choice(card_list)
            hand.append(card_draw)
            card_list.remove(card_draw)
            if len(card_draw) == 3:
                r = card_draw[0] + card_draw[1]
                s = card_draw[-1]
            else:
                r = card_draw[0]
                s = card_draw[-1]
            for v in [r]:
                player[r].append(s)
        if i == 0:
            player_1 = player
        elif i == 1:
            player_2 = player
        elif i == 2:
            player_3 = player
        else:
            player_4 = player
    return card_list, card_draw, hand, r, s, player, player_1, player_2, player_3, player_4, card_dic, players

def go_fish():
    card_list, card_draw, hand, r, s, player, player_1, player_2, player_3, player_4, card_dic, players = deck()
    go_fish = {}
    card_draw = random.choice(card_list)
    hand.append(card_draw)
    card_list.remove(card_draw)
    if len(card_draw) == 3:
        r = card_draw[0] + card_draw[1]
        s = card_draw[-1]
    else:
        r = card_draw[0]
        s = card_draw[-1]
    return card_list, card_draw, hand, r, s, player, player_1, player_2, player_3, player_4, card_dic, players

def card_deal():    
    card_list, card_draw, hand, r, s, player, player_1, player_2, player_3, player_4, card_dic, players = go_fish()
    print(f'\n\n\n\n\n\n\nPlayer 1 Cards: {player_1}')
    print(f'\n\n\n\n\n\n\nPlayer 2 Cards: {player_2}')
    print(f'\n\n\n\n\n\n\nPlayer 3 Cards: {player_3}')
    print(f'\n\n\n\n\n\n\nPlayer 4 Cards: {player_4}')
    return player_1, player_2, player_3, player_4, players, go_fish, r, s, card_list

def card_steal():
    ready = False
    player_1, player_2, player_3, player_4, players, go_fish, r, s, card_list = card_deal()
    while ready == False:
        for i in range(0, players):
            fish = random.choice(card_list)
            card_list.remove(fish)
            if len(fish) == 3:
                r = fish[0] + fish[1]
                s = fish[-1]
            else:
                r = fish[0]
                s = fish[-1]
            print(f"Player {i + 1}'s turn:")
            steal = input(f'Which rank card would you like?\n')
            victim = input(f'\nWho would you like to steal from?(1,2,3,4)\n')
            if victim == '1':
                if i == 0:
                    print('You cannot rob yourself!')
                elif i == 1:
                    for v in player_1[steal]:
                        player_2[steal].append(v)
                    player_1[steal] = []
                    print(f'Player 1 Cards:\n {player_1}')
                    print(f'Player 2 Cards:\n {player_2}')
                    if player_1[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_2[r].append(s)
                            print(f'Your new card is {r} {s}')
                elif i == 2:
                    for v in player_1[steal]:
                       player_3[steal].append(v)
                    player_1[steal] = []
                    print(f'Player 1 Cards:\n {player_1}')
                    print(f'Player 3 Cards:\n {player_3}')
                    if player_1[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_3[r].append(s)
                            print(f'Your new card is {r} {s}')
                elif i == 3:
                    for v in player_1[steal]:
                       player_4[steal].append(v)
                    player_1[steal] = []
                    print(f'Player 1 Cards:\n {player_1}')
                    print(f'Player 4 Cards:\n {player_4}')
                    if player_1[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_4[r].append(s)
                            print(f'Your new card is {r} {s}')
                else:
                    print(f'Invalid input')
            elif victim == '2':
                if i == 0:
                    for v in player_2[steal]:
                       player_1[steal].append(v)
                    player_2[steal] = []
                    print(f'Player 1 Cards:\n {player_1}')
                    print(f'Player 2 Cards:\n {player_2}')
                    if player_2[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_1[r].append(s)
                            print(f'Your new card is {r} {s}')
                elif i == 1:
                    print('You cannot rob yourself!')
                elif i == 2:
                    for v in player_2[steal]:
                       player_3[steal].append(v)
                    player_2[steal] = []
                    print(f'Player 2 Cards:\n {player_2}')
                    print(f'Player 3 Cards:\n {player_3}')
                    if player_2[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_3[r].append(s)
                            print(f'Your new card is {r} {s}')
                elif i == 3:
                    for v in player_2[steal]:
                       player_4[steal].append(v)
                    player_2[steal] = []
                    print(f'Player 2 Cards:\n {player_2}')
                    print(f'Player 4 Cards:\n {player_4}')
                    if player_2[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_4[r].append(s)
                            print(f'Your new card is {r} {s}')
                else:
                    print(f'Invalid input')
            elif victim == '3':
                if i == 0:
                    for v in player_3[steal]:
                       player_1[steal].append(v)
                    player_3[steal] = []
                    print(f'Player 1 Cards:\n {player_1}')
                    print(f'Player 3 Cards:\n {player_3}')
                    if player_3[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_1[r].append(s)
                            print(f'Your new card is {r} {s}')
                elif i == 1:
                    for v in player_3[steal]:
                       player_2[steal].append(v)
                    player_3[steal] = []
                    print(f'Player 2 Cards:\n {player_2}')
                    print(f'Player 3 Cards:\n {player_3}')
                    if player_3[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_2[r].append(s)
                            print(f'Your new card is {r} {s}')
                elif i == 2:
                    print('You cannot rob yourself!')
                elif i == 3:
                    for v in player_3[steal]:
                       player_4[steal].append(v)
                    player_3[steal] = []
                    print(f'Player 3 Cards:\n {player_3}')
                    print(f'Player 4 Cards:\n {player_4}')
                    if player_3[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_4[r].append(s)
                            print(f'Your new card is {r} {s}')
                else:
                    print(f'Invalid input')
            elif victim == '4':
                if i == 0:
                    for v in player_4[steal]:
                       player_1[steal].append(v)
                    player_4[steal] = []
                    print(f'Player 1 Cards:\n {player_1}')
                    print(f'Player 4 Cards:\n {player_4}')
                    if player_4[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_1[r].append(s)
                            print(f'Your new card is {r} {s}')
                elif i == 1:
                    for v in player_4[steal]:
                       player_2[steal].append(v)
                    player_4[steal] = []
                    print(f'Player 2 Cards:\n {player_2}')
                    print(f'Player 4 Cards:\n {player_4}')
                    if player_4[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_2[r].append(s)
                            print(f'Your new card is {r} {s}')
                elif i == 2:
                    for v in player_4[steal]:
                       player_3[steal].append(v)
                    player_4[steal] = []
                    print(f'Player 3 Cards:\n {player_3}')
                    print(f'Player 4 Cards:\n {player_4}')
                    if player_4[steal] == []:
                            print(f'Player does not have {steal}. Go Fish!')
                            player_3[r].append(s)
                            print(f'Your new card is {r} {s}')
                elif i == 3:
                    print('You cannot rob yourself!')
                else:
                    print(f'Invalid input')
        
card_steal()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
