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
          "x\n"
          "x")

_add("@", "',,, x\n"
          " x x x\n"
          " x   x\n"
          ",''''x\n"
          ",''''x")

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

_add("–", "xxx\n"
          "''x\n"
          "xxx\n"
          "xxx\n"
          "xxx")

_add("_", "xxx\n"
          "xxx\n"
          "xxx\n"
          ",,x\n"
          ",,x")

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

_add("#", "x'x'xx\n"
          ", , ,x\n"
          ", , ,x\n"
          "xxxxxx\n"
          "xxxxxx")

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

_add(u"‘", "'x\n"
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

_add(u"฿", "' 'xx\n"
           " '',x\n"
           " xx x\n"
           ", ,xx\n"
           ", ,xx")

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

_add(u"₫", "xxx'x\n"
           "x , x\n"
           "x,,,x\n"
           "x,,,x\n"
           "x,,,x")

_add(u"₽", "x'''x\n"
           "x ' x\n"
           "' 'xx\n"
           "x,xxx\n"
           "x,xxx")

_add(u"㎎", "xxxxxxxxxxx\n"
           " , ,'x',, x\n"
           " x x xx,, x\n"
           "xxxxxx,,,xx\n"
           "xxxxxx,,,xx")

_add(u"㏂", "xxxxxxxxxx\n"
           "x,'x , ,'x\n"
           "', x x x x\n"
           "x,,x,x,x,x\n"
           "x,,x,x,x,x")

_add(u"㏘", "xxxxxxxxxx\n"
           " ,'x , ,'x\n"
           " ',x x x x\n"
           ",xxx,x,x,x\n"
           ",xxx,x,x,x")

_add(" ", "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx\n"
          "xxx")

_add("A", "x''xx\n"
          " xx x\n"
          " ,, x\n"
          ",xx,x\n"
          ",xx,x")

_add("B", "'''xx\n"
          " '',x\n"
          " xx x\n"
          ",,,xx\n"
          ",,,xx")

_add("C", "x''xx\n"
          " xx,x\n"
          " xx'x\n"
          "x,,xx\n"
          "x,,xx")

_add("D", "'''xx\n"
          " xx x\n"
          " xx x\n"
          ",,,xx\n"
          ",,,xx")

_add("E", "''''x\n"
          " ''xx\n"
          " xxxx\n"
          ",,,,x\n"
          ",,,,x")

_add("F", "''''x\n"
          " ''xx\n"
          " xxxx\n"
          ",xxxx\n"
          ",xxxx")

_add("G", "x''xx\n"
          " xx,x\n"
          " x, x\n"
          "x,,xx\n"
          "x,,xx")

_add("H", "'xx'x\n"
          " '' x\n"
          " xx x\n"
          ",xx,x\n"
          ",xx,x")

_add("I", "'x\n"
          " x\n"
          " x\n"
          ",x\n"
          ",x")

_add("J", "xxx'x\n"
          "xxx x\n"
          "'xx x\n"
          "x,,xx\n"
          "x,,xx")

_add("K", "'xx'x\n"
          " ',xx\n"
          " x,'x\n"
          ",xx,x\n"
          ",xx,x")

_add("L", "'xxxx\n"
          " xxxx\n"
          " xxxx\n"
          ",,,,x\n"
          ",,,,x")

_add("M", "'xxx'x\n"
          " ,', x\n"
          " xxx x\n"
          ",xxx,x\n"
          ",xxx,x")

_add("N", "'xx'x\n"
          " ,' x\n"
          " xx x\n"
          ",xx,x\n"
          ",xx,x")

_add("O", "x''xx\n"
          " xx x\n"
          " xx x\n"
          "x,,xx\n"
          "x,,xx")

_add("P", "'''xx\n"
          " xx x\n"
          " ,,xx\n"
          ",xxxx\n"
          ",xxxx")

_add("Q", "x''xx\n"
          " xx x\n"
          " xx x\n"
          "x,,'x\n"
          "x,,'x")

_add("R", "'''xx\n"
          " xx x\n"
          " ,,'x\n"
          ",xx,x\n"
          ",xx,x")

_add("S", "x'''x\n"
          ",''xx\n"
          "xxx x\n"
          ",,,xx\n"
          ",,,xx")

_add("T", "'''x\n"
          "x xx\n"
          "x xx\n"
          "x,xx\n"
          "x,xx")

_add("U", "'xx'x\n"
          " xx x\n"
          " xx x\n"
          "x,,xx\n"
          "x,,xx")

_add("V", "'xx'x\n"
          " xx x\n"
          " x',x\n"
          ",,xxx\n"
          ",,xxx")

_add("W", "'xxx'x\n"
          " xxx x\n"
          " ',' x\n"
          ",xxx,x\n"
          ",xxx,x")

_add("X", "'xx'x\n"
          ",'',x\n"
          "',,'x\n"
          ",xx,x\n"
          ",xx,x")

_add("Y", "'xx'x\n"
          ",'' x\n"
          "xx',x\n"
          "x,xxx\n"
          "x,xxx")

_add("Z", "''''x\n"
          "xx',x\n"
          "',xxx\n"
          ",,,,x\n"
          ",,,,x")

_add("a", "xxxx\n"
          ",,'x\n"
          "', x\n"
          ",,,x\n"
          ",,,x")

_add("b", "'xxx\n"
          " ,'x\n"
          " x x\n"
          ",,xx\n"
          ",,xx")

_add("c", "xxxx\n"
          "',,x\n"
          " xxx\n"
          "x,,x\n"
          "x,,x")

_add("d", "xx'x\n"
          "', x\n"
          " x x\n"
          "x,,x\n"
          "x,,x")

_add("e", "xxxx\n"
          "','x\n"
          " ,,x\n"
          "x,,x\n"
          "x,,x")

_add("f", "x'x\n"
          " 'x\n"
          " xx\n"
          ",xx\n"
          ",xx")

_add("g", "xxxx\n"
          "', x\n"
          ",' x\n"
          "'',x\n"
          "'',x")

_add("h", "'xxx\n"
          " ,'x\n"
          " x x\n"
          ",x,x\n"
          ",x,x")

_add("i", "'x\n"
          "'x\n"
          " x\n"
          ",x\n"
          ",x")

_add("j", "x'x\n"
          "x'x\n"
          "x x\n"
          "',x\n"
          "',x")

_add("k", "'xxx\n"
          " x x\n"
          " ,'x\n"
          ",x,x\n"
          ",x,x")

_add("l", "'x\n"
          " x\n"
          " x\n"
          ",x\n"
          ",x")

_add("m", "xxxxxx\n"
          " ,','x\n"
          " x x x\n"
          ",xxx,x\n"
          ",xxx,x")

_add("n", "xxxx\n"
          " ,'x\n"
          " x x\n"
          ",x,x\n"
          ",x,x")

_add("o", "xxxx\n"
          "','x\n"
          " x x\n"
          "x,xx\n"
          "x,xx")

_add("p", "xxxx\n"
          " ,'x\n"
          " ',x\n"
          " xxx\n"
          " xxx")

_add("q", "xxxx\n"
          "', x\n"
          ",' x\n"
          "xx x\n"
          "xx x")

_add("r", "xxxx\n"
          " ',x\n"
          " xxx\n"
          ",xxx\n"
          ",xxx")

_add("s", "xxxx\n"
          "',,x\n"
          "x,'x\n"
          ",,xx\n"
          ",,xx")

_add("t", "'xx\n"
          " ,x\n"
          " xx\n"
          "x,x\n"
          "x,x")

_add("u", "xxxx\n"
          " x x\n"
          " x x\n"
          "x,,x\n"
          "x,,x")

_add("v", "xxxx\n"
          " x x\n"
          " x x\n"
          ",,xx\n"
          ",,xx")

_add("w", "xxxxxx\n"
          " x x x\n"
          " x x x\n"
          ",,,,xx\n"
          ",,,,xx")

_add("x", "xxxx\n"
          ",',x\n"
          "x xx\n"
          ",x,x\n"
          ",x,x")

_add("y", "xxxx\n"
          " x x\n"
          ",' x\n"
          "'',x\n"
          "'',x")

_add("z", "xxxx\n"
          ",, x\n"
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

_add(u"Đ", "x'''xx\n"
           "' 'x x\n"
           "x xx x\n"
           "x,,,xx\n"
           "x,,,xx")

_add(u"Š", "x,',\n"
           "',,x\n"
           "x,'x\n"
           ",,xx\n"
           ",,xx")


_add(u"Ü", "'xx'x\n"
           "'xx'x\n"
           " xx x\n"
           "x,,xx\n"
           "x,,xx")

_add(u"á", "',xx\n"
           "x,'x\n"
           "', x\n"
           ",,,x\n"
           ",,,x")

_add(u"ả", "',xx\n"
           "x,'x\n"
           "', x\n"
           ",,,x\n"
           ",,,x")

_add(u"ã", ",,,x\n"
           ",,'x\n"
           "', x\n"
           ",,,x\n"
           ",,,x")

_add("ç", "xxxx\n"
          "',,x\n"
          " xxx\n"
          "x ,x\n"
          "x ,x")

_add(u"é", "',xx\n"
           "','x\n"
           " ,,x\n"
           "x,,x\n"
           "x,,x")

_add(u"ğ", ",',x\n"
           "', x\n"
           "x, x\n"
           ",,xx\n"
           ",,xx")

_add(u"í", "',x\n"
           "'xx\n"
           " xx\n"
           ",xx\n"
           ",xx")

_add(u"ł", "x'xx\n"
           "' ,x\n"
           "x xx\n"
           "x,xx\n"
           "x,xx")

_add(u"ñ", "'''x\n"
           "''xx\n"
           " x x\n"
           ",x,x\n"
           ",x,x")

_add(u"ø", "xxxx'x\n"
           "x','xx\n"
           "x x xx\n"
           ",x,xxx\n"
           ",x,xxx")

_add(u"ó", "',xx\n"
           "x'xx\n"
           " x x\n"
           "x,xx\n"
           "x,xx")

_add(u"ô", "'.'x\n"
           "x'xx\n"
           " x x\n"
           "x,xx\n"
           "x,xx")

_add(u"ö", "'x'x\n"
           "x'xx\n"
           " x x\n"
           "x,xx\n"
           "x,xx")

_add("ō", ",,,x\n"
          "','x\n"
          " x x\n"
          "x,xx\n"
          "x,xx")

_add(u"ộ", "'.'x\n"
           "x'xx\n"
           ",',x\n"
           "x'xx\n"
           "x'xx")

_add(u"ú", "x',x\n"
           "'x'x\n"
           " x x\n"
           "x,,x\n"
           "x,,x")

_add(u"ü", "'x'x\n"
           "'x'x\n"
           " x x\n"
           "x,,x\n"
           "x,,x")

_add(u"ý", "x',x\n"
           "'x'x\n"
           ",, x\n"
           ",,xx\n"
           ",,xx")

# Cyrillic ===========================================

_add(u"А", "x''xx\n"
           " xx x\n"
           " ,, x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Б", "''''x\n"
           " ''xx\n"
           " xx x\n"
           ",,,xx\n"
           ",,,xx")

_add(u"В", "'''xx\n"
           " '',x\n"
           " xx x\n"
           ",,,xx\n"
           ",,,xx")

_add(u"Г", "''''x\n"
           " xxxx\n"
           " xxxx\n"
           ",xxxx\n"
           ",xxxx")

_add(u"Д", "x'''x\n"
           " xx x\n"
           " '' x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Е", "''''x\n"
           " ''xx\n"
           " xxxx\n"
           ",,,,x\n"
           ",,,,x")

_add(u"Ё", "x,x,x\n"
           " ,,,x\n"
           " ,,xx\n"
           ",,,,x\n"
           ",,,,x")

_add(u"Ж", "'xx'xx'x\n"
           "x,' ',xx\n"
           "',x x,'x\n"
           ",xx,xx,x\n"
           ",xx,xx,x")

_add(u"З", "x''xx\n"
           ",x',x\n"
           "'xx x\n"
           "x,,xx\n"
           "x,,xx")

_add(u"И", "'xx'x\n"
           " ', x\n"
           " xx x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Й", "x,,xx\n"
           " x' x\n"
           " ,x x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"К", "'xx'x\n"
           " ',xx\n"
           " x,'x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Л", "x'''x\n"
           "x x x\n"
           "x x x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"М", "'xxx'x\n"
           " ,', x\n"
           " xxx x\n"
           ",xxx,x\n"
           ",xxx,x")

_add(u"Н", "'xx'x\n"
           " '' x\n"
           " xx x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"О", "x''xx\n"
           " xx x\n"
           " xx x\n"
           "x,,xx\n"
           "x,,xx")

_add(u"П", "''''x\n"
           " xx x\n"
           " xx x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Р", "'''xx\n"
           " xx x\n"
           " ,,xx\n"
           ",xxxx\n"
           ",xxxx")

_add(u"С", "x''xx\n"
           " xx,x\n"
           " xx'x\n"
           "x,,xx\n"
           "x,,xx")

_add(u"Т", "'''x\n"
           "x xx\n"
           "x xx\n"
           "x,xx\n"
           "x,xx")

_add(u"У", "'xx'x\n"
           ",'' x\n"
           "xx',x\n"
           "x,xxx\n"
           "x,xxx")

_add(u"Ф", "xx'xxx\n"
           "',,,'x\n"
           ",''',x\n"
           "xx,xxx\n"
           "xx,xxx")

_add(u"Х", "'xx'x\n"
           ",'',x\n"
           "',,'x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Ц", "'xx'x\n"
           " xx x\n"
           " xx x\n"
           ",,, x\n"
           ",,, x")

_add(u"Ч", "'xx'x\n"
           ",'' x\n"
           "xxx x\n"
           "xxx,x\n"
           "xxx,x")

_add(u"Ш", "'x'x'x\n"
           " x x x\n"
           " x x x\n"
           ",,,,,x\n"
           ",,,,,x")

_add(u"Щ", "'x'x'x\n"
           " x x x\n"
           " x x x\n"
           ",,,, x\n"
           ",,,, x")

_add(u"Ъ", "''xxxx\n"
           "x ''xx\n"
           "x xx x\n"
           "x,,,xx\n"
           "x,,,xx")

_add(u"Ы", "'xxxx'x\n"
           " ''xx x\n"
           " xx x x\n"
           ",,,xx,x\n"
           ",,,xx,x")

_add(u"Ь", "'xxxx\n"
           " ''xx\n"
           " xx x\n"
           ",,,xx\n"
           ",,,xx")

_add(u"Э", "x''xx\n"
           ",x' x\n"
           "'xx x\n"
           "x,,xx\n"
           "x,,xx")

_add(u"Ю", " xx''xx\n"
           " ' xx x\n"
           " x xx x\n"
           " xx,,xx\n"
           " xx,,xx")

_add(u"Я", "x'''x\n"
           " xx x\n"
           "',, x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"а", "xxxx\n"
           ",,'x\n"
           "', x\n"
           ",,,x\n"
           ",,,x")

_add(u"б", "x'xx\n"
           " ,'x\n"
           " x x\n"
           ",,xx\n"
           ",,xx")

_add(u"в", "xxxx\n"
           " ,'x\n"
           " ,'x\n"
           ",,xx\n"
           ",,xx")

_add(u"г", "xxxx\n"
           " ,,x\n"
           " xxx\n"
           ",xxx\n"
           ",xxx")

_add(u"д", "xxxx\n"
           "', x\n"
           " ' x\n"
           ",x,x\n"
           ",x,x")

_add(u"е", "xxxx\n"
           "','x\n"
           " ,,x\n"
           "x,,x\n"
           "x,,x")

_add(u"ё", ",x,x\n"
           "','x\n"
           " ,,x\n"
           "x,,x\n"
           "x,,x")

_add(u"ж", "xxxxxx\n"
           " x x x\n"
           "', ,'x\n"
           ",x,x,x\n"
           ",x,x,x")

_add(u"з", "xxxx\n"
           ",,'x\n"
           ",,'x\n"
           ",,xx\n"
           ",,xx")

_add(u"и", "xxxxx\n"
           " x' x\n"
           " ,x x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"й", ",,,,x\n"
           " x' x\n"
           " ,x x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"к", "xxxx\n"
           " x x\n"
           " ,'x\n"
           ",x,x\n"
           ",x,x")

_add(u"л", "xxxx\n"
           "', x\n"
           " x x\n"
           ",x,x\n"
           ",x,x")

_add(u"м", "xxxxxx\n"
           " 'x' x\n"
           " x x x\n"
           ",xxx,x\n"
           ",xxx,x")

_add(u"н", "xxxx\n"
           " x x\n"
           " , x\n"
           ",x,x\n"
           ",x,x")

_add(u"о", "xxxx\n"
           "','x\n"
           " x x\n"
           "x,xx\n"
           "x,xx")

_add(u"п", "xxxx\n"
           " , x\n"
           " x x\n"
           ",x,x\n"
           ",x,x")

_add(u"р", "xxxx\n"
           " ,'x\n"
           " ',x\n"
           ",xxx\n"
           ",xxx")

_add(u"с", "xxxx\n"
           "',,x\n"
           " xxx\n"
           "x,,x\n"
           "x,,x")

_add(u"т", "xxxx\n"
           ", ,x\n"
           "x xx\n"
           "x,xx\n"
           "x,xx")

_add(u"у", "xxxx\n"
           " x x\n"
           "x, x\n"
           ",,xx\n"
           ",,xx")

_add(u"ф", "xx'xxx\n"
           "x' 'xx\n"
           ",''',x\n"
           "xx,xxx\n"
           "xx,xxx")

_add(u"х", "xxxx\n"
           ",',x\n"
           "x xx\n"
           ",x,x\n"
           ",x,x")

_add(u"ц", "xxxx\n"
           " x x\n"
           " x x\n"
           ",, x\n"
           ",, x")

_add(u"ч", "xxxx\n"
           " x x\n"
           "x, x\n"
           "xx,x\n"
           "xx,x")

_add(u"ш", "xxxxxx\n"
           " x x x\n"
           " x x x\n"
           ",,,,,x\n"
           ",,,,,x")

_add(u"щ", "xxxxxx\n"
           " x x x\n"
           " x x x\n"
           ",,,, x\n"
           ",,,, x")

_add(u"ъ", "xxxx\n"
           ", 'xx\n"
           "x x x\n"
           "x,,xx\n"
           "x,,xx")

_add(u"ы", "xxxxxx\n"
           " 'xx x\n"
           " x x x\n"
           ",,xx,x\n"
           ",,xx,x")

_add(u"ь", "xxxx\n"
           " 'xx\n"
           " x x\n"
           ",,xx\n"
           ",,xx")

_add(u"э", "xxxx\n"
           ",,'x\n"
           "x, x\n"
           ",,xx\n"
           ",,xx")

_add(u"ю", "xxxxxx\n"
           " '','x\n"
           " x x x\n"
           "xxx,xx\n"
           "xxx,xx")

_add(u"я", "xxxxx\n"
           "',, x\n"
           "',, x\n"
           ",xx,x\n"
           ",xx,x")

# Greek ===========================================

_add(u"Α", "x''xx\n"
           " xx x\n"
           " ,, x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Β", "'''xx\n"
           " '',x\n"
           " xx x\n"
           ",,,xx\n"
           ",,,xx")

_add(u"Γ", "''''x\n"
           " xxxx\n"
           " xxxx\n"
           ",xxxx\n"
           ",xxxx")

_add(u"Δ", "x''xx\n"
           " xx x\n"
           " xx x\n"
           ",,,,x\n"
           ",,,,x")

_add(u"Ε", "''''x\n"
           " ''xx\n"
           " xxxx\n"
           ",,,,x\n"
           ",,,,x")

_add(u"Ζ", "''''x\n"
           "xx',x\n"
           "',xxx\n"
           ",,,,x\n"
           ",,,,x")

_add(u"Η", "'xx'x\n"
           " '' x\n"
           " xx x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Θ", "x''xx\n"
           " '' x\n"
           " xx x\n"
           "x,,xx\n"
           "x,,xx")

_add(u"Ι", "'x\n"
           " x\n"
           " x\n"
           ",x\n"
           ",x")

_add(u"Κ", "'xx'x\n"
           " ',xx\n"
           " x,'x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Λ", "x'''x\n"
           " xx x\n"
           " xx x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Μ", "'xxx'x\n"
           " ,', x\n"
           " xxx x\n"
           ",xxx,x\n"
           ",xxx,x")

_add(u"Ν", "'xx'x\n"
           " ,' x\n"
           " xx x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Ξ", "''''x\n"
           "''''x\n"
           "xxxxx\n"
           ",,,,x\n"
           ",,,,x")

_add(u"Ο", "x''xx\n"
           " xx x\n"
           " xx x\n"
           "x,,xx\n"
           "x,,xx")

_add(u"Π", "''''x\n"
           " xx x\n"
           " xx x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Ρ", "'''xx\n"
           " xx x\n"
           " ,,xx\n"
           ",xxxx\n"
           ",xxxx")

_add(u"Σ", "''''x\n"
           ",'xxx\n"
           "',xxx\n"
           ",,,,x\n"
           ",,,,x")

_add(u"Τ", "'''x\n"
           "x xx\n"
           "x xx\n"
           "x,xx\n"
           "x,xx")

_add(u"Υ", "'xx'x\n"
           ",'' x\n"
           "xx xx\n"
           "xx,xx\n"
           "xx,xx")

_add(u"Φ", "xx'xxx\n"
           "', ,'x\n"
           ",' ',x\n"
           "xx,xxx\n"
           "xx,xxx")

_add(u"Χ", "'xx'x\n"
           ",'',x\n"
           "',,'x\n"
           ",xx,x\n"
           ",xx,x")

_add(u"Ψ", "'x'x'x\n"
           " x x x\n"
           ",' ',x\n"
           "xx,xxx\n"
           "xx,xxx")

_add(u"Ω", "x'''xx\n"
           " xxx x\n"
           ",'x',x\n"
           ",,x,,x\n"
           ",,x,,x")

_add(u"α", "xxxx\n"
           "', x\n"
           " x x\n"
           "x,,x\n"
           "x,,x")

_add(u"β", "x'xx\n"
           " ',x\n"
           " ',x\n"
           ",xxx\n"
           ",xxx")

_add(u"γ", "xxxx\n"
           " x x\n"
           ",',x\n"
           "x,xx\n"
           "x,xx")

_add(u"δ", "x'xx\n"
           ",'xx\n"
           " x x\n"
           "x,xx\n"
           "x,xx")

_add(u"ε", "xxxx\n"
           "',,x\n"
           " ,,x\n"
           "x,,x\n"
           "x,,x")

_add(u"ζ", "'''x\n"
           "x',x\n"
           " xxx\n"
           "x,,x\n"
           "x,,x")

_add(u"η", "xxxx\n"
           " ,'x\n"
           " x x\n"
           "xx,x\n"
           "xx,x")

_add(u"θ", "x'xx\n"
           " ' x\n"
           " x x\n"
           "x,xx\n"
           "x,xx")

_add(u"ι", "xx\n"
           " x\n"
           " x\n"
           ",x\n"
           ",x")

_add(u"κ", "xxxx\n"
           " x x\n"
           " ,'x\n"
           ",x,x\n"
           ",x,x")

_add(u"λ", "''xx\n"
           "x' x\n"
           " x x\n"
           ",x,x\n"
           ",x,x")

_add(u"μ", "xxxx\n"
           " x x\n"
           " x x\n"
           ",,xx\n"
           ",,xx")

_add(u"ν", "xxxx\n"
           ",,'x\n"
           "', x\n"
           ",,,x\n"
           ",,,x")

_add(u"ξ", "'''x\n"
           ",''x\n"
           ",''x\n"
           "xx,x\n"
           "xx,x")

_add(u"ο", "xxxx\n"
           "','x\n"
           " x x\n"
           "x,xx\n"
           "x,xx")

_add(u"π", "xxxx\n"
           " , x\n"
           " x x\n"
           ",x,x\n"
           ",x,x")

_add(u"ρ", "xxxx\n"
           "','x\n"
           " ',x\n"
           ",xxx\n"
           ",xxx")

_add(u"σ", "xxxxx\n"
           "', ,x\n"
           " x xx\n"
           "x,xxx\n"
           "x,xxx")

_add(u"ς", "xxxx\n"
           "',,x\n"
           "x,'x\n"
           ",,xx\n"
           ",,xx")

_add(u"τ", "xxxx\n"
           ", ,x\n"
           "x xx\n"
           "xx,x\n"
           "xx,x")

_add(u"υ", "xxxx\n"
           " x x\n"
           " x x\n"
           "x,xx\n"
           "x,xx")

_add(u"φ", "xx'xxx\n"
           "x' 'xx\n"
           ",' ',x\n"
           "xx,xxx\n"
           "xx,xxx")

_add(u"χ", "xxxx\n"
           " x x\n"
           "','x\n"
           ",x,x\n"
           ",x,x")

_add(u"ψ", "xxxxxx\n"
           " x x x\n"
           ",' ',x\n"
           "xx,xxx\n"
           "xx,xxx")

_add(u"ω", "xxxxxx\n"
           "',x,'x\n"
           " x x x\n"
           "x,,,xx\n"
           "x,,,xx")

# ===========================================


def get_letter(char):
    try:
        return alphabet[char]
    except KeyError:
        return LetterBlock("xxxxx\n"
                           " ,, x\n"
                           " '' x\n"
                           "xxxxx\n"
                           "xxxxx")
