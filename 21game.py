import random 
current_number = 0
n = random.randint(0,1)
if n == 0:
    current_player   = 'human'
else:
    current_player   = 'computer'
while True:
    print(f"Người chơi hiện tại là: {current_player}")
    if current_player == 'human':
        player_choice = int(input('Nhập vào số 1, 2 hoặc 3'))
        if(player_choice>3 or player_choice<1):
            print('Số nhập vào không hợp lệ, số hợp lệ là 1, 2, 3')
            player_choice = int(input('Nhập vào số 1, 2 hoặc 3'))
        else:
            while current_number <21:
                current_number += player_choice
        print(f'Số hiện tại là: {current_number}')
        current_player = 'computer'
    else:
        player_choice = random.randint(1,3)
        print(f"Số nhập vào của máy: {player_choice}")
        while current_number <21:
            current_number += player_choice
        print(f'Số hiện tại là: {current_number}')
        current_player = 'human'