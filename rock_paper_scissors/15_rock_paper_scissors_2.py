import csv

def game_loop():

    incorrect_input_counter = 5

    # grab the data in the table for the different playable options
    # use it after getting user inputs
    """
    """

    hold_1 = None

    while incorrect_input_counter > 0:

        cmd1 = input('Choose your hand: \n[roc]k, \n[fir]e, \n[sci]ssors, \n[sna]ke, \n[hum]an, \n[tre]e, \n[wol], \n[spo]nge, \n[pap]er, \n[air], \n[wat]er, \n[dra]gon, \n[dev]il, \n[lig]htening, \n[gun] \n')

        with open('data-attackers.csv') as att:

            reader = csv.DictReader(att)

            for row in reader:





        with open('data-attackers.csv') as att:

            reader = csv.DictReader(att)

    cmd2 = input(

        'Choose your hand: \n[roc]k, \n[fir]e, \n[sci]ssors, \n[sna]ke, \n[hum]an, \n[tre]e, \n[wol], \n[spo]nge, \n[pap]er, \n[air], \n[wat]er, \n[dra]gon, \n[dev]il, \n[lig]htening, \n[gun] \n')



def print_header():
    print("Let's play Rock Paper Scissors x15.")


def main():

    print_header()

    game_loop()


main()