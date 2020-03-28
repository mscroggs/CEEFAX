from .weather_symbols import weather_symbol
from .size7 import size7font
from .size7condensed import size7condensedfont
from .size7extracondensed import size7extracondensedfont
from .size4 import size4font
from .size4bold import size4boldfont
from .size4mono import size4monofont


def get_font(font):
    if font == "size7":
        return size7font
    elif font == "size7condensed":
        return size7condensedfont
    elif font == "size7extracondensed":
        return size7extracondensedfont
    elif font == "size4":
        return size4font
    elif font == "size4bold":
        return size4boldfont
    elif font == "size4mono":
        return size4monofont
    else:
        raise ValueError("Undefined font.")


font_list = ["size7", "size7condensed", "size7extracondensed", "size4",
             "size4bold", "size4mono"]
