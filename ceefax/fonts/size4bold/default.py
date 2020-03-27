#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ceefax.fonts.LetterBlock import LetterBlock

SIZE = 5
alphabet = {}


def _add(letter, string):
    global alphabet
    assert len(string.split("\n")) == SIZE
    alphabet[letter] = LetterBlock(string)


_add("|", "x\n"
          "x\n"
          "x\n"
          "x\n"
          "x")

_add("-", "xxx\n"
          "''x\n"
          "xxx\n"
          "xxx\n"
          "xxx")

_add(u"–", "xxx\n"
           "''x\n"
           "xxx\n"
           "xxx\n"
           "xxx")

_add("!", "'x\n"
          " x\n"
          ",x\n"
          ",x\n"
          ",x")

_add("#", "x'x'xx\n"
          ", , ,x\n"
          ", , ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("/", "xxxxx\n"
          "xx',x\n"
          "',xxx\n"
          "xxxxx\n"
          "xxxxx")

_add(":", "xx\n"
          "'x\n"
          "'x\n"
          "xx\n"
          "xx")

_add(".", "xx\n"
          "xx\n"
          "xx\n"
          ",x\n"
          ",x")
_add(",", "xx\n"
          "xx\n"
          "xx\n"
          " x\n"
          " x")

_add("?", "x''xx\n"
          ",xx x\n"
          "xx,xx\n"
          "xx,xx\n"
          "xx,xx")

_add("@", "',,,,, x\n"
          " x , x x\n"
          " x '   x\n"
          ",''''''x\n"
          ",''''''x")

_add(u"▲", "xxxxxx\n"
           "xx'xxx\n"
           "'   'x\n"
           "xxxxxx\n"
           "xxxxxx")

_add(u"▼", "xxxxxx\n"
           "'''''x\n"
           "x, ,xx\n"
           "xxxxxx\n"
           "xxxxxx")

_add("%", "'xxxx\n"
          "xx',x\n"
          "',xxx\n"
          "xxx,x\n"
          "xxx,x")

_add("'", "'x\n"
          ",x\n"
          "xx\n"
          "xx\n"
          "xx")

_add(u"’", "'x\n"
           ",x\n"
           "xx\n"
           "xx\n"
           "xx")

_add(u"∨", "xxxxx\n"
           "'xx'x\n"
           " '',x\n"
           "xxxxx\n"
           "xxxxx")

_add(u"∧", "xxxxx\n"
           "'''xx\n"
           " xx x\n"
           "xxxxx\n"
           "xxxxx")

_add(u"¬", "xxxxx\n"
           "''''x\n"
           "xxx x\n"
           "xxxxx\n"
           "xxxxx")

_add(u"⇾", "xxxxx\n"
           "xx'xx\n"
           ",, ,x\n"
           "xxxxx\n"
           "xxxxx")

_add(u"⇿", "xxxxxx\n"
           "x'x'xx\n"
           ", , ,x\n"
           "xxxxxx\n"
           "xxxxxx")

_add("(", "',x\n"
          " xx\n"
          " xx\n"
          ",'x\n"
          ",'x")

_add(u"°", "x'xx\n"
           ",',x\n"
           "xxxx\n"
           "xxxx\n"
           "xxxx")

_add(")", ",'x\n"
          "x x\n"
          "x x\n"
          "',x\n"
          "',x")

_add("&", "xxxx\n"
          "x'xx\n"
          ", ,x\n"
          "xxxx\n"
          "xxxx")

_add("=", "xxxxx\n"
          "''''x\n"
          "''''x\n"
          "xxxxx\n"
          "xxxxx")

_add("$", "x' 'x\n"
          ",''xx\n"
          "'xx x\n"
          "x, xx\n"
          "x, xx")

_add(u"£", "xx''x\n"
           "' 'xx\n"
           "x xxx\n"
           ",,,,x\n"
           ",,,,x")

_add(u"€", "xx''x\n"
           "' 'xx\n"
           "x xxx\n"
           "xx,,x\n"
           "xx,,x")

_add(u"฿", "xxxxxx' 'xx\n"
           "''''xx '',x\n"
           " x x x xx x\n"
           ",xxx,x, ,xx\n"
           ",xxx,x, ,xx")

_add(u"₺", "x'xxx\n"
           "x 'xx\n"
           ", x'x\n"
           "x,,xx\n"
           "x,,xx")

_add(u"¥", "'xx'x\n"
           ",'',x\n"
           "x' 'x\n"
           "xx,xx\n"
           "xx,xx")

_add(u"㎎", "xxxxxxxxxxx\n"
           " , ,'x',, x\n"
           " x x xx,, x\n"
           "xxxxxx,,,xx\n"
           "xxxxxx,,,xx")

_add(" ", "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx")

