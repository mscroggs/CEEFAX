from ceefax import config


class LetterBlock:
    def __init__(self, _str):
        self._str = _str

    def __add__(self, other):
        return LetterBlock(
            "\n".join([l1 + l2 for l1, l2 in
                       zip(self._str.split("\n"),
                           other._str.split("\n"))]))

    def __str__(self):
        return self._str

    def __len__(self):
        return len(self._str.split("\n")[0])


def process_printing_options(function):
    def wrapper(self, text, **options):
        padding_options = options.get("padding", {})
        padding_enabled = padding_options != {}
        left_shift = padding_options.get("left", 0)
        filler = padding_options.get("filler", "|")
        if padding_enabled:
            text = filler * left_shift + text

        result = function(self, text)

        if padding_enabled:
            right_shift = config.WIDTH - len(result)
            if right_shift > 0:
                result += function(self, filler * right_shift)

        return result

    return wrapper


class Font:
    def __init__(self, letters, squashed=None, no_char=None):
        self.squashed = squashed
        self.size = None
        self.letters = {}
        for c, l in letters.items():
            if self.size is None:
                self.size = len(l.split("\n"))
            assert self.size == len(l.split("\n"))
            self.letters[c] = LetterBlock(l)
        if no_char is None:
            self.no_char = "xxxxx\n"
            self.no_char += " ,, x\n"
            self.no_char += " xx x\n" * (self.size - 4)
            self.no_char += " '' x\n"
            self.no_char += "xxxxx"
        else:
            self.no_char = no_char

    @process_printing_options
    def text_to_letterblock(self, text):
        from functools import reduce
        return str(reduce(LetterBlock.__add__,
                          map(self.get_letter, text)))

    def get_letter(self, char):
        if char in self.letters:
            return self.letters[char]
        elif char.upper() in self.letters:
            return self.letters[char.upper()]
        elif char.lower() in self.letters:
            return self.letters[char.lower()]
        else:
            return self.no_char

    def text_to_ascii(self, text, fill=True, vertical_condense=False,
                      max_width=config.WIDTH, **options):
        text_to_print = str(self.text_to_letterblock("|" + text, **options))
        output = []
        hit_sides = False
        for line in text_to_print.split("\n"):
            if len(line) > max_width:
                output.append(line[:max_width])
                hit_sides = True
            elif fill:
                output.append(line + "x" * (max_width - len(line)))
            else:
                output.append(line)
        if vertical_condense:
            output = self.v_condense(output)

        if hit_sides and self.squashed is not None:
            return self.squashed.text_to_ascii(
                text, fill, vertical_condense=vertical_condense, **options)

        return "\n".join(output)

    def v_condense(self, text):
        output = []
        for i in range(0, len(text), 2):
            line = ""
            if i + 1 == len(text):
                text.append("x" * len(text[i]))
            for a, b in zip(text[i], text[i + 1]):
                if a + b == "xx":
                    line += "x"
                elif a + b == "x ":
                    line += "'"
                elif a + b == "' ":
                    line += "'"
                elif a + b == ", ":
                    line += "'"
                elif a + b == " x":
                    line += ","
                elif a + b == " ,":
                    line += ","
                elif a + b == " '":
                    line += ","
                elif a + b == "  ":
                    line += " "
                else:
                    line += "x"
            output.append(line)
        return output
