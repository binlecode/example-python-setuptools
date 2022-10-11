import sys

# import os

# add project root to sys path to resolve package modules
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append("..")

from my_pkg import my_module as mm


def test_add_one():
    assert mm.add_one(1) == 2


def test_echo():
    mm.echo("hello pkg")


def test_message_length():
    ml = mm.msg_length("hello pkg")
    assert ml == 9
