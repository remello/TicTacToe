def print_game(game):
    print("---------")
    print("|", game[2][0], game[2][1], game[2][2], "|")
    print("|", game[1][0], game[1][1], game[1][2], "|")
    print("|", game[0][0], game[0][1], game[0][2], "|")
    print("---------")


def input_validation(data):
    data = data.split()
    try:
        a = int(data[0])
        b = int(data[1])
    except ValueError:
        print("You should enter numbers!")
        return(0)
    if (0 < a < 4) and (0 < b < 4):
        return a - 1, b - 1
    else:
        print("Coordinates should be from 1 to 3!")
        return 0


def draw_check(game):
    draw = 1
    global state
    for i in game:
        for j in i:
            if j == "_":
                draw = 0
    if draw == 1:
        state = 1
        print_game(game)
        print("Draw")


def win_check(game, symbol):
    global state
    for j in range(3):
        if game[j][0] == game[j][1] == game[j][2] == symbol:
            print_game(game)
            print(symbol, "wins")
            state = 1
        if game[0][j] == game[1][j] == game[2][j] == symbol:
            print_game(game)
            print(symbol, "wins")
            state = 1
        if game[0][0] == game[1][1] == game[2][2] == symbol:
            print_game(game)
            print(symbol, "wins")            
            state = 1
        if game[2][0] == game[1][1] == game[0][2] == symbol:
            print_game(game)
            print(symbol, "wins")
            state = 1


def move(game):
    cell = input_validation(input())
    if cell:
        if game[cell[1]][cell[0]] == "_":
            game[cell[1]][cell[0]] = player
            draw_check(game)
            win_check(game, player)
            return True
        else:
            print("This cell is occupied! Choose another one!")
            return False
    else:
        return False


state = 0
player = "X"
playground = [["_", "_", "_"] for i in [0, 1, 2]]

while not state:
    print_game(playground)
    while not move(playground):
        pass
    if player == "X":
        player = "O"
    else:
        player = "X"
