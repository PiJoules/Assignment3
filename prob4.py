#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Leonard Chan

Just run `python prob4.py`. The code prints the stack and lookahead contents  and contains
assertions, so the code should run normally if everything is correct.
"""


from __future__ import print_function


import json


class Node(object):
    __slots__ = ("label", "children")

    def __init__(self, **kwargs):
        for attr in self.__slots__:
            setattr(self, attr, kwargs[attr])

    def dict(self):
        d = {"label": self.label, "children": self.children}
        for i, child in enumerate(self.children):
            if isinstance(child, Node):
                d["children"][i] = child.dict()
        return d

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        return self.label == other.label

    def __str__(self):
        return str(self.dict())

    def height(self):
        """Height of tree."""
        heights = [0] * len(self.children)
        if not self.children:
            return 1
        max_height = max(child.height() for child in self.children)
        return max_height + 1

    def pre_order_labels(self):
        """Get list of labels traversed in pre order."""
        acc = [self.label]
        for child in self.children:
            acc += child.pre_order_labels()
        #if self.leftmost_child:
        #    acc += self.leftmost_child.pre_order_labels()
        #if self.right_sibling:
        #    acc += self.right_sibling.pre_order_labels()
        return acc

    def post_order_labels(self):
        """Get list of labels traversed in post order."""
        acc = []
        for child in self.children:
            acc += child.post_order_labels()
        #if self.leftmost_child:
        #    acc += self.leftmost_child.post_order_labels()
        #if self.right_sibling:
        #    acc += self.right_sibling.post_order_labels()
        acc.append(self.label)
        return acc


grammar = (
    ["w", "c", "<S>"],
    ["{", "<T>"],
    ["s", ";"],
    ["<S>", "<T>"],
    ["}"],
)


parse_table = {
    ("<S>", "w"): 0,
    ("<S>", "{"): 1,
    ("<S>", "s"): 2,
    ("<T>", "w"): 3,
    ("<T>", "{"): 3,
    ("<T>", "}"): 4,
    ("<T>", "s"): 3,
}


def copy_production(row):
    """Return the Node representations of the strings in each row in the grammar."""
    return [Node(label=x, children=[]) for x in grammar[row]]


def transform_parse_table():
    """Convert the string keys in the parse table to Node objects instead."""
    global parse_table
    for rule, lookahead in parse_table.iterkeys():
        parse_table[(Node(label=rule, children=[]), Node(label=lookahead, children=[]))] = parse_table.pop((rule, lookahead))


def parse(query):
    """Parse a list of nodes into a parse tree."""
    stack = []
    stack.append(Node(label="<S>", children=[]))
    head = stack[0]
    while stack:
        lookahead = query[0]

        # Print stack + lookahead on each iteration
        print([x.label for x in stack], lookahead.label)

        top = stack.pop(0)
        next_node = top
        if top == lookahead:
            lookahead = query.pop(0)
        else:
            action = parse_table[(top, lookahead)]
            symbols = copy_production(action)
            stack = symbols + stack
            next_node.children = symbols
    return head


def main():
    """Program entry point"""
    transform_parse_table()

    # Input
    sentence = ["{", "w", "c", "s", ";", "s", ";", "}"]
    tree = parse([Node(label=x, children=[]) for x in sentence])

    # Uncomment to see tree
    #print(json.dumps(tree.dict(), indent=4))
    assert tree.height() == 5
    assert ['<S>', '{', '<T>', '<S>', 'w', 'c', '<S>', 's', ';', '<T>', '<S>', 's', ';', '<T>', '}'] == tree.pre_order_labels()
    assert ['{', 'w', 'c', 's', ';', '<S>', '<S>', 's', ';', '<S>', '}', '<T>', '<T>', '<T>', '<S>'] == tree.post_order_labels()

    return 0


if __name__ == "__main__":
    main()

