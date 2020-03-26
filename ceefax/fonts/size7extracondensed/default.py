#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fonts.LetterBlock import LetterBlock

SIZE = 7
alphabet = {}


def _add(letter, string):
    global alphabet
    assert len(letter.split("\n")) == SIZE
    alphabet[letter] = LetterBlock(letter)


_add("'", " x\n"
          " x\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx")

_add("(", "xxx\n"
          "' x\n"
          " 'x\n"
          " 'x\n"
          " 'x\n"
          ", x\n"
          "xxx\n"
          "xxx")

_add(")", "xxx\n"
          " 'x\n"
          "' x\n"
          "' x\n"
          "' x\n"
          " ,x\n"
          "xxx\n"
          "xxx")

_add("&", "xxxx\n"
          "xxxx\n"
          "x xx\n"
          "   x\n"
          "x xx\n"
          "xxxx\n"
          "xxxx\n"
          "xxxx")

_add("|", "x\n"
          "x\n"
          "x\n"
          "x\n"
          "x\n"
          "x\n"
          "x\n"
          "x")

_add("-", "xx\n"
          "xx\n"
          "xx\n"
          " x\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx")

_add("!", "xxx\n"
          " x\n"
          " x\n"
          " x\n"
          "xx\n"
          " x\n"
          "xx\n"
          "xx")

_add("?", "xxx\n"
          "  x\n"
          "x x\n"
          " xx\n"
          "xxx\n"
          " xx\n"
          "xxx\n"
          "xxx")


_add("/", "xxxx\n"
          "xx x\n"
          "x',x\n"
          "x xx\n"
          "',xx\n"
          " xxx\n"
          "xxxx\n"
          "xxxx")

_add(" ", "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx")

_add("A", "xxxx\n"
          "' 'x\n"
          " x x\n"
          "   x\n"
          " x x\n"
          " x x\n"
          "xxxx\n"
          "xxxx")

_add("B", "xxxx\n"
          "  'x\n"
          " x x\n"
          "  xx\n"
          " x x\n"
          "  ,x\n"
          "xxxx\n"
          "xxxx")

_add("C", "xxx\n"
          "  x\n"
          " xx\n"
          " xx\n"
          " xx\n"
          "  x\n"
          "xxx\n"
          "xxx")

_add("D", "xxxx\n"
          "  'x\n"
          " x x\n"
          " x x\n"
          " x x\n"
          "  ,x\n"
          "xxxx\n"
          "xxxx")

_add("E", "xxx\n"
          "  x\n"
          " xx\n"
          "  x\n"
          " xx\n"
          "  x\n"
          "xxx\n"
          "xxx")

_add("F", "xxxx\n"
          "  x\n"
          " xx\n"
          "  x\n"
          " xx\n"
          " xx\n"
          "xxx\n"
          "xxx")

_add("G", "xxxx\n"
          "' 'x\n"
          " xxx\n"
          " x'x\n"
          " x x\n"
          ",' x\n"
          "xxxx\n"
          "xxxx")

_add("H", "xxxx\n"
          " x x\n"
          " x x\n"
          "   x\n"
          " x x\n"
          " x x\n"
          "xxxx\n"
          "xxxx")

_add("I", "xx\n"
          " x\n"
          " x\n"
          " x\n"
          " x\n"
          " x\n"
          "xx\n"
          "xx")

_add("J", "xxxx\n"
          "xx x\n"
          "xx x\n"
          "xx x\n"
          "'x x\n"
          ", ,x\n"
          "xxxx\n"
          "xxxx")

_add("K", "xxxx\n"
          " x x\n"
          " x x\n"
          "  xx\n"
          " x x\n"
          " x x\n"
          "xxxx\n"
          "xxxx")

_add("L", "xxx\n"
          " xx\n"
          " xx\n"
          " xx\n"
          " xx\n"
          "  x\n"
          "xxx\n"
          "xxx")

_add("M", "xxxxxx\n"
          " 'x' x\n"
          " , , x\n"
          " x,x x\n"
          " xxx x\n"
          " xxx x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("N", "xxxx\n"
          "  'x\n"
          " x x\n"
          " x x\n"
          " x x\n"
          " x x\n"
          "xxxx\n"
          "xxxx")

_add("O", "xxxx\n"
          "' 'x\n"
          " x x\n"
          " x x\n"
          " x x\n"
          ", ,x\n"
          "xxxx\n"
          "xxxx")

_add("P", "xxxx\n"
          "  'x\n"
          " x x\n"
          "   x\n"
          " xxx\n"
          " xxx\n"
          "xxxx\n"
          "xxxx")

_add("Q", "xxxx\n"
          "' 'x\n"
          " x x\n"
          " x x\n"
          " x x\n"
          ",  x\n"
          "xxxx\n"
          "xxxx")

_add("R", "xxxx\n"
          "  'x\n"
          " x x\n"
          "  ,x\n"
          " x x\n"
          " x x\n"
          "xxxx\n"
          "xxxx")

_add("S", "xxx\n"
          "  x\n"
          " xx\n"
          "  x\n"
          "x x\n"
          "  x\n"
          "xxx\n"
          "xxx")

_add("T", "xxxx\n"
          "   x\n"
          "x xx\n"
          "x xx\n"
          "x xx\n"
          "x xx\n"
          "xxxx\n"
          "xxxx")

_add("U", "xxxx\n"
          " x x\n"
          " x x\n"
          " x x\n"
          " x x\n"
          ", ,x\n"
          "xxxx\n"
          "xxxx")

