from fonts.LetterBlock import LetterBlock
from fonts.exceptions import LetterNotDefined

SIZE = 4
alphabet = {}


def _add(letter, string):
    global alphabet
    letter_str = string.strip()
    assert len(letter_str.split("\n")) == SIZE
    alphabet[letter] = LetterBlock(letter_str)

_add("|", """
x
x
x
x
""")

_add("-", """
xxx
''x
xxx
xxx
""")

_add("!", """
'x
 x
,x
,x
""")

_add("/", """
xxxxx
xx',x
',xxx
xxxxx
""")

_add(":", """
xx
'x
'x
xx
""")

_add(" ","""
xxx
xxx
xxx
xxx
""")

_add("A", """
x''xx
 xx x
 ,, x
,xx,x
""")

_add("B", """
'''xx
 '',x
 xx x
,,,xx
""")

_add("C", """
x''xx
 xx,x
 xx'x
x,,xx
""")

_add("D", """
'''xx
 xx x
 xx x
,,,xx
""")

_add("E", """
''''x
 ''xx
 xxxx
,,,,x
""")

_add("F", """
''''x
 ''xx
 xxxx
,xxxx
""")

_add("G", """
x''xx
 xx,x
 x, x
x,,xx
""")

_add("H", """
'xx'x
 '' x
 xx x
,xx,x
""")

_add("I", """
'x
 x
 x
,x
""")

_add("J", """
xxx'x
xxx x
'xx x
x,,xx
""")

_add("K", """
'xx'x
 ',xx
 x,'x
,xx,x
""")

_add("L", """
'xxxx
 xxxx
 xxxx
,,,,x
""")

_add("M", """
'xxx'x
 ,', x
 xxx x
,xxx,x
""")

_add("N", """
'xx'x
 ,' x
 xx x
,xx,x
""")

_add("O", """
x''xx
 xx x
 xx x
x,,xx
""")

_add("P", """
'''xx
 xx x
 ,,xx
,xxxx
""")

_add("Q", """
x''xx
 xx x
 x' x
x,,,x
""")

_add("R", """
'''xx
 xx x
 ,,'x
,xx,x
""")

_add("S", """
x'''x
,''xx
xxx x
,,,xx
""")

_add("T", """
'''x
x xx
x xx
x,xx
""")

_add("U", """
'xx'x
 xx x
 xx x
x,,xx
""")

_add("V", """
'xx'x
 xx x
 x',x
,,xxx
""")

_add("W", """
'xxx'x
 xxx x
 ',' x
,xxx,x
""")

_add("X", """
'xx'x
,'',x
',,'x
,xx,x
""")

_add("Y", """
'xx'x
,'' x
xx',x
x,xxx
""")

_add("Z", """
''''x
xx',x
',xxx
,,,,x
""")

_add("1", """
x'x
, x
x x
x,x
""")

_add("2", """
x''xx
,x',x
',xxx
,,,,x
""")

_add("3", """
x''xx
,x',x
'xx x
x,,xx
""")

_add("4", """
'xxxx
 x'xx
 ' 'x
xx,xx
""")

_add("5", """
''''x
 ''xx
'xx x
x,,xx
""")

_add("6", """
x''xx
 ''xx
 xx x
x,,xx
""")

_add("7", """
''''x
xxx x
x',xx
x,xxx
""")

_add("8", """
x''xx
,'',x
 xx x
x,,xx
""")

_add("9", """
x''xx
 xx x
x,, x
x,,xx
""")

_add("0", """
x''xx
 xx x
 xx x
x,,xx
""")



def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError as e:
        raise LetterNotDefined(e)