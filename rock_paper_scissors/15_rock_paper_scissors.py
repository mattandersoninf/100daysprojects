from hands import playable_hands, rock,

def game_loop(hand1, hand2):
    if hand1.name in hand2.strength:
        print('{} {} {} \n'.format(hand1.name, hand2.strength[hand1.name], hand2.name))
    elif hand2.name in hand1.strength:
        print('{} {} {} \n'.format(hand2.name, hand1.strength[hand2.name], hand1.name))
    else:
        print('Nothing happened. Neither hand beats the other.')

    rerun = input('Do you want to play again? [y] for yes and any other key for no')

    if rerun != 'y': break


# there's a way to check whether the cmd is valid prior to putting it in the method to reduce the time,
# do some research
def choose_hand(cmd):
    if cmd == 'roc':
        return


def print_header():
    print("Let's play Rock Paper Scissors x15.")


def main():

    print_header()

    player1 = input('Choose your hand: \n[roc]k, \n[fir]e, \n[sci]ssors, \n[sna]ke, \n[hum]an, \n[tre]e, \n[wol], \n[spo]nge, \n[pap]er, \n[air], \n[wat]er, \n[dra]gon, \n[dev]il, \n[lig]htening, \n[gun] \n')

    player2 = input('Choose your hand: \n[roc]k, \n[fir]e, \n[sci]ssors, \n[sna]ke, \n[hum]an, \n[tre]e, \n[wol], \n[spo]nge, \n[pap]er, \n[air], \n[wat]er, \n[dra]gon, \n[dev]il, \n[lig]htening, \n[gun] \n')

    game_loop(p1, p2)


if __name__=='__main__':
    main()