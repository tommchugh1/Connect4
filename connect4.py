

default_setup = {1: ["|               |"], 
                2: ["|               |"], 
                3: ["|               |"], 
                4: ["|               |"], 
                5: ["|               |"], 
                6: ["|               |"], 
                7: ["| 1 2 3 4 5 6 7 |"]}


def reset_game():
    active_setup = default_setup

def startup():
    print("WELCOME TO CONNECT 4:")
    player1_name = input("Please input player 1 name: ")
    player1_symbol = input("Please input Player 1 symbol: ")
    while len(player1_symbol) > 1:
        player1_symbol = input("Symbols can only be 1 character, please input again: ")
    player2_name = input("Please input player 2 name: ")
    player2_symbol = input("Please input Player 2 symbol: ")
    while len(player2_symbol) > 1:
        player2_symbol = input("Symbols can only be 1 character, please input again: ")

reset_game()
startup()


