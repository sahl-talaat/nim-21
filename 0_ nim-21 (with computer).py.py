import random
n = 0
count = n + 1
limit = 21
choose=int(input("enter '1' to play against computer or '2' to play in multiplayer mode\n"))
print(limit)
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
    print ("reminder = ", limit)

def handle_input(player_name):
    print (player_name)
    if choose==2 or count%2==1:
        x = int(input ("x: "))
    elif choose==1 and count%2==0:
        x=random.randint(1,3)
        while x > limit:
            x=random.randint(1,3)
    if choose==1 and count%2==0:
        print('x:',x)
    if x < 1 or x > 3 or x > limit:
        print ("invalid x")
    else:
        substract(x, player_name)

def read_user_input():
    if count%2 == 0 and choose==1:
        handle_input("computer")
    elif count%2==0:
        handle_input("player-2")
    else:
        handle_input("player-1")

while True:
    read_user_input()
