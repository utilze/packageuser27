#! /BiO/Access/home/user27/.pyenv/shims/python

from packageuser27.addition import add
def test_add():
 assert add(2, 3) == 5
 assert add(-1, 1) == 0
 assert add(-1, -1) == -2
 assert add(0, 0) == 0
