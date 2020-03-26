from fonts.LetterBlock import LetterBlock

SIZE = 7
alphabet = {}


def _add(letter, string):
    global alphabet
    letter_str = string.strip()
    assert len(letter_str.split("\n")) == SIZE
    alphabet[letter] = LetterBlock(letter_str)


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

_add("&", "xxxx\n"
          "xxxx\n"
          "x xx\n"
          "   x\n"
          "x xx\n"
          "xxxx\n"
          "xxxx\n"
          "xxxx")

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

_add("!", "xxx\n"
          "  x\n"
          "  x\n"
          "  x\n"
          "xxx\n"
          "  x\n"
          "xxx\n"
          "xxx")

_add("?", "xxxxxx\n"
          "'   'x\n"
          ",,x  x\n"
          "xx  ,x\n"
          "xx,,xx\n"
          "xx  xx\n"
          "xxxxxx\n"
          "xxxxxx")

_add("/", "xxxxxx\n"
          "xxxx x\n"
          "xxx xx\n"
          "xx xxx\n"
          "x xxxx\n"
          " xxxxx\n"
          "xxxxxx\n"
          "xxxxxx")

_add(" ", "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx\n"
          "xx")

_add("A", "xxxxxx\n"
          "'   'x\n"
          "  x  x\n"
          "     x\n"
          "  x  x\n"
          "  x  x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("B", "xxxxxx\n"
          "    'x\n"
          "  x  x\n"
          "    'x\n"
          "  x  x\n"
          "    ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("C", "xxxxx\n"
          "'   x\n"
          "  xxx\n"
          "  xxx\n"
          "  xxx\n"
          ",   x\n"
          "xxxxx\n"
          "xxxxx")

_add("D", "xxxxxx\n"
          "    'x\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          "    ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("E", "xxxxx\n"
          "    x\n"
          "  xxx\n"
          "   xx\n"
          "  xxx\n"
          "    x\n"
          "xxxxx\n"
          "xxxxx")

_add("F", "xxxxx\n"
          "    x\n"
          "  xxx\n"
          "   xx\n"
          "  xxx\n"
          "  xxx\n"
          "xxxxx\n"
          "xxxxx")

_add("G", "xxxxxx\n"
          "'   'x\n"
          "  xxxx\n"
          "  x''x\n"
          "  x  x\n"
          ",    x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("H", "xxxxxx\n"
          "  x  x\n"
          "  x  x\n"
          "     x\n"
          "  x  x\n"
          "  x  x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("I", "xxx\n"
          "  x\n"
          "  x\n"
          "  x\n"
          "  x\n"
          "  x\n"
          "xxx\n"
          "xxx")

_add("J", "xxxxx\n"
          "xx  x\n"
          "xx  x\n"
          "xx  x\n"
          "xx  x\n"
          "   ,x\n"
          "xxxxx\n"
          "xxxxx")

_add("K", "xxxxxx\n"
          "  x  x\n"
          "  x ,x\n"
          "   'xx\n"
          "  x  x\n"
          "  x  x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("L", "xxxxx\n"
          "  xxx\n"
          "  xxx\n"
          "  xxx\n"
          "  xxx\n"
          "    x\n"
          "xxxxx\n"
          "xxxxx")

_add("M", "xxxxxx\n"
          " 'x' x\n"
          "     x\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("N", "xxxxxx\n"
          "    'x\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("O", "xxxxxx\n"
          "'   'x\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          ",   ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("P", "xxxxxx\n"
          "    'x\n"
          "  x  x\n"
          "    ,x\n"
          "  xxxx\n"
          "  xxxx\n"
          "xxxxxx\n"
          "xxxxxx")

_add("Q", "xxxxxx\n"
          "'   'x\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          ",    x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("R", "xxxxxx\n"
          "    'x\n"
          "  x  x\n"
          "    ,x\n"
          "  x  x\n"
          "  x  x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("S", "xxxxx\n"
          "'   x\n"
          "  xxx\n"
          ",  'x\n"
          "xx  x\n"
          "   ,x\n"
          "xxxxx\n"
          "xxxxx")

_add("T", "xxxxx\n"
          "    x\n"
          "x  xx\n"
          "x  xx\n"
          "x  xx\n"
          "x  xx\n"
          "xxxxx\n"
          "xxxxx")

_add("U", "xxxxxx\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          ",   ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("V", "xxxxxx\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          "   ,xx\n"
          "xxxxxx\n"
          "xxxxxx")

_add("W", "xxxxxx\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          "     x\n"
          " ,x, x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("X", "xxxxxx\n"
          "  x  x\n"
          "  x  x\n"
          "x   xx\n"
          "  x  x\n"
          "  x  x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("Y", "xxxxxx\n"
          "  x  x\n"
          "  x  x\n"
          ",    x\n"
          "xxx  x\n"
          "x   ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("Z", "xxxxx\n"
          "    x\n"
          "xx' x\n"
          "x   x\n"
          " ,xxx\n"
          "    x\n"
          "xxxxx\n"
          "xxxxx")

_add("1", "xxx\n"
          "' x\n"
          "  x\n"
          "  x\n"
          "  x\n"
          "  x\n"
          "xxx\n"
          "xxx")

_add("2", "xxxxxx\n"
          "'   'x\n"
          ",,x  x\n"
          "x'  ,x\n"
          "  ,xxx\n"
          "     x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("3", "xxxxxx\n"
          "'   'x\n"
          ",,x  x\n"
          "xx  'x\n"
          "''x  x\n"
          ",   ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("4", "xxxxxx\n"
          "  x  x\n"
          "  x  x\n"
          "     x\n"
          "xxx  x\n"
          "xxx  x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("5", "xxxxxx\n"
          "     x\n"
          "  xxxx\n"
          "    'x\n"
          "xxx  x\n"
          "    xx\n"
          "xxxxxx\n"
          "xxxxxx")

_add("6", "xxxxxx\n"
          "'   'x\n"
          "  x,,x\n"
          "    'x\n"
          "  x  x\n"
          ",   ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("7", "xxxxxx\n"
          "     x\n"
          "xxx  x\n"
          "xxx  x\n"
          "xxx  x\n"
          "xxx  x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("8", "xxxxxx\n"
          "'   'x\n"
          "  x  x\n"
          "x   xx\n"
          "  x  x\n"
          ",   ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("9", "xxxxxx\n"
          "'   'x\n"
          "  x  x\n"
          ",    x\n"
          "''x  x\n"
          ",   ,x\n"
          "xxxxxx\n"
          "xxxxxx")

_add("0", "xxxxxx\n"
          "'   'x\n"
          "  x  x\n"
          "  x  x\n"
          "  x  x\n"
          ",   ,x\n"
          "xxxxxx\n"
          "xxxxxx")

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

#  storm
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
