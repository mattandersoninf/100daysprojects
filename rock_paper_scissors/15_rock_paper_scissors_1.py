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
    game_loop()


if __name__=='__main__':
    main()