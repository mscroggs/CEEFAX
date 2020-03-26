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

_add("@", "',,,, x\n"
          " x  x x\n"
          " x    x\n"
          ",'''''x\n"
          ",'''''x")

_add("A", "xx''xxx\n"
          "x xx xx\n"
          "x ,, xx\n"
          "x,xx,xx\n"
          "x,xx,xx")

_add("B", "x'''xxx\n"
          "x '',xx\n"
          "x xx xx\n"
          "x,,,xxx\n"
          "x,,,xxx")

_add("C", "xx''xxx\n"
          "x xx,xx\n"
          "x xx'xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("D", "x'''xxx\n"
          "x xx xx\n"
          "x xx xx\n"
          "x,,,xxx\n"
          "x,,,xxx")

_add("E", "x''''xx\n"
          "x ''xxx\n"
          "x xxxxx\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("F", "x''''xx\n"
          "x ''xxx\n"
          "x xxxxx\n"
          "x,xxxxx\n"
          "x,xxxxx")

_add("G", "xx''xxx\n"
          "x xx,xx\n"
          "x x, xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("H", "x'xx'xx\n"
          "x '' xx\n"
          "x xx xx\n"
          "x,xx,xx\n"
          "x,xx,xx")

_add("I", "x''''xx\n"
          "xx  xxx\n"
          "xx  xxx\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("J", "xxxx'xx\n"
          "xxxx xx\n"
          "x'xx xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("K", "x'xx'xx\n"
          "x ',xxx\n"
          "x x,'xx\n"
          "x,xx,xx\n"
          "x,xx,xx")

_add("L", "x'xxxxx\n"
          "x xxxxx\n"
          "x xxxxx\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("M", "'xxxx'x\n"
          " ,'', x\n"
          " xxxx x\n"
          ",xxxx,x\n"
          ",xxxx,x")

_add("N", "x'xx'xx\n"
          "x ,' xx\n"
          "x xx xx\n"
          "x,xx,xx\n"
          "x,xx,xx")

_add("O", "xx''xxx\n"
          "x xx xx\n"
          "x xx xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("P", "x'''xxx\n"
          "x xx xx\n"
          "x ,,xxx\n"
          "x,xxxxx\n"
          "x,xxxxx")

_add("Q", "xx''xxx\n"
          "x xx xx\n"
          "x x' xx\n"
          "xx,,,xx\n"
          "xx,,,xx")

_add("R", "x'''xxx\n"
          "x xx xx\n"
          "x ,,'xx\n"
          "x,xx,xx\n"
          "x,xx,xx")

_add("S", "xx'''xx\n"
          "x,''xxx\n"
          "xxxx xx\n"
          "x,,,xxx\n"
          "x,,,xxx")

_add("T", "''''''x\n"
          "xx  xxx\n"
          "xx  xxx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("U", "x'xx'xx\n"
          "x xx xx\n"
          "x xx xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("V", "x'xxx'x\n"
          "x xxx x\n"
          "x x',xx\n"
          "xx,xxxx\n"
          "xx,xxxx")

_add("W", "'xxxx'x\n"
          " xxxx x\n"
          " ',,' x\n"
          ",xxxx,x\n"
          ",xxxx,x")

_add("X", "x'xx'xx\n"
          "x,'',xx\n"
          "x',,'xx\n"
          "x,xx,xx\n"
          "x,xx,xx")

_add("Y", "x'xx'xx\n"
          "x,'' xx\n"
          "xxx',xx\n"
          "xx,xxxx\n"
          "xx,xxxx")

_add("Z", "x''''xx\n"
          "xxx',xx\n"
          "x',xxxx\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("1", "xxx'xxx\n"
          "xx, xxx\n"
          "xxx xxx\n"
          "xxx,xxx\n"
          "xxx,xxx")

_add("2", "xx''xxx\n"
          "x,x',xx\n"
          "x',xxxx\n"
          "x,,,,xx\n"
          "x,,,,xx")

_add("3", "xx''xxx\n"
          "x,x',xx\n"
          "x'xx xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("4", "x'xxxxx\n"
          "x x'xxx\n"
          "x ' 'xx\n"
          "xxx,xxx\n"
          "xxx,xxx")

_add("5", "x''''xx\n"
          "x ''xxx\n"
          "x'xx xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("6", "xx''xxx\n"
          "x ''xxx\n"
          "x xx xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("7", "x''''xx\n"
          "xxxx xx\n"
          "xx',xxx\n"
          "xx,xxxx\n"
          "xx,xxxx")

_add("8", "xx''xxx\n"
          "x,'',xx\n"
          "x xx xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("9", "xx''xxx\n"
          "x xx xx\n"
          "xx,, xx\n"
          "xx,,xxx\n"
          "xx,,xxx")

_add("0", "xx''xxx\n"
          "x xx xx\n"
          "x xx xx\n"
          "xx,,xxx\n"
          "xx,,xxx")


def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError:
        return LetterBlock("xxxxxxx\n"
                           "x ,, xx\n"
                           "x '' xx\n"
                           "xxxxxxx\n"
                           "xxxxxxx")
