from ceefax.fonts.font import Font

letters = {"'": " x\n"
                " x\n"
                "xx\n"
                "xx\n"
                "xx\n"
                "xx\n"
                "xx",
           "(": "xxx\n"
                "' x\n"
                " 'x\n"
                " 'x\n"
                " 'x\n"
                ", x\n"
                "xxx",
           ")": "xxx\n"
                " 'x\n"
                "' x\n"
                "' x\n"
                "' x\n"
                " ,x\n"
                "xxx",
           "&": "xxxx\n"
                "xxxx\n"
                "x xx\n"
                "   x\n"
                "x xx\n"
                "xxxx\n"
                "xxxx",
           "|": "x\n"
                "x\n"
                "x\n"
                "x\n"
                "x\n"
                "x\n"
                "x",
           "-": "xx\n"
                "xx\n"
                "xx\n"
                " x\n"
                "xx\n"
                "xx\n"
                "xx",
           "!": "xxx\n"
                " x\n"
                " x\n"
                " x\n"
                "xx\n"
                " x\n"
                "xx",
           "?": "xxx\n"
                "  x\n"
                "x x\n"
                " xx\n"
                "xxx\n"
                " xx\n"
                "xxx",
           "/": "xxxx\n"
                "xx x\n"
                "x',x\n"
                "x xx\n"
                "',xx\n"
                " xxx\n"
                "xxxx",
           " ": "xx\n"
                "xx\n"
                "xx\n"
                "xx\n"
                "xx\n"
                "xx\n"
                "xx",
           "A": "xxxx\n"
                "' 'x\n"
                " x x\n"
                "   x\n"
                " x x\n"
                " x x\n"
                "xxxx",
           "B": "xxxx\n"
                "  'x\n"
                " x x\n"
                "  xx\n"
                " x x\n"
                "  ,x\n"
                "xxxx",
           "C": "xxx\n"
                "  x\n"
                " xx\n"
                " xx\n"
                " xx\n"
                "  x\n"
                "xxx",
           "D": "xxxx\n"
                "  'x\n"
                " x x\n"
                " x x\n"
                " x x\n"
                "  ,x\n"
                "xxxx",
           "E": "xxx\n"
                "  x\n"
                " xx\n"
                "  x\n"
                " xx\n"
                "  x\n"
                "xxx",
           "F": "xxxx\n"
                "  x\n"
                " xx\n"
                "  x\n"
                " xx\n"
                " xx\n"
                "xxx",
           "G": "xxxx\n"
                "' 'x\n"
                " xxx\n"
                " x'x\n"
                " x x\n"
                ",' x\n"
                "xxxx",
           "H": "xxxx\n"
                " x x\n"
                " x x\n"
                "   x\n"
                " x x\n"
                " x x\n"
                "xxxx",
           "I": "xx\n"
                " x\n"
                " x\n"
                " x\n"
                " x\n"
                " x\n"
                "xx",
           "J": "xxxx\n"
                "xx x\n"
                "xx x\n"
                "xx x\n"
                "'x x\n"
                ", ,x\n"
                "xxxx",
           "K": "xxxx\n"
                " x x\n"
                " x x\n"
                "  xx\n"
                " x x\n"
                " x x\n"
                "xxxx",
           "L": "xxx\n"
                " xx\n"
                " xx\n"
                " xx\n"
                " xx\n"
                "  x\n"
                "xxx",
           "M": "xxxxxx\n"
                " 'x' x\n"
                " , , x\n"
                " x,x x\n"
                " xxx x\n"
                " xxx x\n"
                "xxxxxx",
           "N": "xxxx\n"
                "  'x\n"
                " x x\n"
                " x x\n"
                " x x\n"
                " x x\n"
                "xxxx",
           "O": "xxxx\n"
                "' 'x\n"
                " x x\n"
                " x x\n"
                " x x\n"
                ", ,x\n"
                "xxxx",
           "P": "xxxx\n"
                "  'x\n"
                " x x\n"
                "   x\n"
                " xxx\n"
                " xxx\n"
                "xxxx",
           "Q": "xxxx\n"
                "' 'x\n"
                " x x\n"
                " x x\n"
                " x x\n"
                ",  x\n"
                "xxxx",
           "R": "xxxx\n"
                "  'x\n"
                " x x\n"
                "  ,x\n"
                " x x\n"
                " x x\n"
                "xxxx",
           "S": "xxx\n"
                "  x\n"
                " xx\n"
                "  x\n"
                "x x\n"
                "  x\n"
                "xxx",
           "T": "xxxx\n"
                "   x\n"
                "x xx\n"
                "x xx\n"
                "x xx\n"
                "x xx\n"
                "xxxx",
           "U": "xxxx\n"
                " x x\n"
                " x x\n"
                " x x\n"
                " x x\n"
                ", ,x\n"
                "xxxx",
           "V": "xxxx\n"
                " x x\n"
                " x x\n"
                " x x\n"
                " x x\n"
                "  ,x\n"
                "xxxx",
           "W": "xxxxxx\n"
                " xxx x\n"
                " xxx x\n"
                " x'x x\n"
                " x x x\n"
                "  ,  x\n"
                "xxxxxx",
           "X": "xxxx\n"
                " x x\n"
                ",',x\n"
                "x xx\n"
                "','x\n"
                " x x\n"
                "xxxx",
           "Y": "xxxx\n"
                " x x\n"
                " x x\n"
                ", ,x\n"
                "x xx\n"
                "x xx\n"
                "xxxx",
           "Z": "xxxx\n"
                "   x\n"
                "xx x\n"
                "x ,x\n"
                " xxx\n"
                "   x\n"
                "xxxx",
           "1": "xx\n"
                " x\n"
                " x\n"
                " x\n"
                " x\n"
                " x\n"
                "xx",
           "2": "xxxx\n"
                "   x\n"
                "xx x\n"
                "   x\n"
                " xxx\n"
                "   x\n"
                "xxxx",
           "3": "xxxx\n"
                "   x\n"
                "xx x\n"
                "   x\n"
                "xx x\n"
                "   x\n"
                "xxxx",
           "4": "xxxx\n"
                " x x\n"
                " x x\n"
                "   x\n"
                "xx x\n"
                "xx x\n"
                "xxxx",
           "5": "xxxx\n"
                "   x\n"
                " xxx\n"
                "   x\n"
                "xx x\n"
                "   x\n"
                "xxxx",
           "6": "xxxx\n"
                "   x\n"
                " xxx\n"
                "   x\n"
                " x x\n"
                "   x\n"
                "xxxx",
           "7": "xxxx\n"
                "   x\n"
                "xx x\n"
                "xx x\n"
                "xx x\n"
                "xx x\n"
                "xxxx",
           "8": "xxxx\n"
                "   x\n"
                " x x\n"
                "   x\n"
                " x x\n"
                "   x\n"
                "xxxx",
           "9": "xxxx\n"
                "   x\n"
                " x x\n"
                "   x\n"
                "xx x\n"
                "   x\n"
                "xxxx",
           "0": "xxxx\n"
                "   x\n"
                " x x\n"
                " x x\n"
                " x x\n"
                "   x\n"
                "xxxx",
           ".": "xx\n"
                "xx\n"
                "xx\n"
                "xx\n"
                "xx\n"
                " x\n"
                "xx",
           "*": "xxxxx xxxxxx\n"
                "x,'xx,xx',xx\n"
                "xxx'   'xxxx\n"
                ",,x     x,,x\n"
                "xxx,   ,xxxx\n"
                "x',xx'xx,'xx\n"
                "xxxxx xxxxxx",
           # cloud
           "@": "xxxxxxxxxxxxx\n"
                "xxxx'''xxxxxx\n"
                "x'',xxx,'xxxx\n"
                " xx,xxx',,,'x\n"
                ",'''''''''',x\n"
                "xxxxxxxxxxxxx\n"
                "xxxxxxxxxxxxx",
           # rain
           "{": "xxx',,,'xxxxx\n"
                "',,'xxxx ''xx\n"
                " xxxxxx,xxx x\n"
                "x,,,,,,,,,,xx\n"
                "xx','xxxx'xxx\n"
                "x,''',x',x,'x\n"
                "xxxxxxx,''',x",
           # moon
           "}": "xxx'' ,,x\n"
                "x'   ,xxx\n"
                "'   xxxxx\n"
                "    xxxxx\n"
                ",   xxxxx\n"
                "x,   'xxx\n"
                "xxx,, ''x",
           # cloud sun
           "~": "xxxxxxxxxxxxxxxx\n"
                "xxx',,,'xx xx'xx\n"
                "',,'xxxx ''x,xxx\n"
                " xxxxxx,xxx x,,x\n"
                "x,,,,,,,,,,x'xxx\n"
                "xxxxxxxxxx xx,xx\n"
                "xxxxxxxxxxxxxxxx",
           # storm
           "^": "xxx',,,'xxxxx\n"
                "',,'xxxx'xxxx\n"
                " xxxxxx, ''xx\n"
                "x,,x'   ,,,'x\n"
                "xxx,  'xxxx x\n"
                "xxxxx,  'x',x\n"
                "xxxx' ,x,x,xx",
           # snow
           "%": "xxx',,,'xxxxx\n"
                "',,'xxxx ''xx\n"
                " xxxxxx,xxx x\n"
                "x,,,,,,,,,,xx\n"
                "xxxxxx,',xxxx\n"
                "x,',xx,x,xxxx\n"
                "x,x,xxxxxxxxx"}

size7extracondensedfont = Font(letters)