_add("A", "x''''xx\n"
          "  xx  x\n"
          "  ,,  x\n"
          ",,xx,,x\n"
          ",,xx,,x")

_add("B", "'''''xx\n"
          "  '',,x\n"
          "  xx  x\n"
          ",,,,,xx\n"
          ",,,,,xx")

_add("C", "x''''xx\n"
          "  xx,,x\n"
          "  xx''x\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("D", "'''''xx\n"
          "  xx  x\n"
          "  xx  x\n"
          ",,,,,xx\n"
          ",,,,,xx")

_add("E", "''''''x\n"
          "  '''xx\n"
          "  xxxxx\n"
          ",,,,,,x\n"
          ",,,,,,x")

_add("F", "''''''x\n"
          "  '''xx\n"
          "  xxxxx\n"
          ",,xxxxx\n"
          ",,xxxxx")

_add("G", "x''''xx\n"
          "  xx,,x\n"
          "  x,  x\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("H", "''xx''x\n"
          "  ''  x\n"
          "  xx  x\n"
          ",,xx,,x\n"
          ",,xx,,x")

_add("I", "''x\n"
          "  x\n"
          "  x\n"
          ",,x\n"
          ",,x")

_add("J", "xxxx''x\n"
          "xxxx  x\n"
          "''xx  x\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("K", "''xx''x\n"
          "  ' ,xx\n"
          "  x, 'x\n"
          ",,xx,,x\n"
          ",,xx,,x")

_add("L", "''xxxxx\n"
          "  xxxxx\n"
          "  xxxxx\n"
          ",,,,,,x\n"
          ",,,,,,x")

_add("M", "''xxx''x\n"
          "  ,',  x\n"
          "  xxx  x\n"
          ",,xxx,,x\n"
          ",,xxx,,x")

_add("N", "''xx''x\n"
          "  ,'  x\n"
          "  xx  x\n"
          ",,xx,,x\n"
          ",,xx,,x")

_add("O", "x''''xx\n"
          "  xx  x\n"
          "  xx  x\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("P", "'''''xx\n"
          "  xx  x\n"
          "  ,,,xx\n"
          ",,xxxxx\n"
          ",,xxxxx")

_add("Q", "x''''xx\n"
          "  xx  x\n"
          "  x'  x\n"
          "x,,,,,x\n"
          "x,,,,,x")

_add("R", "'''''xx\n"
          "  xx  x\n"
          "  ,, 'x\n"
          ",,xx,,x\n"
          ",,xx,,x")

_add("S", "x'''''x\n"
          ", '''xx\n"
          "xxxx  x\n"
          ",,,,,xx\n"
          ",,,,,xx")

_add("T", "''''''x\n"
          "xx  xxx\n"
          "xx  xxx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("U", "''xx''x\n"
          "  xx  x\n"
          "  xx  x\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("V", "''xx''x\n"
          "  xx  x\n"
          "  x' ,x\n"
          ",,,,xxx\n"
          ",,,,xxx")

_add("W", "''xxx''x\n"
          "  xxx  x\n"
          "  ','  x\n"
          ",,xxx,,x\n"
          ",,xxx,,x")

_add("X", "''xx''x\n"
          ", '' ,x\n"
          "' ,, 'x\n"
          ",,xx,,x\n"
          ",,xx,,x")

_add("Y", "''xx''x\n"
          ", '' ,x\n"
          "xx  xxx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("Z", "''''''x\n"
          "xx'',,x\n"
          "' ,xxxx\n"
          ",,,,,,x\n"
          ",,,,,,x")

_add("1", "x''x\n"
          ",  x\n"
          "x  x\n"
          "x,,x\n"
          "x,,x")

_add("2", "x''''xx\n"
          ",,x' ,x\n"
          "x' ,xxx\n"
          ",,,,,,x\n"
          ",,,,,,x")

_add("3", "x''''xx\n"
          ",,x' ,x\n"
          "''xx  x\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("4", "''xxxxx\n"
          "  x''xx\n"
          "  '  'x\n"
          "xxx,,xx\n"
          "xxx,,xx")

_add("5", "''''''x\n"
          "  '''xx\n"
          "''xx  x\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("6", "x''''xx\n"
          "  '''xx\n"
          "  xx  x\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("7", "''''''x\n"
          "xxxx  x\n"
          "xx' ,xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("8", "x''''xx\n"
          ", '' ,x\n"
          "  xx  x\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("9", "x''''xx\n"
          "  xx  x\n"
          "x,,,  x\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("0", "x''''xx\n"
          "  xx  x\n"
          "  xx  x\n"
          "x,,,,xx\n"
          "x,,,,xx")


def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError:
        return LetterBlock("xxxxx\n"
                           " ,, x\n"
                           " '' x\n"
                           "xxxxx\n"
                           "xxxxx")
