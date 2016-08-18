#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


next_terminal = "()()"


class SlotDefinedClass(object):
    __slots__ = tuple()

    def __init__(self, **kwargs):
        for attr in self.__slots__:
            setattr(self, attr, kwargs[attr])


class Node(SlotDefinedClass):
    __slots__ = ("label", "leftmost_child", "right_sibling")


def make_node0(x):
    root = Node(label=x, leftmost_child=None, right_sibling=None)
    return root


def make_node1(x, t):
    root = make_node0(x)
    root.leftmost_child = t
    return root


def make_node4(x, t1, t2, t3, t4):
    root = make_node1(x, t1)
    t1.right_sibling = t2
    t2.right_sibling = t3
    t3.right_sibling = t4
    return root


def B():
    global next_terminal

    if next_terminal[0] == "(":
        next_terminal = next_terminal[1:]
        first_b = B()
        if first_b and next_terminal[0] == ")":
            next_terminal = next_terminal[1:]
            second_b = B()
            if not second_b:
                return None
            else:
                return make_node4("B", make_node0("("), first_b, make_node0(")"), second_b)
        else:
            return None
    else:
        return make_node1("B", make_node0("e"))


def main():
    global next_terminal
    parse_tree = B()

    print(parse_tree)

    return 0


if __name__ == "__main__":
    main()

