from ..my_module import add_one
from ..my_module import echo
from ..my_module import msg_length


def test_add_one():
    assert add_one(1) == 2


def test_echo():
    echo("hello pkg")


def test_message_length():
    ml = msg_length("hello pkg")
    assert ml == 9
