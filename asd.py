n = 0
count = n + 1
limit = 21
#sahl talaat
def restart():
    global limit, count, n
    print('New Game!!')
    n = 0
    count = n + 1
    limit = 21

def substract(num, player_name):
    global limit, count
    limit-=num
    count+=1
    if limit==0:
        print(player_name+' lossed :(')
        restart()
    print ("limit = ", limit)

def handle_input(player_name):
    print (player_name)
    x = input ("x: ")
    if x < 1 or x > 3 or x > limit:
        print ("invalid x")
    else:
        substract(x, player_name)

def read_user_input():
    if count%2 == 0 :
        handle_input("player-2")
    else:
        handle_input("player-1")

while True:
    read_user_input()
