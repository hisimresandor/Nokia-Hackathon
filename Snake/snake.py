import os
import random

def make_field():
    f = [['*']]

    for i in range(59):
        f[0].append('*')

    for i in range(34):
        f.append(['*'])
        for j in range(58):
            f[i+1].append(' ')
        f[i+1].append('*')

    f.append(['*'])

    for i in range(59):
        f[len(f) - 1].append('*')

    return f

def snake_coord():
    x = random.randrange(1, 59)
    y = random.randrange(1, 35)

    return [x, y]

def play(f, s, l):
    direction = " "
    while not l:
        while True:
            draw_field(f)
            print("Hova?")
            direction = input("")
            if direction == "fel" or direction == "le" or direction == "jobbra" or direction == "balra" or direction == "meguntam":
                break
            
        if direction == "fel":
            f[s[1]][s[0]] = ' '
            s[1] -= 1
            print(s[1])
            f[s[1]][s[0]] = '@'
        if direction == "le":
            f[s[1]][s[0]] = ' '
            s[1] += 1
            print(s[1])
            f[s[1]][s[0]] = '@'
        if direction == "jobbra":
            f[s[1]][s[0]] = ' '
            s[0] += 1
            print(s[0])
            f[s[1]][s[0]] = '@'
        if direction == "balra":
            f[s[1]][s[0]] = ' '
            s[0] -= 1
            print(s[0])
            f[s[1]][s[0]] = '@'

        if s[0] == 0 or s[0] == 59 or s[1] == 0 or s[1] == 35 or direction == "meguntam":
            l = True
    
    draw_field(f)
    print("Hova?")
    print("Most ennyi volt, szép napot!")
    input()


def draw_field(f):
    os.system("cls")
    for i in range(len(f)):
        for j in range(len(f[i])):
            print((f[i][j]), end='')
        print("")

lose = False
field = make_field()
snake = snake_coord()
field[snake[1]][snake[0]] = "@"
play(field, snake, lose)