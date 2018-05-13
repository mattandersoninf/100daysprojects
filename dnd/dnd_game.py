"""
Simulate a game of DND using the object from the actors class
"""

from actors import Creature, Dragon, Wizard
import random


def main():
	print_header()
	game_loop()


def print_header():
	print('-----------------------------')
	print('          DND')
	print('-----------------------------')
	print()

def game_loop():
	creatures = [
		Creature('Bat', 5),
		Creature('Toad', 1),
		Creature('Tiger', 12),
		# based on the order, you could just said 2 after 50 but just to be safe,
		# define it directly
		Dragon('Black Dragon', 50, scaliness=2, breathes_fire=False),
		Wizard('Evil Wizard(aka Merlin)', 1000),
	]

	hero = Wizard('Gandolf', 75)

	"""
	let's make the game loop a little forgiving because it's possible that
	because it's possible that someone will accidentally hit the wrong key, so give
	the player three chances to hit a playable key, it's a global variable because
	while the game may be forgiving, it tells you the playable commends during the 
	game loop so you only have so many non renewable chances
	"""

	miss_counter = 3

	while True:
		# randomly select an oppenent creature
		active_creature = random.choice(creatures)

		# READY TO PLAY A GAME??
		# let the oppenent know what their oppnent in the game is
		print('A {} of level {} has appeared from a dark and foggy forrest...\n'.format((active_creature.name,active_creature.level)))

		# get the player's input commands to interact in the game
		cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
		# depending on the options, this is what you're going to do
		if cmd == 'a':
			if hero.attack(active_creature):
				creatures.remove(active_creature)
				print("The wizard has defeated {}".format((active_creature.name)))
			else:
				print("The wizard has been defeated by the powerful {}".format(active_creature.name))
		elif cmd == "r":
			print('The wizard has become unsure of his power and flees!!!')
		elif cmd == 'l':
			print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
			for c in creatures:
				print(" * {} of level {}".format(c.name,c.level))
		else:
			miss_counter-=1
			if miss_counter == 0:
				print("OK, exiting the game...bye!")
				break

		if not creatures:
			print("You've defeated all the creatures, well done!")
			break

		print()

if __name__=='__main__':
	main()