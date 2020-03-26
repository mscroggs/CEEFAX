#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fonts.LetterBlock import LetterBlock
from random import choice

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

_add("&", "xxxx\n"
          "xxxx\n"
          "x xx\n"
          "   x\n"
          "x xx\n"
          "xxxx\n"
          "xxxx\n"
          "xxxx")

_add("#", "xxxxxx\n"
          "x x xx\n"
          "     x\n"
          "x x xx\n"
          "     x\n"
          "x x xx\n"
          "xxxxxx\n"
          "xxxxxx")

_add("|", "x\n"
          "x\n"
          "x\n"
          "x\n"
          "x\n"
          "x\n"
          "x\n"
          "x")

_add("-", "xxxx\n"
          "xxxx\n"
          "xxxx\n"
          "   x\n"
          "xxxx\n"
          "xxxx\n"
          "xxxx\n"
          "xxxx")

_add(".", "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx\n"
          "  x\n"
          "xxx\n"
          "xxx")

_add(":", "xxx\n"
          "xxx\n"
          "''x\n"
          ",,x\n"
          "''x\n"
          ",,x\n"
          "xxx\n"
          "xxx")

_add("!", "xxx\n"
          "  x\n"
          "  x\n"
          "  x\n"
          "xxx\n"
          "  x\n"
          "xxx\n"
          "xxx")

