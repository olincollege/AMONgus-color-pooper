"""
Unit tests for Amon.
"""
# import pygame
import pytest #pylint: disable=unused-import
from amon import Amon

# def test_movement():
#     """
#     Test to see if Amon takes and interprets user input correctly
#     """
#     user = Amon()
#     initial_position=user.amon_stats[0]
#     user.movement(pygame.K_LEFT)
#     assert amon_stats()[0]==(initial_position-2)

def test_does_amon_exist():
    '''
    Test to see if we can sucessfully initiate an instance of Amon with
    correct attributes
    '''
    user = Amon()
    assert user.amon_stats == [200, 200, "down", "red"]


def test_out_of_bounds():
    '''
    Test to see if Amon successfully detects when he is out-of-bounds and
    self corrects.
    '''
    user = Amon()
    user.update_x_and_y(300,300)
    user.amon_passive_update()
    user.amon_passive_update()
    assert user.amon_stats == [478, 472, "down", "red"]


def test_in_bounds():
    '''
    Test to see if Amon sucessfully moves whilst inbounds
    '''
    user = Amon()
    user.update_x_and_y(50,50)
    user.amon_passive_update()
    user.amon_passive_update()
    assert user.amon_stats == [250, 250, "down", "red"]
