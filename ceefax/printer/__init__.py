from .Printer import Printer
from .Printer import instance
from .Printer import thin_instance
from .Printer import extrathin_instance
from .Printer import size4_instance
from .Printer import size4bold_instance
from .Printer import size4mono_instance


def get_font(font):
    if font == "size7":
        return instance
    elif font == "size7condensed":
        return thin_instance
    elif font == "size7extracondensed":
        return extrathin_instance
    elif font == "size4":
        return size4_instance
    elif font == "size4bold":
        return size4bold_instance
    elif font == "size4mono":
        return size4mono_instance
    else:
        raise ValueError("Undefined font.")


font_list = ["size7", "size7condensed", "size7extracondensed", "size4",
             "size4bold", "size4mono"]
