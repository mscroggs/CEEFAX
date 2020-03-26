#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fonts.LetterBlock import LetterBlock

SIZE = 4
alphabet = {}


def _add(letter, string):
    global alphabet
    assert len(letter.split("\n")) == SIZE
    alphabet[letter] = LetterBlock(letter)


_add("|", "x\n"
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

_add("A", "','x\n"
          " ' x\n"
          ",x,x\n"
          ",x,x")

_add("B", " ,'x\n"
          " , x\n"
          ",,xx\n"
          ",,xx")

_add("C", "',,x\n"
          " xxx\n"
          "x,,x\n"
          "x,,x")

_add("D", " ,'x\n"
          " x x\n"
          ",,xx\n"
          ",,xx")

_add("E", " ,,x\n"
          " ,xx\n"
          ",,,x\n"
          ",,,x")

_add("F", " ,,x\n"
          " ,xx\n"
          ",xxx\n"
          ",xxx")

_add("G", "',,x\n"
          " x x\n"
          "x,,x\n"
          "x,,x")

_add("H", " x x\n"
          " , x\n"
          ",x,x\n"
          ",x,x")

_add("I", " x\n"
          " x\n"
          ",x\n"
          ",x")

_add("J", "xx x\n"
          "'x x\n"
          "x,xx\n"
          "x,xx")

_add("K", " x x\n"
          " ,'x\n"
          ",x,x\n"
          ",x,x")

_add("L", " xxx\n"
          " xxx\n"
          ",,,x\n"
          ",,,x")

_add("M", " ' x\n"
          " x x\n"
          ",x,x\n"
          ",x,x")

_add("N", " ,'x\n"
          " x x\n"
          ",x,x\n"
          ",x,x")

_add("O", "','x\n"
          " x x\n"
          "x,xx\n"
          "x,xx")

_add("P", " ,'x\n"
          " ,xx\n"
          ",xxx\n"
          ",xxx")

_add("Q", "','x\n"
          " x x\n"
          "x,,x\n"
          "x,,x")

_add("R", " ,'x\n"
          " ,'x\n"
          ",x,x\n"
          ",x,x")

_add("S", " ,,x\n"
          ",, x\n"
          ",,,x\n"
          ",,,x")

_add("T", ", ,x\n"
          "x xx\n"
          "x,xx\n"
          "x,xx")

_add("U", " x x\n"
          " x x\n"
          ",,,x\n"
          ",,,x")

_add("V", " x x\n"
          " x x\n"
          ",,xx\n"
          ",,xx")

_add("W", " x x\n"
          " ' x\n"
          ",x,x\n"
          ",x,x")

_add("X", " x x\n"
          "','x\n"
          ",x,x\n"
          ",x,x")

_add("Y", " x x\n"
          ",, x\n"
          ",,xx\n"
          ",,xx")

_add("Z", ",, x\n"
          "',xx\n"
          ",,,x\n"
          ",,,x")

_add("1", "x'x\n"
          ", x\n"
          "x x\n"
          "x,x\n"
          "x,x")

_add("2", "x''xx\n"
          ",x',x\n"
          "',xxx\n"
          ",,,,x\n"
          ",,,,x")

_add("3", "x''xx\n"
          ",x',x\n"
          "'xx x\n"
          "x,,xx\n"
          "x,,xx")

_add("4", "'xxxx\n"
          " x'xx\n"
          " ' 'x\n"
          "xx,xx\n"
          "xx,xx")

_add("5", "''''x\n"
          " ''xx\n"
          "'xx x\n"
          "x,,xx\n"
          "x,,xx")

_add("6", "x''xx\n"
          " ''xx\n"
          " xx x\n"
          "x,,xx\n"
          "x,,xx")

_add("7", "''''x\n"
          "xxx x\n"
          "x',xx\n"
          "x,xxx\n"
          "x,xxx")

_add("8", "x''xx\n"
          ",'',x\n"
          " xx x\n"
          "x,,xx\n"
          "x,,xx")

_add("9", "x''xx\n"
          " xx x\n"
          "x,, x\n"
          "x,,xx\n"
          "x,,xx")

_add("0", "x''xx\n"
          " xx x\n"
          " xx x\n"
          "x,,xx\n"
          "x,,xx")


def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError:
        return LetterBlock("xxxxx\n"
                           " ,, x\n"
                           " '' x\n"
                           "xxxxx\n"
                           "xxxxx")
