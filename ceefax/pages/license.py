from ceefax.page import Page
from ceefax import config
from ceefax.helpers.file_handler import load_lib_file


class LiPage(Page):
    def __init__(self):
        super(LiPage, self).__init__("003")
        self.in_index = False
        self.enabled = False
        self.title = "License"

    def generate_content(self):
        self.add_title("License", font="size4")
        li = load_lib_file("LICENSE.txt")
        c = load_lib_file("contributors.txt").split("\n")
        while "" in c:
            c.remove("")
        li = li.replace("The " + config.NAME + " contributors", ", ".join(c))
        self.add_wrapped_text(li)


sub_page = LiPage()
