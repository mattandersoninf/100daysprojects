import csv

def game_loop():

    incorrect_input_counter = 5

    # grab the data in the table for the different playable options
    # use it after getting user inputs
    """
    """

    hold_1 = None

    hand_1_str = None

    hold_2 = None

    hand_2_str = None

    with open('data-attackers.csv') as att:

        reader = csv.DictReader(att)

        while incorrect_input_counter > 0:

            cmd1 = input(
                'Choose your hand: \n[Rock], \n[Fire], \n[Scissors], \n[Snake], \n[Human], \n[Tree], \n[Wolf], \n[Sponge], \n[Paper], \n[Air], \n[Water], \n[Dragon], \n[Devil], \n[Lightening], \n[Gun] \n')

            for row in reader:

                if row[cmd1] != None:

                    hand_1_str = row[cmd1]

                    break

            if hand_1_str == None :

                print(cmd1+' is not a valid input.')

                incorrect_input_counter -= 1

            else: break

        if incorrect_input_counter == 0:


    cmd2 = input(
        'Choose your hand: \n[Rock], \n[Fire], \n[Scissors], \n[Snake], \n[Human], \n[Tree], \n[Wolf], \n[Sponge], \n[Paper], \n[Air], \n[Water], \n[Dragon], \n[Devil], \n[Lightening], \n[Gun] \n')


def print_header():
    print("Let's play Rock Paper Scissors x15.")


def teardown():
    # this function is terminating the program


def main():

    print_header()

    game_loop()


main()