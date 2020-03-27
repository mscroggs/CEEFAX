from ceefax.printer import get_font, font_list
import pytest


@pytest.mark.parametrize("fontname", font_list)
def test_fonts(fontname):
    font = get_font(fontname)
    text = font.text_to_ascii("Hello! ")
    assert isinstance(text, str)