_add("?", "xxxxxxx\n"
          "'    'x\n"
          ",,xx  x\n"
          "xx'  ,x\n"
          "xx,,xxx\n"
          "xx  xxx\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("(", "xxxx\n"
          "x  x\n"
          "  xx\n"
          " xxx\n"
          "  xx\n"
          "x  x\n"
          "xxxx\n"
          "xxxx")

_add(")", "xxxx\n"
          "x  x\n"
          "xx\n"
          "xxx\n"
          "xx\n"
          "x  x\n"
          "xxxx\n"
          "xxxx")

_add("/", "xxxxxx\n"
          "xxxx x\n"
          "xxx xx\n"
          "xx xxx\n"
          "x xxxx\n"
          " xxxxx\n"
          "xxxxxx\n"
          "xxxxxx")

_add(" ", "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx")

_add(u"£", "xxxxxxx\n"
           "x'   'x\n"
           "x  x,,x\n"
           "    xxx\n"
           "x  xxxx\n"
           "      x\n"
           "xxxxxxx\n"
           "xxxxxxx")

_add(u"$", "xxxxxxx\n"
           "xx  xxx\n"
           "  ,,,,x\n"
           "      x\n"
           "''''  x\n"
           "xx  xxx\n"
           "xxxxxxx\n"
           "xxxxxxx")

_add(u"€", "xxxxxxx\n"
           "x'   'x\n"
           "'  'xxx\n"
           "'  'xxx\n"
           "x  xxxx\n"
           "x,   ,x\n"
           "xxxxxxx\n"
           "xxxxxxx")

_add(u"฿", "xxxxxxxxxxxxx\n"
           "xxxxxx' ' 'xx\n"
           "xxxxxx  xx  x\n"
           " , ,'x    ''x\n"
           " x x x  xx  x\n"
           " x x x, , ,xx\n"
           "xxxxxxxxxxxxx\n"
           "xxxxxxxxxxxxx")

_add(u"₺", "xxxxxxx\n"
           "x  x'xx\n"
           "'  ,xxx\n"
           "x  ',xx\n"
           ",  x''x\n"
           "x    ,x\n"
           "xxxxxxx\n"
           "xxxxxxx")

_add(u"¥", "xxxxxxx\n"
           "  xx  x\n"
           "  ''  x\n"
           "x,  ,xx\n"
           "x,  ,xx\n"
           "x,  ,xx\n"
           "xxxxxxx\n"
           "xxxxxxx")


_add("A", "xxxxxxx\n"
          "x'  'xx\n"
          "  xx  x\n"
          "  ''  x\n"
          "  ,,  x\n"
          "  xx  x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("B", "xxxxxxx\n"
          "     'x\n"
          "  xx  x\n"
          "     xx\n"
          "  xx  x\n"
          "     ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("C", "xxxxxxx\n"
          "'    'x\n"
          "  xx,,x\n"
          "  xxxxx\n"
          "  xx''x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("D", "xxxxxxx\n"
          "     xx\n"
          "  xx  x\n"
          "  xx  x\n"
          "  xx  x\n"
          "     xx\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("E", "xxxxxxx\n"
          "      x\n"
          "  xxxxx\n"
          "    xxx\n"
          "  xxxxx\n"
          "      x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("F", "xxxxxxx\n"
          "      x\n"
          "  xxxxx\n"
          "    xxx\n"
          "  xxxxx\n"
          "  xxxxx\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("G", "xxxxxxx\n"
          "'    'x\n"
          "  xx,,x\n"
          "  x'''x\n"
          "  x,  x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("H", "xxxxxxx\n"
          "  xx  x\n"
          "  xx  x\n"
          "      x\n"
          "  xx  x\n"
          "  xx  x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("I", "xxx\n"
          "  x\n"
          "  x\n"
          "  x\n"
          "  x\n"
          "  x\n"
          "xxx\n"
          "xxx")

_add("J", "xxxxxx\n"
          "xxx  x\n"
          "xxx  x\n"
          "xxx  x\n"
          "''x  x\n"
          ",   ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("K", "xxxxxxx\n"
          "  xx  x\n"
          "  x  xx\n"
          "    xxx\n"
          "  x  xx\n"
          "  xx  x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("L", "xxxxxx\n"
          "  xxxx\n"
          "  xxxx\n"
          "  xxxx\n"
          "  xxxx\n"
          "     x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("M", "xxxxxxxxx\n"
          "  xxxx  x\n"
          "   ''   x\n"
          "  ,  ,  x\n"
          "  x,,x  x\n"
          "  xxxx  x\n"
          "xxxxxxxxx\n"
          "xxxxxxxxx")

_add("N", "xxxxxxxx\n"
          "   xx  x\n"
          "    x  x\n"
          "  x    x\n"
          "  xx   x\n"
          "  xxx  x\n"
          "xxxxxxxx\n"
          "xxxxxxxx")

_add("O", "xxxxxxx\n"
          "'    'x\n"
          "  xx  x\n"
          "  xx  x\n"
          "  xx  x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("P", "xxxxxxx\n"
          "     'x\n"
          "  xx  x\n"
          "     ,x\n"
          "  xxxxx\n"
          "  xxxxx\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("Q", "xxxxxxx\n"
          "'    'x\n"
          "  xx  x\n"
          "  xx  x\n"
          "  x'',x\n"
          ", ',  x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("R", "xxxxxxx\n"
          "     'x\n"
          "  xx  x\n"
          "     ,x\n"
          "  xx 'x\n"
          "  xx  x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("S", "xxxxxxx\n"
          "'    'x\n"
          "  xxxxx\n"
          ",    'x\n"
          "xxxx  x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("T", "xxxxxxx\n"
          "      x\n"
          "xx  xxx\n"
          "xx  xxx\n"
          "xx  xxx\n"
          "xx  xxx\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("U", "xxxxxxx\n"
          "  xx  x\n"
          "  xx  x\n"
          "  xx  x\n"
          "  xx  x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("V", "xxxxxxx\n"
          "  xx  x\n"
          "  xx  x\n"
          "  xx  x\n"
          "x    xx\n"
          "xx  xxx\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("W", "xxxxxxxxx\n"
          "  xxxx  x\n"
          "  xxxx  x\n"
          "  x  x  x\n"
          "        x\n"
          "x  xx  xx\n"
          "xxxxxxxxx\n"
          "xxxxxxxxx")

_add("X", "xxxxxxx\n"
          "  xx  x\n"
          "x '' xx\n"
          "xx  xxx\n"
          "x ,, xx\n"
          "  xx  x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("Y", "xxxxxxx\n"
          "  xx  x\n"
          "  xx  x\n"
          "x    xx\n"
          "xx  xxx\n"
          "xx  xxx\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("Z", "xxxxxxx\n"
          "      x\n"
          "xxx  xx\n"
          "xx  xxx\n"
          "x  xxxx\n"
          "      x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("1", "xxxx\n"
          "'  x\n"
          ",  x\n"
          "x  x\n"
          "x  x\n"
          "x  x\n"
          "xxxx\n"
          "xxxx")

_add("2", "xxxxxxx\n"
          "'    'x\n"
          ",,xx  x\n"
          "x'   ,x\n"
          "' ,xxxx\n"
          "      x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("3", "xxxxxxx\n"
          "'    'x\n"
          ",,xx  x\n"
          "xx   ,x\n"
          "''xx  x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("4", "xxxxxxx\n"
          "  xxxxx\n"
          "  xxxxx\n"
          "  x  xx\n"
          "      x\n"
          "xxx  xx\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("5", "xxxxxxx\n"
          "      x\n"
          "  '''xx\n"
          ",,,,  x\n"
          "''xx  x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("6", "xxxxxxx\n"
          "'    'x\n"
          "  xx,,x\n"
          "     'x\n"
          "  xx  x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("7", "xxxxxxx\n"
          "      x\n"
          "xxxx  x\n"
          "xx'  xx\n"
          "xx  xxx\n"
          "xx  xxx\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("8", "xxxxxxx\n"
          "'    'x\n"
          "  xx  x\n"
          "'    'x\n"
          "  xx  x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("9", "xxxxxxx\n"
          "'    'x\n"
          "  xx  x\n"
          ",     x\n"
          "''xx  x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("0", "xxxxxxx\n"
          "'    'x\n"
          "  xx  x\n"
          "  xx  x\n"
          "  xx  x\n"
          ",    ,x\n"
          "xxxxxxx\n"
          "xxxxxxx")

_add("*", "xxxxxxx xxxxxxxx\n"
          "xxx,'xx,xx',xxxx\n"
          "xxxxx'   'xxxxxx\n"
          "xx,,x     x,,xxx\n"
          "xxxxx,   ,xxxxxx\n"
          "xxx',xx'xx,'xxxx\n"
          "xxxxxxx xxxxxxxx\n"
          "xxxxxxx xxxxxxxx")

# cloud
_add("@", "xxxxxxxxxxxxxxxx\n"
          "xxxx',,,,,'xxxxx\n"
          "x'' xxxxxxx xxxx\n"
          " xxx,xxxx'',,,'x\n"
          " 'xxxxxxxxxxxx x\n"
          "x,,,,,,,,,,,,,xx\n"
          "xxxxxxxxxxxxxxxx\n"
          "xxxxxxxxxxxxxxxx")

# cloud
_add(">", "----------------\n"
          "----,''''',-----\n"
          "-,,x-------x----\n"
          "x---'----,,''',-\n"
          "x,------------x-\n"
          "-'''''''''''''--\n"
          "----------------\n"
          "----------------")

# cloud sun rain
_add("<", "xxxxxxxxxxxxxxxx\n"
          "xxx',,,'xx xx'xx\n"
          "',,'xxxx ''x,xxx\n"
          " xxxxxx,xxx x,,x\n"
          "x,x'x,,,,,,x'xxx\n"
          "x',x,'xxxx xx,xx\n"
          "xx,,,xxxxxxxxxxx\n"
          "xx,,,xxxxxxxxxxx")

# light rain
_add("[", "xxxxxxxxxxxxxxxx\n"
          "xxxxx',,,'xxxxxx\n"
          "xx',,'xxxx ''xxx\n"
          "xx xxxx'x,xxx xx\n"
          "xxx,x',,'x,,,xxx\n"
          "xxxx xxx xxxxxxx\n"
          "xxxxx,,,xxxxxxxx\n"
          "xxxxx,,,xxxxxxxx")

# rain
_add("{", "xxxxx',,,'xxxxxx\n"
          "xx',,'xxxx ''xxx\n"
          "xx xxxxxx,xxx xx\n"
          "xxx,,,,,,,,,,xxx\n"
          "xxxx','xxxx'xxxx\n"
          "xxx,''',x',x,'xx\n"
          "xxxxxxxxx,''',xx\n"
          "xxxxxxxxx,''',xx")

# moon
_add("}", "xxxxxx'' ,,xxxxx\n"
          "xxxx'   ,xxxxxxx\n"
          "xxx'   xxxxxxxxx\n"
          "xxx    xxxxxxxxx\n"
          "xxx,   xxxxxxxxx\n"
          "xxxx,   'xxxxxxx\n"
          "xxxxxx,, ''xxxxx\n"
          "xxxxxx,, ''xxxxx")

# cloud sun
_add("~", "xxxxxxxxxxxxxxxx\n"
          "xxx',,,'xx xx'xx\n"
          "',,'xxxx ''x,xxx\n"
          " xxxxxx,xxx x,,x\n"
          "x,,,,,,,,,,x'xxx\n"
          "xxxxxxxxxx xx,xx\n"
          "xxxxxxxxxxxxxxxx\n"
          "xxxxxxxxxxxxxxxx")

# heavy rain
_add("]", "xxxx'',,,'xxxxxx\n"
          "',,,'xxxxx ''''x\n"
          " xxxxxxxx,xxxxxx\n"
          ",''''''''''xx'x,\n"
          "xx'xxxxx'xx',x,'\n"
          "',x,'x',x,'x,,,x\n"
          "x,,,xxx,,,xxxxxx\n"
          "x,,,xxx,,,xxxxxx")

# storm
_add("^", "xxxxx',,,'xxxxxx\n"
          "xx',,'xxxx ''xxx\n"
          "xx xxxxxx,xxx xx\n"
          "xxx,,x'   ,x,xxx\n"
          "xxxxx,  'xxxxxxx\n"
          "xxxxxxx,  xxxxxx\n"
          "xxxxxx' ,xxxxxxx\n"
          "xxxxxx' ,xxxxxxx")

# snow
_add("%", "xxxxx',,,'xxxxxx\n"
          "xx',,'xxxx ''xxx\n"
          "xx xxxxxx,xxx xx\n"
          "xxx,,,,,,,,,,xxx\n"
          "xxxxxxxx,',xxxxx\n"
          "xxx,',xx,x,xxxxx\n"
          "xxx,x,xxxxxxxxxx\n"
          "xxx,x,xxxxxxxxxx")

# unknown
_add("`", "\n".join(["".join([choice(["x", ",", "'"]) for i in range(16)])
                    for j in range(7)]))


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
