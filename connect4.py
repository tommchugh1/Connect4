
class setup:

    def __init__(self):
        self.default = {1: "|               |", 
                        2: "|               |", 
                        3: "|               |", 
                        4: "|               |", 
                        5: "|               |", 
                        6: "|               |", 
                        7: "| 1 2 3 4 5 6 7 |"}
        self.active = self.default

    def __repr__(self):
        state = ""
        for row in self.active.values():
            state += row + "\n"
        return state

    def reset_game(self):
        self.active = self.default

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

#def input(setup, player, position):

grid = setup()
print(grid)

grid.reset_game()
startup()


