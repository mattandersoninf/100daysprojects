"""
 1. Creature class to hold all playable actions by the
    characters in the dnd_game file
 2. Grab the random class because we're going to
    be rolling dice to determine game actions
"""

import random

class Creature:
    # initialize a character object with a name and level
	# name = str, level = int
	def __init__(self, name, level):
        self.name = name
        self.level = level

    # every character gets the option to roll and activate
    # randomize a twelve sided die and return the value
    def defensive_roll(self) -> int:
        roll = random.randint(1,12)
        return roll * self.level

# Create Dragon creature that is a subclass of the creature class
# So the Dragon class inherits traits from the creature class
class Dragon(Creature):
    # initialize the Draon creature and inherit the parameters from the creature class
    def __init__(self, name, level, scaliness, breathes_fire = False):
        super().__init__(name,level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    # extra properties from the Dragon class take affect into the defensive roll for the creature
    def defensive_roll(self) -> int:

        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breathes_fire:
            value = value * 2
        return value

# Create Wizard creature that can fight back against the player
# subclass of the create class, you don't need a new initializer or defensive roll
# because it's only for striking back at the character
class Wizard(Creature):

    def attack(self, creature) -> bool:

        my_roll = self.defensive_roll()
        opponent_roll = creature.defensive_roll()
        
        return my_roll >= opponent_roll