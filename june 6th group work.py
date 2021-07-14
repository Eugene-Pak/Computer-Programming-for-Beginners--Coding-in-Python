def grid():
    grid = [['A1', 'A2', 'A3', 'A4'], ['B1', 'B2', 'B3', 'B4'], ['C1', 'C2', 'C3', 'C4'], ['D1', 'D2', 'D3', 'D4']]
    return grid
    
def place():
    hi = ''
    boat = 1
    boat_num = 'first'
    boat_half = 1
    boat_half_count = 'first'
    position_check = []
    final_positions = []
    while boat <= 2:
        if boat == 2:
            boat_num = 'second'
        else:
            boat_num = 'first'
        if boat_half == 2:
            boat_half_count = 'second'
        else:
            boat_half_count = 'first'
        position_check = []
        position_check.append(input(f'Where do you wish to place your {boat_half_count} half of your {boat_num} boat?\n'))
        position_check2 = []
        position_check2 = position_check.pop()
        for position_check in grid():
            if (position_check2 in position_check) == True:
                final_positions.append(position_check2)
                if boat_half == 2:
                    boat += 1
                    boat_half = 1
                else:
                    boat_half += 1
                break
            elif (position_check2 in position_check) == False:
                hi = ''
            else:
                print('Invalid Tile Placement')
    return final_positions

def start_p1():
    print('Player 1, place your boats.')
    p1 = []
    p1 = place()
    return p1
     

def start_p2():
    print('\n \nPlayer 2, place your boats.')
    p2 = []
    p2 = place()
    return p2

def merge():
    end = False
    target_for_p2 = start_p1()
    target_for_p1 = start_p2()
    while end == False:
        mark1 = ''
        mark2 = ''
        turn = 1
        while turn == 1:
            mark1 = (input('\n\nPlayer 1, which tile do you want to attack?\n'))
            if (mark1 in target_for_p1) == False:
                print('The attack has missed...')
                turn = 2
            elif (mark1 in target_for_p1) == True:
                print('The attack has hit!')
                target_for_p1.remove(mark1)
                turn = 1
            else:
                print('Invalid tile placement')
            if len(target_for_p1) == 0:
                print('Player 1 wins!')
                turn = 3
                end = True
        while turn == 2:
            mark2 = (input('\n\nPlayer 2, which tile do you want to attack?\n'))
            if (mark2 in target_for_p2) == False:
                print('The attack has missed...')
                turn = 1
            elif (mark2 in target_for_p2) == True:
                print('The attack has hit!')
                target_for_p2.remove(mark2)
                turn = 2
            else:
                print('Invalid tile placement')
            if len(target_for_p2) == 0:
                print('Player 2 wins!')
                turn = 3
                end = True

merge()












