### Rock, paper, Scissor

from random import choice

cnt_plyer1 = 0
cnt_plyer2 = 0

while cnt_plyer1 < 3 and cnt_plyer2 < 3  :
    choice_player2 = choice(['rock', 'paper', 'scissor'])
    print(f"the computer point is:{cnt_plyer2} your points is: {cnt_plyer1}")
    chocice_player1 = input("Hey you ingress an choice beteween Rock, paper and Scissor\n").lower()


    if chocice_player1 == choice_player2:
        print('TIE :D')
    elif chocice_player1 == 'rock':
        if choice_player2 == 'paper':
            print("player 2 wins")
            cnt_plyer2 += 1  
        else:
            print("player 1 wins")
            cnt_plyer1 += 1  
    elif chocice_player1 == 'paper':
        if choice_player2 == 'rock':
            print("player 1 wins")
            cnt_plyer1 += 1
        else:
            print("player 2 wins") 
            cnt_plyer2 += 1
    elif chocice_player1 == 'scissor':  
        if choice_player2 == 'rock':
            print("player 2 wins")
            cnt_plyer2 += 1
        else:
            print("player 1 wins")
            cnt_plyer1 += 1
    else:
        print("Plese enter a valid choice")

print(f"Choice player 1: {cnt_plyer1}")
print(f"Choice player 2: {cnt_plyer2}")º