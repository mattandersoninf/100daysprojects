import unittest
import pytest
import rps15
import sys


def test_print_header():
    rps15.print_header()
    assert sys.stdout.getvalue().strip() == "Let's play Rock Paper Scissors x15."

@pytest.mark.parameterize("test_input, expected", [
    """
    {} is not a valid input. Please try again.
    """
    ('a',"'a' is not a valid input. Please try again. \nYou have 4 attempts to pick a hand.\n")
    'b',
    'c',
    'd',
    'e'
])
def test_invalid_inputs():
    """
    since the dictionary's only except key values that already exist in them,
    let's take a look a how invalid keys are being handled
    """
    rps15.game_loop()



def test_rock():
    rps15.game_loop()



def test_fire():



def test_scissors():



def test_snake():



def test_human():



def test_tree():



def test_wolf():



def test_sponge():



def test_paper():



def test_air():



def test_water():



def test_dragon():



def test_devil():



def test_lightning():


def test_gun()


if __name__ == '__main__':
    test_print_header()