from ceefax.fonts.font import Font

letters = {"|": "x\n"
                "x\n"
                "x\n"
                "x",
           "@": "',,, x\n"
                " x x x\n"
                " x   x\n"
                ",''''x",
           "-": "xxx\n"
                "''x\n"
                "xxx\n"
                "xxx",
           u"–": "xxx\n"
                 "''x\n"
                 "xxx\n"
                 "xxx",
           "–": "xxx\n"
                "''x\n"
                "xxx\n"
                "xxx",
           "_": "xxx\n"
                "xxx\n"
                "xxx\n"
                ",,x",
           "!": "'x\n"
                " x\n"
                ",x\n"
                ",x",
           "/": "xxxxx\n"
                "xx',x\n"
                "',xxx\n"
                "xxxxx",
           "#": "x'x'xx\n"
                ", , ,x\n"
                ", , ,x\n"
                "xxxxxx",
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
           u"‘": "'x\n"
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
           u"฿": "' 'xx\n"
                 " '',x\n"
                 " xx x\n"
                 ", ,xx",
           u"₺": "x'xxx\n"
                 "x 'xx\n"
                 ", x'x\n"
                 "x,,xx",
           u"¥": "'xx'x\n"
                 ",'',x\n"
                 "x' 'x\n"
                 "xx,xx",
           u"₫": "xxx'x\n"
                 "x , x\n"
                 "x,,,x\n"
                 "x,,,x",
           u"₽": "x'''x\n"
                 "x ' x\n"
                 "' 'xx\n"
                 "x,xxx",
           u"㎎": "xxxxxxxxxxx\n"
                 " , ,'x',, x\n"
                 " x x xx,, x\n"
                 "xxxxxx,,,xx",
           u"㏂": "xxxxxxxxxx\n"
                 "x,'x , ,'x\n"
                 "', x x x x\n"
                 "x,,x,x,x,x",
           u"㏘": "xxxxxxxxxx\n"
                 " ,'x , ,'x\n"
                 " ',x x x x\n"
                 ",xxx,x,x,x",
           " ": "xxx\n"
                "xxx\n"
                "xxx\n"
                "xxx",
           "A": "x''xx\n"
                " xx x\n"
                " ,, x\n"
                ",xx,x",
           "B": "'''xx\n"
                " '',x\n"
                " xx x\n"
                ",,,xx",
           "C": "x''xx\n"
                " xx,x\n"
                " xx'x\n"
                "x,,xx",
           "D": "'''xx\n"
                " xx x\n"
                " xx x\n"
                ",,,xx",
           "E": "''''x\n"
                " ''xx\n"
                " xxxx\n"
                ",,,,x",
           "F": "''''x\n"
                " ''xx\n"
                " xxxx\n"
                ",xxxx",
           "G": "x''xx\n"
                " xx,x\n"
                " x, x\n"
                "x,,xx",
           "H": "'xx'x\n"
                " '' x\n"
                " xx x\n"
                ",xx,x",
           "I": "'x\n"
                " x\n"
                " x\n"
                ",x",
           "J": "xxx'x\n"
                "xxx x\n"
                "'xx x\n"
                "x,,xx",
           "K": "'xx'x\n"
                " ',xx\n"
                " x,'x\n"
                ",xx,x",
           "L": "'xxxx\n"
                " xxxx\n"
                " xxxx\n"
                ",,,,x",
           "M": "'xxx'x\n"
                " ,', x\n"
                " xxx x\n"
                ",xxx,x",
           "N": "'xx'x\n"
                " ,' x\n"
                " xx x\n"
                ",xx,x",
           "O": "x''xx\n"
                " xx x\n"
                " xx x\n"
                "x,,xx",
           "P": "'''xx\n"
                " xx x\n"
                " ,,xx\n"
                ",xxxx",
           "Q": "x''xx\n"
                " xx x\n"
                " xx x\n"
                "x,,'x",
           "R": "'''xx\n"
                " xx x\n"
                " ,,'x\n"
                ",xx,x",
           "S": "x'''x\n"
                ",''xx\n"
                "xxx x\n"
                ",,,xx",
           "T": "'''x\n"
                "x xx\n"
                "x xx\n"
                "x,xx",
           "U": "'xx'x\n"
                " xx x\n"
                " xx x\n"
                "x,,xx",
           "V": "'xx'x\n"
                " xx x\n"
                " x',x\n"
                ",,xxx",
           "W": "'xxx'x\n"
                " xxx x\n"
                " ',' x\n"
                ",xxx,x",
           "X": "'xx'x\n"
                ",'',x\n"
                "',,'x\n"
                ",xx,x",
           "Y": "'xx'x\n"
                ",'' x\n"
                "xx',x\n"
                "x,xxx",
           "Z": "''''x\n"
                "xx',x\n"
                "',xxx\n"
                ",,,,x",
           "a": "xxxx\n"
                ",,'x\n"
                "', x\n"
                ",,,x",
           "b": "'xxx\n"
                " ,'x\n"
                " x x\n"
                ",,xx",
           "c": "xxxx\n"
                "',,x\n"
                " xxx\n"
                "x,,x",
           "d": "xx'x\n"
                "', x\n"
                " x x\n"
                "x,,x",
           "e": "xxxx\n"
                "','x\n"
                " ,,x\n"
                "x,,x",
           "f": "x'x\n"
                " 'x\n"
                " xx\n"
                ",xx",
           "g": "xxxx\n"
                "', x\n"
                ",' x\n"
                "'',x",
           "h": "'xxx\n"
                " ,'x\n"
                " x x\n"
                ",x,x",
           "i": "'x\n"
                "'x\n"
                " x\n"
                ",x",
           "j": "x'x\n"
                "x'x\n"
                "x x\n"
                "',x",
           "k": "'xxx\n"
                " x x\n"
                " ,'x\n"
                ",x,x",
           "l": "'x\n"
                " x\n"
                " x\n"
                ",x",
           "m": "xxxxxx\n"
                " ,','x\n"
                " x x x\n"
                ",xxx,x",
           "n": "xxxx\n"
                " ,'x\n"
                " x x\n"
                ",x,x",
           "o": "xxxx\n"
                "','x\n"
                " x x\n"
                "x,xx",
           "p": "xxxx\n"
                " ,'x\n"
                " ',x\n"
                " xxx",
           "q": "xxxx\n"
                "', x\n"
                ",' x\n"
                "xx x",
           "r": "xxxx\n"
                " ',x\n"
                " xxx\n"
                ",xxx",
           "s": "xxxx\n"
                "',,x\n"
                "x,'x\n"
                ",,xx",
           "t": "'xx\n"
                " ,x\n"
                " xx\n"
                "x,x",
           "u": "xxxx\n"
                " x x\n"
                " x x\n"
                "x,,x",
           "v": "xxxx\n"
                " x x\n"
                " x x\n"
                ",,xx",
           "w": "xxxxxx\n"
                " x x x\n"
                " x x x\n"
                ",,,,xx",
           "x": "xxxx\n"
                ",',x\n"
                "x xx\n"
                ",x,x",
           "y": "xxxx\n"
                " x x\n"
                ",' x\n"
                "'',x",
           "z": "xxxx\n"
                ",, x\n"
                "',xx\n"
                ",,,x",
           "1": "x'x\n"
                ", x\n"
                "x x\n"
                "x,x",
           "2": "x''xx\n"
                ",x',x\n"
                "',xxx\n"
                ",,,,x",
           "3": "x''xx\n"
                ",x',x\n"
                "'xx x\n"
                "x,,xx",
           "4": "'xxxx\n"
                " x'xx\n"
                " ' 'x\n"
                "xx,xx",
           "5": "''''x\n"
                " ''xx\n"
                "'xx x\n"
                "x,,xx",
           "6": "x''xx\n"
                " ''xx\n"
                " xx x\n"
                "x,,xx",
           "7": "''''x\n"
                "xxx x\n"
                "x',xx\n"
                "x,xxx",
           "8": "x''xx\n"
                ",'',x\n"
                " xx x\n"
                "x,,xx",
           "9": "x''xx\n"
                " xx x\n"
                "x,, x\n"
                "x,,xx",
           "0": "x''xx\n"
                " xx x\n"
                " xx x\n"
                "x,,xx",
           u"Đ": "x'''xx\n"
                 "' 'x x\n"
                 "x xx x\n"
                 "x,,,xx",
           u"Š": "x,',\n"
                 "',,x\n"
                 "x,'x\n"
                 ",,xx",
           u"Ü": "'xx'x\n"
                 "'xx'x\n"
                 " xx x\n"
                 "x,,xx",
           u"á": "',xx\n"
                 "x,'x\n"
                 "', x\n"
                 ",,,x",
           u"ả": "',xx\n"
                 "x,'x\n"
                 "', x\n"
                 ",,,x",
           u"ã": ",,,x\n"
                 ",,'x\n"
                 "', x\n"
                 ",,,x",
           "ç": "xxxx\n"
                "',,x\n"
                " xxx\n"
                "x ,x",
           u"é": "',xx\n"
                 "','x\n"
                 " ,,x\n"
                 "x,,x",
           u"ğ": ",',x\n"
                 "', x\n"
                 "x, x\n"
                 ",,xx",
           u"í": "',x\n"
                 "'xx\n"
                 " xx\n"
                 ",xx",
           u"ł": "x'xx\n"
                 "' ,x\n"
                 "x xx\n"
                 "x,xx",
           u"ñ": "'''x\n"
                 "''xx\n"
                 " x x\n"
                 ",x,x",
           u"ø": "xxxx'x\n"
                 "x','xx\n"
                 "x x xx\n"
                 ",x,xxx",
           u"ó": "',xx\n"
                 "x'xx\n"
                 " x x\n"
                 "x,xx",
           u"ô": "'.'x\n"
                 "x'xx\n"
                 " x x\n"
                 "x,xx",
           u"ö": "'x'x\n"
                 "x'xx\n"
                 " x x\n"
                 "x,xx",
           "ō": ",,,x\n"
                "','x\n"
                " x x\n"
                "x,xx",
           u"ộ": "'.'x\n"
                 "x'xx\n"
                 ",',x\n"
                 "x'xx",
           u"ú": "x',x\n"
                 "'x'x\n"
                 " x x\n"
                 "x,,x",
           u"ü": "'x'x\n"
                 "'x'x\n"
                 " x x\n"
                 "x,,x",
           u"ý": "x',x\n"
                 "'x'x\n"
                 ",, x\n"
                 ",,xx",
           # Cyrillic ==============
           u"А": "x''xx\n"
                 " xx x\n"
                 " ,, x\n"
                 ",xx,x",
           u"Б": "''''x\n"
                 " ''xx\n"
                 " xx x\n"
                 ",,,xx",
           u"В": "'''xx\n"
                 " '',x\n"
                 " xx x\n"
                 ",,,xx",
           u"Г": "''''x\n"
                 " xxxx\n"
                 " xxxx\n"
                 ",xxxx",
           u"Д": "x'''x\n"
                 " xx x\n"
                 " '' x\n"
                 ",xx,x",
           u"Е": "''''x\n"
                 " ''xx\n"
                 " xxxx\n"
                 ",,,,x",
           u"Ё": "x,x,x\n"
                 " ,,,x\n"
                 " ,,xx\n"
                 ",,,,x",
           u"Ж": "'xx'xx'x\n"
                 "x,' ',xx\n"
                 "',x x,'x\n"
                 ",xx,xx,x",
           u"З": "x''xx\n"
                 ",x',x\n"
                 "'xx x\n"
                 "x,,xx",
           u"И": "'xx'x\n"
                 " ', x\n"
                 " xx x\n"
                 ",xx,x",
           u"Й": "x,,xx\n"
                 " x' x\n"
                 " ,x x\n"
                 ",xx,x",
           u"К": "'xx'x\n"
                 " ',xx\n"
                 " x,'x\n"
                 ",xx,x",
           u"Л": "x'''x\n"
                 "x x x\n"
                 "x x x\n"
                 ",xx,x",
           u"М": "'xxx'x\n"
                 " ,', x\n"
                 " xxx x\n"
                 ",xxx,x",
           u"Н": "'xx'x\n"
                 " '' x\n"
                 " xx x\n"
                 ",xx,x",
           u"О": "x''xx\n"
                 " xx x\n"
                 " xx x\n"
                 "x,,xx",
           u"П": "''''x\n"
                 " xx x\n"
                 " xx x\n"
                 ",xx,x",
           u"Р": "'''xx\n"
                 " xx x\n"
                 " ,,xx\n"
                 ",xxxx",
           u"С": "x''xx\n"
                 " xx,x\n"
                 " xx'x\n"
                 "x,,xx",
           u"Т": "'''x\n"
                 "x xx\n"
                 "x xx\n"
                 "x,xx",
           u"У": "'xx'x\n"
                 ",'' x\n"
                 "xx',x\n"
                 "x,xxx",
           u"Ф": "xx'xxx\n"
                 "',,,'x\n"
                 ",''',x\n"
                 "xx,xxx",
           u"Х": "'xx'x\n"
                 ",'',x\n"
                 "',,'x\n"
                 ",xx,x",
           u"Ц": "'xx'x\n"
                 " xx x\n"
                 " xx x\n"
                 ",,, x",
           u"Ч": "'xx'x\n"
                 ",'' x\n"
                 "xxx x\n"
                 "xxx,x",
           u"Ш": "'x'x'x\n"
                 " x x x\n"
                 " x x x\n"
                 ",,,,,x",
           u"Щ": "'x'x'x\n"
                 " x x x\n"
                 " x x x\n"
                 ",,,, x",
           u"Ъ": "''xxxx\n"
                 "x ''xx\n"
                 "x xx x\n"
                 "x,,,xx",
           u"Ы": "'xxxx'x\n"
                 " ''xx x\n"
                 " xx x x\n"
                 ",,,xx,x",
           u"Ь": "'xxxx\n"
                 " ''xx\n"
                 " xx x\n"
                 ",,,xx",
           u"Э": "x''xx\n"
                 ",x' x\n"
                 "'xx x\n"
                 "x,,xx",
           u"Ю": " xx''xx\n"
                 " ' xx x\n"
                 " x xx x\n"
                 " xx,,xx",
           u"Я": "x'''x\n"
                 " xx x\n"
                 "',, x\n"
                 ",xx,x",
           u"а": "xxxx\n"
                 ",,'x\n"
                 "', x\n"
                 ",,,x",
           u"б": "x'xx\n"
                 " ,'x\n"
                 " x x\n"
                 ",,xx",
           u"в": "xxxx\n"
                 " ,'x\n"
                 " ,'x\n"
                 ",,xx",
           u"г": "xxxx\n"
                 " ,,x\n"
                 " xxx\n"
                 ",xxx",
           u"д": "xxxx\n"
                 "', x\n"
                 " ' x\n"
                 ",x,x",
           u"е": "xxxx\n"
                 "','x\n"
                 " ,,x\n"
                 "x,,x",
           u"ё": ",x,x\n"
                 "','x\n"
                 " ,,x\n"
                 "x,,x",
           u"ж": "xxxxxx\n"
                 " x x x\n"
                 "', ,'x\n"
                 ",x,x,x",
           u"з": "xxxx\n"
                 ",,'x\n"
                 ",,'x\n"
                 ",,xx",
           u"и": "xxxxx\n"
                 " x' x\n"
                 " ,x x\n"
                 ",xx,x",
           u"й": ",,,,x\n"
                 " x' x\n"
                 " ,x x\n"
                 ",xx,x",
           u"к": "xxxx\n"
                 " x x\n"
                 " ,'x\n"
                 ",x,x",
           u"л": "xxxx\n"
                 "', x\n"
                 " x x\n"
                 ",x,x",
           u"м": "xxxxxx\n"
                 " 'x' x\n"
                 " x x x\n"
                 ",xxx,x",
           u"н": "xxxx\n"
                 " x x\n"
                 " , x\n"
                 ",x,x",
           u"о": "xxxx\n"
                 "','x\n"
                 " x x\n"
                 "x,xx",
           u"п": "xxxx\n"
                 " , x\n"
                 " x x\n"
                 ",x,x",
           u"р": "xxxx\n"
                 " ,'x\n"
                 " ',x\n"
                 ",xxx",
           u"с": "xxxx\n"
                 "',,x\n"
                 " xxx\n"
                 "x,,x",
           u"т": "xxxx\n"
                 ", ,x\n"
                 "x xx\n"
                 "x,xx",
           u"у": "xxxx\n"
                 " x x\n"
                 "x, x\n"
                 ",,xx",
           u"ф": "xx'xxx\n"
                 "x' 'xx\n"
                 ",''',x\n"
                 "xx,xxx",
           u"х": "xxxx\n"
                 ",',x\n"
                 "x xx\n"
                 ",x,x",
           u"ц": "xxxx\n"
                 " x x\n"
                 " x x\n"
                 ",, x",
           u"ч": "xxxx\n"
                 " x x\n"
                 "x, x\n"
                 "xx,x",
           u"ш": "xxxxxx\n"
                 " x x x\n"
                 " x x x\n"
                 ",,,,,x",
           u"щ": "xxxxxx\n"
                 " x x x\n"
                 " x x x\n"
                 ",,,, x",
           u"ъ": "xxxx\n"
                 ", 'xx\n"
                 "x x x\n"
                 "x,,xx",
           u"ы": "xxxxxx\n"
                 " 'xx x\n"
                 " x x x\n"
                 ",,xx,x",
           u"ь": "xxxx\n"
                 " 'xx\n"
                 " x x\n"
                 ",,xx",
           u"э": "xxxx\n"
                 ",,'x\n"
                 "x, x\n"
                 ",,xx",
           u"ю": "xxxxxx\n"
                 " '','x\n"
                 " x x x\n"
                 "xxx,xx",
           u"я": "xxxxx\n"
                 "',, x\n"
                 "',, x\n"
                 ",xx,x",
           # Greek =================
           u"Α": "x''xx\n"
                 " xx x\n"
                 " ,, x\n"
                 ",xx,x",
           u"Β": "'''xx\n"
                 " '',x\n"
                 " xx x\n"
                 ",,,xx",
           u"Γ": "''''x\n"
                 " xxxx\n"
                 " xxxx\n"
                 ",xxxx",
           u"Δ": "x''xx\n"
                 " xx x\n"
                 " xx x\n"
                 ",,,,x",
           u"Ε": "''''x\n"
                 " ''xx\n"
                 " xxxx\n"
                 ",,,,x",
           u"Ζ": "''''x\n"
                 "xx',x\n"
                 "',xxx\n"
                 ",,,,x",
           u"Η": "'xx'x\n"
                 " '' x\n"
                 " xx x\n"
                 ",xx,x",
           u"Θ": "x''xx\n"
                 " '' x\n"
                 " xx x\n"
                 "x,,xx",
           u"Ι": "'x\n"
                 " x\n"
                 " x\n"
                 ",x",
           u"Κ": "'xx'x\n"
                 " ',xx\n"
                 " x,'x\n"
                 ",xx,x",
           u"Λ": "x'''x\n"
                 " xx x\n"
                 " xx x\n"
                 ",xx,x",
           u"Μ": "'xxx'x\n"
                 " ,', x\n"
                 " xxx x\n"
                 ",xxx,x",
           u"Ν": "'xx'x\n"
                 " ,' x\n"
                 " xx x\n"
                 ",xx,x",
           u"Ξ": "''''x\n"
                 "''''x\n"
                 "xxxxx\n"
                 ",,,,x",
           u"Ο": "x''xx\n"
                 " xx x\n"
                 " xx x\n"
                 "x,,xx",
           u"Π": "''''x\n"
                 " xx x\n"
                 " xx x\n"
                 ",xx,x",
           u"Ρ": "'''xx\n"
                 " xx x\n"
                 " ,,xx\n"
                 ",xxxx",
           u"Σ": "''''x\n"
                 ",'xxx\n"
                 "',xxx\n"
                 ",,,,x",
           u"Τ": "'''x\n"
                 "x xx\n"
                 "x xx\n"
                 "x,xx",
           u"Υ": "'xx'x\n"
                 ",'' x\n"
                 "xx xx\n"
                 "xx,xx",
           u"Φ": "xx'xxx\n"
                 "', ,'x\n"
                 ",' ',x\n"
                 "xx,xxx",
           u"Χ": "'xx'x\n"
                 ",'',x\n"
                 "',,'x\n"
                 ",xx,x",
           u"Ψ": "'x'x'x\n"
                 " x x x\n"
                 ",' ',x\n"
                 "xx,xxx",
           u"Ω": "x'''xx\n"
                 " xxx x\n"
                 ",'x',x\n"
                 ",,x,,x",
           u"α": "xxxx\n"
                 "', x\n"
                 " x x\n"
                 "x,,x",
           u"β": "x'xx\n"
                 " ',x\n"
                 " ',x\n"
                 ",xxx",
           u"γ": "xxxx\n"
                 " x x\n"
                 ",',x\n"
                 "x,xx",
           u"δ": "x'xx\n"
                 ",'xx\n"
                 " x x\n"
                 "x,xx",
           u"ε": "xxxx\n"
                 "',,x\n"
                 " ,,x\n"
                 "x,,x",
           u"ζ": "'''x\n"
                 "x',x\n"
                 " xxx\n"
                 "x,,x",
           u"η": "xxxx\n"
                 " ,'x\n"
                 " x x\n"
                 "xx,x",
           u"θ": "x'xx\n"
                 " ' x\n"
                 " x x\n"
                 "x,xx",
           u"ι": "xx\n"
                 " x\n"
                 " x\n"
                 ",x",
           u"κ": "xxxx\n"
                 " x x\n"
                 " ,'x\n"
                 ",x,x",
           u"λ": "''xx\n"
                 "x' x\n"
                 " x x\n"
                 ",x,x",
           u"μ": "xxxx\n"
                 " x x\n"
                 " x x\n"
                 ",,xx",
           u"ν": "xxxx\n"
                 ",,'x\n"
                 "', x\n"
                 ",,,x",
           u"ξ": "'''x\n"
                 ",''x\n"
                 ",''x\n"
                 "xx,x",
           u"ο": "xxxx\n"
                 "','x\n"
                 " x x\n"
                 "x,xx",
           u"π": "xxxx\n"
                 " , x\n"
                 " x x\n"
                 ",x,x",
           u"ρ": "xxxx\n"
                 "','x\n"
                 " ',x\n"
                 ",xxx",
           u"σ": "xxxxx\n"
                 "', ,x\n"
                 " x xx\n"
                 "x,xxx",
           u"ς": "xxxx\n"
                 "',,x\n"
                 "x,'x\n"
                 ",,xx",
           u"τ": "xxxx\n"
                 ", ,x\n"
                 "x xx\n"
                 "xx,x",
           u"υ": "xxxx\n"
                 " x x\n"
                 " x x\n"
                 "x,xx",
           u"φ": "xx'xxx\n"
                 "x' 'xx\n"
                 ",' ',x\n"
                 "xx,xxx",
           u"χ": "xxxx\n"
                 " x x\n"
                 "','x\n"
                 ",x,x",
           u"ψ": "xxxxxx\n"
                 " x x x\n"
                 ",' ',x\n"
                 "xx,xxx",
           u"ω": "xxxxxx\n"
                 "',x,'x\n"
                 " x x x\n"
                 "x,,,xx"}

size4font = Font(letters)
