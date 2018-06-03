import unittest
import pytest
import rps15

def test_getting_data_from_csv():
    while True:

        with open('data-attacker.csv') as f:

            reader = csv.DictReader(f)

            cmd = input('Please enter a hand value and see what comes out: \n')

            for row in reader:
                print("Here are your hand's weaknesses: {}".format(row[cmd]))

            print('\n')


def test_invalid_inputs():


def test_rock():



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