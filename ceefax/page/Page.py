from ceefax import config
from ceefax.error import error_list
from ceefax.fonts import get_font

WARNING_USED = False

color_codes = {"k": "BLACK", "K": "GREY",
               "r": "RED", "R": "LIGHTRED",
               "o": "ORANGE", "y": "YELLOW",
               "g": "GREEN", "G": "LIGHTGREEN",
               "c": "CYAN", "C": "LIGHTCYAN",
               "b": "BLUE", "B": "LIGHTBLUE",
               "m": "MAGENTA", "p": "PINK",
               "w": "WHITE", "W": "BRIGHTWHITE",
               "d": "DEFAULT", "-": "BLACK"}


class Dummy(object):
    def __init__(self, number="???"):
        self.number = number

    def __getattr__(self, *args, **kwargs):
        global WARNING_USED
        if not WARNING_USED:
            error_list.add(self.number,
                           "Warning: using Dummy class in place of CuPT")
            WARNING_USED = True
        return self

    def __call__(self, *args, **kwargs):
        return self


class Page(object):
    def __init__(self, number):
        self.reveal_status = False
        self.enabled = True
        self.index_num = None
        self.tagline = config.NAME + ": The World at Your Fingertips"
        self.importance = 2
        self.number = str(number)
        self.loaded = False
        self.background_loaded = False
        self.background_error = None
        self.title = ""
        self.duration_sec = config.default_page_duration_sec
        self.exception = None
        self.cupt = Dummy(self.number)

    def plot(self, *args, **kwargs):
        from ceefax.ceegraph import plot as ceeplot
        ceeplot(self, *args, **kwargs)

    def move_cursor(self, x=None, y=None):
        self.cupt.move_cursor(x=x, y=y)

    def start_fg_color(self, color):
        self.cupt.start_fg_color(color)

    def start_bg_color(self, color):
        self.cupt.start_bg_color(color)

    def start_random_fg_color(self):
        from ceefax.cupt.cupt import non_dark_colors
        from random import choice
        self.cupt.start_fg_color(choice(non_dark_colors))

    def start_random_bg_color(self):
        from ceefax.cupt.cupt import non_dark_colors
        from random import choice
        self.cupt.start_bg_color(choice(non_dark_colors))

    def end_fg_color(self):
        self.cupt.end_fg_color()

    def end_bg_color(self):
        self.cupt.end_bg_color()

    def add_block(self, block, *args, **kwargs):
        bg = None
        if "bg" in kwargs:
            bg = kwargs["bg"]
        self.cupt.add_block(block, *args, bg=bg)

    def add_title(self, title, bg="BLUE", fg="YELLOW", font="size7", pre=0,
                  fill=True, max_width=config.WIDTH):
        if fg in color_codes:
            fg = color_codes[fg]
        if bg in color_codes:
            bg = color_codes[bg]
        prinstance = get_font(font)
        title_block = prinstance.text_to_ascii(title, fill=fill,
                                               max_width=max_width)
        self.cupt.add_blocked_block(title_block, fg=fg, bg=bg, pre=pre)

    def add_rainbow_title(self, title, font="size7", pre=0, fill=True):
        prinstance = get_font(font)
        title_block = prinstance.text_to_ascii(title, fill=fill)
        self.cupt.add_blocked_block(title_block, rainbow=True, pre=pre)

    def add_text(self, text, fg=None, bg=None):
        if fg in color_codes:
            fg = color_codes[fg]
        if bg in color_codes:
            bg = color_codes[bg]
        if fg is not None:
            self.start_fg_color(fg)
        if bg is not None:
            self.start_bg_color(bg)
        self.cupt.add_text(text)
        if fg is not None:
            self.end_fg_color()
        if bg is not None:
            self.end_bg_color()

    def add_reveal_text(self, text, fg=None, bg=None, show=False,
                        wrapping=False):
        if fg in color_codes:
            fg = color_codes[fg]
        if bg in color_codes:
            bg = color_codes[bg]
        if fg is not None:
            self.start_fg_color(fg)
        if bg is not None:
            self.start_bg_color(bg)
        self.cupt.add_reveal_text(text, show, wrapping=wrapping)
        if fg is not None:
            self.end_fg_color()
        if bg is not None:
            self.end_bg_color()

    def add_unreveal_text(self, *args, **kwargs):
        self.add_reveal_text(*args, show=True, **kwargs)

    def toggle_reveal(self):
        if self.reveal_status:
            self.reveal_status = False
            self.cupt.reveal()
        else:
            self.reveal_status = True
            self.cupt.unreveal()

    def add_rainbow_text(self, text):
        from ceefax.cupt.cupt import non_dark_colors
        from random import choice
        for c in text:
            self.start_fg_color(choice(non_dark_colors))
            self.cupt.add_text(c)
        self.end_fg_color()

    def add_newline(self):
        self.cupt.add_newline()

    def add_wrapped_text(self, text, pre=0, fg=None, bg=None):
        if fg in color_codes:
            fg = color_codes[fg]
        if bg in color_codes:
            bg = color_codes[bg]
        if fg is not None:
            self.start_fg_color(fg)
        if bg is not None:
            self.start_bg_color(bg)
        self.cupt.add_text(text, True, pre=pre)
        if fg is not None:
            self.end_fg_color()
        if bg is not None:
            self.end_bg_color()

    def print_image(self, image, y_coord=0, x_coord=0):
        self.move_cursor(y=y_coord, x=x_coord)
        lines = image.split("\n")
        for l in range(len(lines) // 2):
            for c in range(len(lines[2 * l])):
                c1 = lines[2 * l][c]
                try:
                    c2 = lines[2 * l + 1][c]
                except:
                    c2 = "k"
                self.start_fg_color(color_codes[c1])
                self.start_bg_color(color_codes[c2])
                self.add_text(u"\u2580")
                self.end_bg_color()
                self.end_fg_color()
            self.move_cursor(y=y_coord + l + 1, x=x_coord)

    def four_to_one(self, four):
        n = {i: 0 for i in color_codes}
        for i in four:
            if i not in n:
                i = "-"
            n[i] += 1
        m1 = None
        m2 = None
        for tot in range(4, 0, -1):
            ls = [i for i in n if n[i] == tot]
            if len(ls) > 0 and m1 is None:
                m1 = ls[0]
                ls = ls[1:]
            if len(ls) > 0 and m2 is None:
                m2 = ls[0]
                break
        if m2 is None:
            m2 = "-"
        if m1 == "-":
            m1, m2 = m2, m1

        char = ""
        for i in four:
            if i == m1:
                char += "1"
            else:
                char += "0"
        char = self.get_char(char)

        return char, color_codes[m1], color_codes[m2]

    def get_char(self, char):
        """Note: this returns a number when the character won't display
        on a pi."""
        if char == "0001":
            char = "0011"
        if char == "0010":
            char = "0011"
        if char == "0100":
            char = "1100"
        if char == "1000":
            char = "1100"
        if char == "0110":
            char = "1100"
        if char == "1001":
            char = "0011"
        if char == "0111":
            char = "1111"
        if char == "1011":
            char = "1111"
        if char == "1101":
            char = "1111"
        if char == "1110":
            char = "1111"
        if char == "0011":
            return u"\u2584"
        if char == "0101":
            return u"\u2590"
        if char == "1010":
            return u"\u258C"
        if char == "1100":
            return u"\u2580"
        if char == "1111":
            return u"\u2588"
        return " "

    def print_compressed_image(self, image, y_coord=0, x_coord=0):
        self.move_cursor(y=y_coord, x=x_coord)
        lines = image.split("\n")
        for l in range(0, len(lines), 2):
            self.move_cursor(y=y_coord + l // 2, x=x_coord)
            for c in range(0, len(lines[l]), 2):
                four = ""
                for A in [l, l + 1]:
                    for B in [c, c + 1]:
                        if len(lines) > A and len(lines[A]) > B:
                            four += lines[A][B]
                        else:
                            four += "-"
                char, fg, bg = self.four_to_one(four)
                self.start_fg_color(fg)
                self.start_bg_color(bg)
                self.add_text(char)
                self.end_bg_color()
                self.end_fg_color()

    def width_of_word(self, word,font="size4"):
        if font=="size7":
            width = len(word)*7 \
            - sum(map(word.count, u"|"))*6 \
            - sum(map(word.count, u"'"))*5 \
            - sum(map(word.count, u"I!:."))*4 \
            - sum(map(word.count, u"1()-#&"))*3 \
            - sum(map(word.count, u"LJ/"))*1 \
            + sum(map(word.count, u"N"))*1 \
            + sum(map(word.count, u"WM"))*2
        else:
            width = len(word)*5 \
            - sum(map(word.count, u"|"))*4 \
            - sum(map(word.count, u"!:,‘’.'I’"))*3 \
            - sum(map(word.count, u"-()1"))*2 \
            - sum(map(word.count, u"T"))*1 \
            + sum(map(word.count, u"MW"))*1 \
            - sum(map(word.count, u"il"))*3 \
            - sum(map(word.count, u"fjt"))*2 \
            - sum(map(word.count, u"abcdeghknopqrsuvxyz"))*1 \
            + sum(map(word.count, u"mw"))*1
        return width

    def center_pad(self,center,chars_left,right=False):
        if center:
            if right:
                return ((chars_left+2)//2 + (chars_left+2)%2)*"|"
            else:
                return ((chars_left+2)//2)*"|"
        else:
            return ""

    def add_title_wrapped(self, text, max_width=config.WIDTH, bg="YELLOW",
                          fg="BLACK", font="size4", fill=True, pre=0,
                          center=False):
        chars_left = max_width
        line = ""
        text = text.split(" ")
        first_line = True
        for word in text:
            if chars_left - self.width_of_word(word,font) <= 0 and not first_line:
                # Print old line and start new line.
                self.add_title(self.center_pad(center, chars_left) + line[:-1],
                               bg=bg, fg=fg, font=font, fill=fill, pre=pre)
                chars_left = max_width
                line = word + " "
            else:
                # Add word to line
                line = line + word + " "
                first_line = False
            chars_left = chars_left - self.width_of_word(word,font) - 3
        # Print final line.
        self.add_title(self.center_pad(center, chars_left) + line[:-1] + self.center_pad(center,chars_left,right=True),
                       bg=bg, fg=fg, font=font, fill=fill, pre=pre)

    def loop(self):
        pass

    def keyboard_handler(self):
        pass

    def now(self):
        return config.now()

    background = None
    # Define this function to run something every so often in the background.
    # Use it for (eg) downloading weather data.

    def generate_content(self):
        """This function will be run every time the page is loaded."""
        pass

    def show(self):
        self.cupt.show_page_number(self.number)
        self.cupt.show_tagline(self.tagline)
        self.cupt.show()

    def reload(self):
        self.cupt.clear_content()
        self.generate_content()

    def as_html(self):
        try:
            self.background()
            self.generate_content()
            return self.cupt.as_html()
        except:
            return "Error loading page..."
