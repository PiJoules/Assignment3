#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


class SlotDefinedClass(object):
    __slots__ = tuple()

    def __init__(self, **kwargs):
        for attr in self.__slots__:
            setattr(self, attr, kwargs[attr])


class Rule(SlotDefinedClass):
    @classmethod
    def matches_rule(cls, s):
        raise NotImplementedError

    @classmethod
    def match_rule(self, s):
        raise NotImplementedError


class S(Rule):
    """
    <S> -> wc<S>
    <S> -> {<T>
    <S> ->s;
    """

    @classmethod
    def matches_rule(cls, s):
        if len(s) >= 2 and s[:2] == "wc" and cls.matches_rule(s[2:]):
            return True

        if len(s) >= 1 and s[0] == "{" and cls.matches_rule(s[1:]):
            return True

        if len(s) >= 2 and s[:2] == "s;":
            return True

        return False


class T(Rule):
    """
    <T> -> <S><T>
    <T> -> }
    """

    @classmethod
    def matches_rule(cls, s):
        if len(s) >= 2 and s[:2] == "wc" and cls.matches_rule(s[2:]):
            return True

        if len(s) >= 1 and s[0] == "{" and cls.matches_rule(s[1:]):
            return True

        if len(s) >= 2 and s[:2] == "s;":
            return True

        return False


def parse(query):
    stack = []
    stack.append(S)
    lookahead = query[0]
    while stack:
        top = stack[0]
        if top == "e":
            pass


def main():
    return 0


if __name__ == "__main__":
    main()

