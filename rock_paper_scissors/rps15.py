import csv
import collections as c

# defaultdictionary object to hold all of the data collected from the csv file
hands_dict = c.defaultdict(dict)

"""
Form a dictionary from scraping the csv data.
"""
def setup():
    with open('data-attacker.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hands_dict[row['Attacker']] = row
    f.close()

"""
All game functions will be handled in this method. Functions similarly to DND game loop.
"""
def game_loop():
    """
    The incorrect_input_counter keeps track of the attempts for giving
    a valid input for the game. It decrements every time you give an invalid input.
    """
    incorrect_input_counter = 5
    """
    This is to hold the first input command string from the game user. I'm only going
    to make an object of the first command because the second command is only for comparison,
    so there's no need to make another object and hold it throughout the game loop.
    """
    cmd1 = None
    """
    This dict is to hold all of the information scraped fromt he row that corresponds
    to the user's input. Same reason for only using 1 obj to hold the command applies
    to this dictionary.
    """
    hand_dict_1 = None


    """
    This loop is for getting the first player's hand. So long as the error counter is above
    0, the loop will continue.
    """
    while incorrect_input_counter > 0:
        """
        I added the title method to make the program a little more forgiving,
        if you type 'rock', it's acceptable any combination of the letters
        uppercase or lowercase will allow the gam to continue.
        """
        cmd1 = input(
            "Choose your hand: \n[Rock], \n[Fire], \n[Scissors], \n[Snake], \n[Human], \n[Tree], \n[Wolf], \n[Sponge], \n[Paper], \n[Air], \n[Water], \n[Dragon], \n[Devil], \n[Lightening], \n[Gun] \n").title()

        """
        Grab the row data from the csv file that corresponds to the user input.
        """
        try:
            hand_dict_1 = hands_dict[cmd1]
        except(KeyError):
            print("'{}' is not a valid input. Please try again.\n".format(cmd1))
            print("You have {} attempts to pick a hand.\n".format(str(incorrect_input_counter)))
            incorrect_input_counter -= 1

    """
    If the loop exited top early, exit the programm and let the user know that they gave too many
    invalid inputs.
    """
    if incorrect_input_counter <= 0:
        print("You entered too many invalid inputs.\n")
        teardown()

    """
    Reset the incorrect_input_counter and notify the player.
    """
    incorrect_input_counter = 5
    print("Your attempts to give a valid input were reset to {}.".format(str(incorrect_input_counter)))

    """
    Use this loop to compare the first player's hand against the second player.
    """
    while incorrect_input_counter > 0:

        """
        Grab the second player's input.
        """
        cmd2 = input(
            "Choose your hand: \n[Rock], \n[Fire], \n[Scissors], \n[Snake], \n[Human], \n[Tree], \n[Wolf], \n[Sponge], \n[Paper], \n[Air], \n[Water], \n[Dragon], \n[Devil], \n[Lightening], \n[Gun] \n").title()

        """
        Try to compare the player inputs against eachother to determine a winner.
        """
        try:
            if hand_dict_1[cmd2] != 'L' or hand_dict_1[cmd2] != 'D':
                print("{} {} {} \n".format(cmd1, hand_dict_1[cmd2], cmd2))
            elif hand_dict_1[cmd2] == 'L':
                print("{} {} {} \n".format(cmd2, hands_dict[cmd2][cmd1], cmd1))
            else:
                print("You both chose the same hand: {}\n".format(cmd1))
        except(KeyError):
            print("'{}' is not a valid input. Please try again. \n".format(cmd1))
            print("You have {} attempts to pick a hand. \n".format(str(incorrect_input_counter)))
            incorrect_input_counter -= 1

    if incorrect_input_counter <= 0:
        print("You entered too many invalid inputs.")
        teardown()
    else:
        final_cmd = input('Do you want to keep playing? Press [y] to continue, any other key will end the game')
        if final_cmd == 'y':
            pass
        else:
            teardown()

"""
This prints the inro message to the game.
"""
def print_header():
    print("Let's play Rock Paper Scissors x15.")


"""
This function is terminates the program by making sure the connection to the 
csv file is closed. Then it ends the program.
"""
def teardown():
    f = open('data-attacker.csv')
    if not f.closed:
        f.close()
    print('The game is over.')
    exit()


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()