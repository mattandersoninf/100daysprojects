
"""
You could very easily make a default dict and map to
each of the option but the point of this exercise is
to practice making subclasses, that being said, I did
use dictionaries to the strengths of each obj. It is
possible to also make for instance a 'beat' method for
beating each individual hand so you wouldn't have to store
more information. Fruit for thought :)
"""

"""
The base playable hand class that all playable hands will derive from
"""

class playable_hands:
    """
    1. The game is currently intended to only support only 2 players
    2. Add on a loss counter to track of the amount of opponents hands that beat
       your hand that round, the one with the highest number of losses will be
       removed from the current game, in case you want to expand the number of
       of possible players
    3. The name for each playable hand will be represented by the first 3
       letters of the word associated
    """
    def __init__(self, name, strength={}): #loss_counter = 0
        self.name = name
        self.strength = strength

    def get_strength(self):
        return self.__strength

class rock(playable_hands):
    def __init__(self):
        super().__init__(name = 'roc', strength={
            'fire':'pounds out',
            'snake': 'crushes',
            'human': 'crushes',
            'wolf': 'crushes',
            'sponge': 'crushes',
            'tree': 'blocks growth of',
        })

class fire(playable_hands):
    def __init__(self):
        super().__init__(name = 'fir', strength={
            'scissors': 'melts',
            'paper': 'burns',
            'snake': 'burns',
            'human': 'burns',
            'tree': 'burns',
            'wolf': ' burns',
            'sponge':'burns',
        })

class scissors(playable_hands):
    def __init__(self):
        super.__init__(name='sci', strength={
            'air': 'swishes through',
            'tree':'carve',
            'paper': 'cut',
            'snake':'cut',
            'human':'cut',
            'wolf':'cut',
            'sponge':'cut',
        })

class snake(playable_hands):
    def __init__(self):
        super().__init__(name = 'sci', strength={
            'human': 'bites',
            'wolf': 'bites',
            'sponge': 'swallows',
            'tree': 'nests in',
            # how in the world does this make sense??? but, dems the rules
            'paper': 'nests in',
            'air': 'breathes',
            'water': 'drinks',
        })


class human(playable_hands):
    def __init__(self):
        super().__init__(name = 'hum', strength={
            'tree': 'plants',
            'wolf': 'tames',
            'sponge': 'cleans with',
            'paper': 'writes',
            'air': 'breathes',
            'water': 'drinks',
            'dragon': 'slays',
        })


class tree(playable_hands):
    def __init__(self):
        super().__init__(name = 'tre', strength={
            'wolf': 'shelters',
            # That's either a very big tree or a very small dragon
            'dragon': 'shelters',
            'sponge': 'outlives',
            'paper': 'becomes',
            'air': 'produces',
            'water': 'drinks',
            'devil': 'imprisons',
        })


class wolf(playable_hands):
    def __init__(self):
        super().__init__(name='wol', strength={
            'sponge': 'chews up',
            'paper': 'chews up',
            'air': 'breathes',
            'water': 'drinks',
            # Can't the dragon just fly???
            'dragon': 'outruns',
            'lightning': 'devil',
            'devil': 'bites booty of',
        })


class sponge(playable_hands):
    def __init__(self):
        super().__init__(name='spo', strength={
            'paper': 'soaks',
            'air': 'uses pockets',
            'water': 'absorbs',
            'devil': 'cleanses',
            'dragon': 'cleanses',
            'gun': 'cleans',
            'lightning': 'conducts',
        })


class paper(playable_hands):
    def __init__(self):
        super().__init__(name='pap', strength={
            'air': 'fans',
            'rock': 'covers',
            'water': 'floats on',
            'devil': 'rebukes',
            'dragon': 'rebukes',
            'gun': 'outlaws',
            'lightning': 'defines',
        })


class air(playable_hands):
    def __init__(self):
        super().__init__(name = 'air', strength={
            'fire': 'blows out',
            'rock': 'erodes',
            'water': 'evaporates',
            'devil': 'chokes',
            'gun': 'tarnishes',
            'dragon': 'freezes',
            'lightning': 'creates',
        })


class water(playable_hands):
    def __init__(self):
        super().__init__(name = 'wat', strength={
            'devil': 'drowns',
            'dragon': 'drowns',
            'rock': 'erodes',
            'fire': 'puts out',
            'scissors': 'rusts',
            'gun': 'rusts',
            'lightning': 'conducts',
        })


class dragon(playable_hands):
    def __init__(self):
        super().__init__(name = 'dra', strength={
            'devil': 'commands',
            # It breathes both lightning and fire!!
            'lightning': 'breathes',
            'fire': 'breathes',
            'rock': 'rests on',
            'scissors': 'immune to',
            'gun': 'immune to ',
            'snake': 'spawns',
        })


class devil(playable_hands):
    def __init__(self):
        super().__init__(name = 'dev', strength={
            'rock': 'hurls',
            'fire': 'breathes',
            'scissors': 'immune to',
            'gun': 'immune to',
            'lightning': 'casts',
            'snakes': 'eats',
            'human': 'possesses',
        })


class lightning(playable_hands):
    def __init__(self):
        super().__init__(name = 'lig', strength={
            'gun': 'melts',
            'scissors': 'melts',
            'rock': 'splits',
            'tree': 'splits',
            'fire': 'starts',
            'snake': 'strikes',
            'human': 'strikes',
        })


class gun(playable_hands):
    def __init__(self):
        super().__init__(name = 'gun', strength={
            'rock': 'targets',
            'tree': 'targets',
            # Who shoots at fire??
            'fire': 'targets',
            'scissors': 'outclasses',
            'snake': 'shoots',
            'human': 'shoots',
            'wolf': 'shoots',
        })
