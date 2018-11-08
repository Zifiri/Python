# While Basic

i = 0

while i <= 10:
    print("i:", i)
    i += 1



# While 

win = "loser"
winner = ""
limits = 3
limitcounts = 0
gameover = False


while winner != win and not(gameover):
    if limitcounts < limits: 
        winner = input("Enter Winner Name:")
        limitcounts += 1
    else:
        gameover = True    


if gameover:
    print("Game over you lose.")
else:    
    print("You winner...")


    


