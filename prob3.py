#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Leonard Chan

Just run `python prob3.py`. The code prints the trees and contains
asserttions, so the code should run normally if everything is correct.
"""

from __future__ import print_function

import json


# String to parse
next_terminal = "()()"


class SlotDefinedClass(object):
    __slots__ = tuple()

    def __init__(self, **kwargs):
        for attr in self.__slots__:
            setattr(self, attr, kwargs[attr])


class Node(SlotDefinedClass):
    """Nodes of tree."""
    __slots__ = ("label", "leftmost_child", "right_sibling")

    def dict(self):
        """Dict representation of this tree."""
        d = {}
        for k in self.__slots__:
            v = getattr(self, k)
            if isinstance(v, Node):
                v = v.dict()
            d[k] = v
        return d

    def height(self):
        """Height of tree."""
        lh = rh = 0
        if self.leftmost_child:
            lh = self.leftmost_child.height()
        if self.right_sibling:
            rh = self.right_sibling.height()
        return max(lh, rh) + 1

    def pre_order_labels(self):
        """Get list of labels traversed in pre order."""
        acc = [self.label]
        if self.leftmost_child:
            acc += self.leftmost_child.pre_order_labels()
        if self.right_sibling:
            acc += self.right_sibling.pre_order_labels()
        return acc

    def post_order_labels(self):
        """Get list of labels traversed in post order."""
        acc = []
        if self.leftmost_child:
            acc += self.leftmost_child.post_order_labels()
        if self.right_sibling:
            acc += self.right_sibling.post_order_labels()
        acc.append(self.label)
        return acc


def make_node0(x):
    """Make leaf."""
    root = Node(label=x, leftmost_child=None, right_sibling=None)
    return root


def make_node1(x, t):
    """Make node with only left branch."""
    root = make_node0(x)
    root.leftmost_child = t
    return root


def make_node4(x, t1, t2, t3, t4):
    """Make node with nested right branches."""
    root = make_node1(x, t1)
    t1.right_sibling = t2
    t2.right_sibling = t3
    t3.right_sibling = t4
    return root


def B():
    """Create parse tree."""
    global next_terminal

    if next_terminal and next_terminal[0] == "(":
        next_terminal = next_terminal[1:]
        first_b = B()
        if first_b and next_terminal and next_terminal[0] == ")":
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
    """Program entry point."""
    global next_terminal
    parse_tree = B()

    # Pretty print tree as dict of nested dicts
    print(json.dumps(parse_tree.dict(), indent=4))

    # Assertions/tests
    assert parse_tree.height() == 10
    assert "".join(parse_tree.pre_order_labels()) == "B(Be)B(Be)Be"
    assert "".join(parse_tree.post_order_labels()) == "eeeB)B(B)B(B"

    return 0


if __name__ == "__main__":
    main()