_add("V", "xxxx\n"
          " x x\n"
          " x x\n"
          " x x\n"
          " x x\n"
          "  ,x\n"
          "xxxx\n"
          "xxxx")

_add("W", "xxxxxx\n"
          " xxx x\n"
          " xxx x\n"
          " x'x x\n"
          " x x x\n"
          "  ,  x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("X", "xxxx\n"
          " x x\n"
          ",',x\n"
          "x xx\n"
          "','x\n"
          " x x\n"
          "xxxx\n"
          "xxxx")

_add("Y", "xxxx\n"
          " x x\n"
          " x x\n"
          ", ,x\n"
          "x xx\n"
          "x xx\n"
          "xxxx\n"
          "xxxx")

_add("Z", "xxxx\n"
          "   x\n"
          "xx x\n"
          "x ,x\n"
          " xxx\n"
          "   x\n"
          "xxxx\n"
          "xxxx")

_add("1", "xx\n"
          " x\n"
          " x\n"
          " x\n"
          " x\n"
          " x\n"
          "xx\n"
          "xx")

_add("2", "xxxx\n"
          "   x\n"
          "xx x\n"
          "   x\n"
          " xxx\n"
          "   x\n"
          "xxxx\n"
          "xxxx")

_add("3", "xxxx\n"
          "   x\n"
          "xx x\n"
          "   x\n"
          "xx x\n"
          "   x\n"
          "xxxx\n"
          "xxxx")

_add("4", "xxxx\n"
          " x x\n"
          " x x\n"
          "   x\n"
          "xx x\n"
          "xx x\n"
          "xxxx\n"
          "xxxx")

_add("5", "xxxx\n"
          "   x\n"
          " xxx\n"
          "   x\n"
          "xx x\n"
          "   x\n"
          "xxxx\n"
          "xxxx")

_add("6", "xxxx\n"
          "   x\n"
          " xxx\n"
          "   x\n"
          " x x\n"
          "   x\n"
          "xxxx\n"
          "xxxx")

_add("7", "xxxx\n"
          "   x\n"
          "xx x\n"
          "xx x\n"
          "xx x\n"
          "xx x\n"
          "xxxx\n"
          "xxxx")

_add("8", "xxxx\n"
          "   x\n"
          " x x\n"
          "   x\n"
          " x x\n"
          "   x\n"
          "xxxx\n"
          "xxxx")

_add("9", "xxxx\n"
          "   x\n"
          " x x\n"
          "   x\n"
          "xx x\n"
          "   x\n"
          "xxxx\n"
          "xxxx")

_add("0", "xxxx\n"
          "   x\n"
          " x x\n"
          " x x\n"
          " x x\n"
          "   x\n"
          "xxxx\n"
          "xxxx")

_add(".", "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          " x\n"
          "xx\n"
          "xx")

_add("*", "xxxxx xxxxxx\n"
          "x,'xx,xx',xx\n"
          "xxx'   'xxxx\n"
          ",,x     x,,x\n"
          "xxx,   ,xxxx\n"
          "x',xx'xx,'xx\n"
          "xxxxx xxxxxx\n"
          "xxxxx xxxxxx")

# cloud
_add("@", "xxxxxxxxxxxxx\n"
          "xxxx'''xxxxxx\n"
          "x'',xxx,'xxxx\n"
          " xx,xxx',,,'x\n"
          ",'''''''''',x\n"
          "xxxxxxxxxxxxx\n"
          "xxxxxxxxxxxxx\n"
          "xxxxxxxxxxxxx")

# rain
_add("{", "xxx',,,'xxxxx\n"
          "',,'xxxx ''xx\n"
          " xxxxxx,xxx x\n"
          "x,,,,,,,,,,xx\n"
          "xx','xxxx'xxx\n"
          "x,''',x',x,'x\n"
          "xxxxxxx,''',x\n"
          "xxxxxxx,''',x")

# moon
_add("}", "xxx'' ,,x\n"
          "x'   ,xxx\n"
          "'   xxxxx\n"
          "    xxxxx\n"
          ",   xxxxx\n"
          "x,   'xxx\n"
          "xxx,, ''x\n"
          "xxx,, ''x")

# cloud sun
_add("~", "xxxxxxxxxxxxxxxx\n"
          "xxx',,,'xx xx'xx\n"
          "',,'xxxx ''x,xxx\n"
          " xxxxxx,xxx x,,x\n"
          "x,,,,,,,,,,x'xxx\n"
          "xxxxxxxxxx xx,xx\n"
          "xxxxxxxxxxxxxxxx\n"
          "xxxxxxxxxxxxxxxx")

# storm
_add("^", "xxx',,,'xxxxx\n"
          "',,'xxxx'xxxx\n"
          " xxxxxx, ''xx\n"
          "x,,x'   ,,,'x\n"
          "xxx,  'xxxx x\n"
          "xxxxx,  'x',x\n"
          "xxxx' ,x,x,xx\n"
          "xxxx' ,x,x,xx")

# snow
_add("%", "xxx',,,'xxxxx\n"
          "',,'xxxx ''xx\n"
          " xxxxxx,xxx x\n"
          "x,,,,,,,,,,xx\n"
          "xxxxxx,',xxxx\n"
          "x,',xx,x,xxxx\n"
          "x,x,xxxxxxxxx\n"
          "x,x,xxxxxxxxx")


def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError:
        return LetterBlock("xxxxx\n"
                           "xxxxx\n"
                           "xxxxx\n"
                           " ,, x\n"
                           " '' x\n"
                           "xxxxx\n"
                           "xxxxx\n"
                           "xxxxx")
