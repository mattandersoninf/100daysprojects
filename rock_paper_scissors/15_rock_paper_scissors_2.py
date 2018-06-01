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

    while incorrect_input_counter > 0:

        cmd1 = input('Choose your hand: \n[Rock], \n[Fire], \n[Scissors], \n[Snake], \n[Human], \n[Tree], \n[Wolf], \n[Sponge], \n[Paper], \n[Air], \n[Water], \n[Dragon], \n[Devil], \n[Lightening], \n[Gun] \n')

        with open('data-attackers.csv') as att:

            reader = csv.DictReader(att)

            for row in reader:

                if row[cmd1] != None:

                    hand_1_str = row[cmd1]

                    break







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