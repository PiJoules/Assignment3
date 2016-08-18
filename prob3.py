#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


class SlotDefinedClass(object):
    __slots__ = tuple()

    def __init__(self, **kwargs):
        for attr in self.__slots__:
            setattr(self, attr, kwargs[attr])


class Node(object):
    __slots__ = ("label", "leftmost_child", "right_sibling")


def make_node0(x):
    pass


def make_node1(x, t):
    pass


def make_node4(x, t1, t2, t3, t4):
    pass


def main():
    return 0


if __name__ == "__main__":
    main()

