from ceefax.fonts.font import Font
from ceefax.fonts.size4 import size4font

letters = {"|": "x\n"
                "x\n"
                "x\n"
                "x",
           "-": "xxx\n"
                "''x\n"
                "xxx\n"
                "xxx",
           u"–": "xxx\n"
                 "''x\n"
                 "xxx\n"
                 "xxx",
           "!": "'x\n"
                " x\n"
                ",x\n"
                ",x",
           "#": "x'x'xx\n"
                ", , ,x\n"
                ", , ,x\n"
                "xxxxxx",
           "/": "xxxxx\n"
                "xx',x\n"
                "',xxx\n"
                "xxxxx",
           ":": "xx\n"
                "'x\n"
                "'x\n"
                "xx",
           ".": "xx\n"
                "xx\n"
                "xx\n"
                ",x",
           ",": "xx\n"
                "xx\n"
                "xx\n"
                " x",
           "?": "x''xx\n"
                ",xx x\n"
                "xx,xx\n"
                "xx,xx",
           "@": "',,,,, x\n"
                " x , x x\n"
                " x '   x\n"
                ",''''''x",
           u"▲": "xxxxxx\n"
                 "xx'xxx\n"
                 "'   'x\n"
                 "xxxxxx",
           u"▼": "xxxxxx\n"
                 "'''''x\n"
                 "x, ,xx\n"
                 "xxxxxx",
           "%": "'xxxx\n"
                "xx',x\n"
                "',xxx\n"
                "xxx,x",
           "'": "'x\n"
                ",x\n"
                "xx\n"
                "xx",
           u"’": "'x\n"
                 ",x\n"
                 "xx\n"
                 "xx",
           u"∨": "xxxxx\n"
                 "'xx'x\n"
                 " '',x\n"
                 "xxxxx",
           u"∧": "xxxxx\n"
                 "'''xx\n"
                 " xx x\n"
                 "xxxxx",
           u"¬": "xxxxx\n"
                 "''''x\n"
                 "xxx x\n"
                 "xxxxx",
           u"⇾": "xxxxx\n"
                 "xx'xx\n"
                 ",, ,x\n"
                 "xxxxx",
           u"⇿": "xxxxxx\n"
                 "x'x'xx\n"
                 ", , ,x\n"
                 "xxxxxx",
           "(": "',x\n"
                " xx\n"
                " xx\n"
                ",'x",
           u"°": "x'xx\n"
                 ",',x\n"
                 "xxxx\n"
                 "xxxx",
           ")": ",'x\n"
                "x x\n"
                "x x\n"
                "',x",
           "&": "xxxx\n"
                "x'xx\n"
                ", ,x\n"
                "xxxx",
           "=": "xxxxx\n"
                "''''x\n"
                "''''x\n"
                "xxxxx",
           "$": "x' 'x\n"
                ",''xx\n"
                "'xx x\n"
                "x, xx",
           u"£": "xx''x\n"
                 "' 'xx\n"
                 "x xxx\n"
                 ",,,,x",
           u"€": "xx''x\n"
                 "' 'xx\n"
                 "x xxx\n"
                 "xx,,x",
           u"฿": "xxxxxx' 'xx\n"
                 "''''xx '',x\n"
                 " x x x xx x\n"
                 ",xxx,x, ,xx",
           u"₺": "x'xxx\n"
                 "x 'xx\n"
                 ", x'x\n"
                 "x,,xx",
           u"¥": "'xx'x\n"
                 ",'',x\n"
                 "x' 'x\n"
                 "xx,xx",
           u"㎎": "xxxxxxxxxxx\n"
                 " , ,'x',, x\n"
                 " x x xx,, x\n"
                 "xxxxxx,,,xx",
           " ": "xxx\n"
                "xxx\n"
                "xxx\n"
                "xxx",
           "A": "x''''xx\n"
                "  xx  x\n"
                "  ,,  x\n"
                ",,xx,,x",
           "B": "'''''xx\n"
                "  '',,x\n"
                "  xx  x\n"
                ",,,,,xx",
           "C": "x''''xx\n"
                "  xx,,x\n"
                "  xx''x\n"
                "x,,,,xx",
           "D": "'''''xx\n"
                "  xx  x\n"
                "  xx  x\n"
                ",,,,,xx",
           "E": "''''''x\n"
                "  '''xx\n"
                "  xxxxx\n"
                ",,,,,,x",
           "F": "''''''x\n"
                "  '''xx\n"
                "  xxxxx\n"
                ",,xxxxx",
           "G": "x''''xx\n"
                "  xx,,x\n"
                "  x,  x\n"
                "x,,,,xx",
           "H": "''xx''x\n"
                "  ''  x\n"
                "  xx  x\n"
                ",,xx,,x",
           "I": "''x\n"
                "  x\n"
                "  x\n"
                ",,x",
           "J": "xxxx''x\n"
                "xxxx  x\n"
                "''xx  x\n"
                "x,,,,xx",
           "K": "''xx''x\n"
                "  ' ,xx\n"
                "  x, 'x\n"
                ",,xx,,x",
           "L": "''xxxxx\n"
                "  xxxxx\n"
                "  xxxxx\n"
                ",,,,,,x",
           "M": "''xxx''x\n"
                "  ,',  x\n"
                "  xxx  x\n"
                ",,xxx,,x",
           "N": "''xx''x\n"
                "  ,'  x\n"
                "  xx  x\n"
                ",,xx,,x",
           "O": "x''''xx\n"
                "  xx  x\n"
                "  xx  x\n"
                "x,,,,xx",
           "P": "'''''xx\n"
                "  xx  x\n"
                "  ,,,xx\n"
                ",,xxxxx",
           "Q": "x''''xx\n"
                "  xx  x\n"
                "  x'  x\n"
                "x,,,,,x",
           "R": "'''''xx\n"
                "  xx  x\n"
                "  ,, 'x\n"
                ",,xx,,x",
           "S": "x'''''x\n"
                ", '''xx\n"
                "xxxx  x\n"
                ",,,,,xx",
           "T": "''''''x\n"
                "xx  xxx\n"
                "xx  xxx\n"
                "xx,,xxx",
           "U": "''xx''x\n"
                "  xx  x\n"
                "  xx  x\n"
                "x,,,,xx",
           "V": "''xx''x\n"
                "  xx  x\n"
                "  x' ,x\n"
                ",,,,xxx",
           "W": "''xxx''x\n"
                "  xxx  x\n"
                "  ','  x\n"
                ",,xxx,,x",
           "X": "''xx''x\n"
                ", '' ,x\n"
                "' ,, 'x\n"
                ",,xx,,x",
           "Y": "''xx''x\n"
                ", '' ,x\n"
                "xx  xxx\n"
                "xx,,xxx",
           "Z": "''''''x\n"
                "xx'',,x\n"
                "' ,xxxx\n"
                ",,,,,,x",
           "1": "x''x\n"
                ",  x\n"
                "x  x\n"
                "x,,x",
           "2": "x''''xx\n"
                ",,x' ,x\n"
                "x' ,xxx\n"
                ",,,,,,x",
           "3": "x''''xx\n"
                ",,x' ,x\n"
                "''xx  x\n"
                "x,,,,xx",
           "4": "''xxxxx\n"
                "  x''xx\n"
                "  '  'x\n"
                "xxx,,xx",
           "5": "''''''x\n"
                "  '''xx\n"
                "''xx  x\n"
                "x,,,,xx",
           "6": "x''''xx\n"
                "  '''xx\n"
                "  xx  x\n"
                "x,,,,xx",
           "7": "''''''x\n"
                "xxxx  x\n"
                "xx' ,xx\n"
                "xx,,xxx",
           "8": "x''''xx\n"
                ", '' ,x\n"
                "  xx  x\n"
                "x,,,,xx",
           "9": "x''''xx\n"
                "  xx  x\n"
                "x,,,  x\n"
                "x,,,,xx",
           "0": "x''''xx\n"
                "  xx  x\n"
                "  xx  x\n"
                "x,,,,xx"}

size4boldfont = Font(letters, squashed=size4font)
