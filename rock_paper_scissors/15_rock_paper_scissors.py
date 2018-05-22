from playable_hands import playable_hands

def handFight(hand1, hand2):
    if hand1.name in hand2.strength:
        print('{} {} {} \n'.format(hand1.name, hand2.strength[hand1.name], hand2.name))
    elif hand2.name in hand1.strength:
        print('{} {} {} \n'.format(hand2.name, hand1.strength[hand2.name], hand1.name))
    else:
        print('Nothing happened. Neither hand beats the other.')


def main():

    while True:

        print("Let's play Rock Paper Scissors x15")

        player1 = input('Choose your hand: \n[roc]k, \n[fir]e, \n[sci]ssors, \n[sna]ke, \n[hum]an, \n[tre]e, \n[wol], \n[spo]nge, \n[pap]er, \n[air], \n[wat]er, \n[dra]gon, \n[dev]il, \n[lig]htening, \n[gun] \n')

        p1 = playable_hands.hand_dict(player1)

        player2 = input('Choose your hand: \n[roc]k, \n[fir]e, \n[sci]ssors, \n[sna]ke, \n[hum]an, \n[tre]e, \n[wol], \n[spo]nge, \n[pap]er, \n[air], \n[wat]er, \n[dra]gon, \n[dev]il, \n[lig]htening, \n[gun] \n')

        p2 = playable_hands.hand_dict(player2)

        handFight(p1, p2)

        rerun = input('Do you want to play again? [y] for yes and any other key for no')

        if rerun != 'y': break



if __name__=='__main__':
    main()