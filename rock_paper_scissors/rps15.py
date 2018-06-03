import csv
import collections as c

# defaultdictionary object to hold all of the data collected from the csv file
hands_dict = c.defaultdict(dict)


def setup():
    with open('data-attacker.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hands_dict[row['Attacker']] = row
    f.close()


def game_loop():
    # keeps track of the attempts for giving a valid input for the game
    incorrect_input_counter = 5
    cmd1 = None
    hand_dict_1 = None

    """
    # grab the data in the table for the different playable options
    # use it after getting user inputs
    """

    # this loop is for getting the first player's hand

    while incorrect_input_counter > 0:

        cmd1 = input(
            "Choose your hand: \n[Rock], \n[Fire], \n[Scissors], \n[Snake], \n[Human], \n[Tree], \n[Wolf], \n[Sponge], \n[Paper], \n[Air], \n[Water], \n[Dragon], \n[Devil], \n[Lightening], \n[Gun] \n")

        try:
            hand_dict_1 = hands_dict[cmd1]
        except(KeyError):
            print("{} is not a valid input. Please try again.\n".format(cmd1))
            print("You have {} attempts to pick a hand.\n".format(str(incorrect_input_counter)))
            incorrect_input_counter -= 1

    if incorrect_input_counter <= 0:
        print("You entered too many invalid inputs.\n")
        teardown()

    print("Your attempts to give a valid input were reset to {}.".format(str(incorrect_input_counter)))
    incorrect_input_counter = 5

    while incorrect_input_counter > 0:

        cmd2 = input(
            "Choose your hand: \n[Rock], \n[Fire], \n[Scissors], \n[Snake], \n[Human], \n[Tree], \n[Wolf], \n[Sponge], \n[Paper], \n[Air], \n[Water], \n[Dragon], \n[Devil], \n[Lightening], \n[Gun] \n")

        try:
            if hand_dict_1[cmd2] != 'L' or hand_dict_1[cmd2] != 'D':
                print("{} {} {} \n".format(cmd1, hand_dict_1[cmd2], cmd2))
            elif hand_dict_1[cmd2] == 'L':
                print("{} {} {} \n".format(cmd2, hands_dict[cmd2][cmd1], cmd1))
            else:
                print("You both chose the same hand: {}\n".format(cmd1))

        except(KeyError):
            print("{} is not a valid input. Please try again. \n".format(cmd1))
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


def print_header():
    print("Let's play Rock Paper Scissors x15.")


def teardown():
    # this function is terminating the program
    f = open('data-attacker.csv')
    if not f.closed:
        f.close()
    print('The game is over.')
    exit()


def main():
    print_header()

    game_loop()


"""
if __name__ == '__main__':
    print(hands_dict.items())
"""
