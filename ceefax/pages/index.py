from ceefax.page import Page
from ceefax import config
from ceefax import Ceefax


class IndexPage(Page):
    def __init__(self, n):
        super(IndexPage, self).__init__(n)
        self.importance = 5
        self.title = "Index"

    def generate_content(self):
        self.print_image(config.title, 1)
        self.add_newline()
        self.add_text(" INDEX  " * 10, fg="GREEN")
        self.add_newline()
        self.add_newline()
        for i, page in enumerate(Ceefax().page_manager.index_pages()):
            self.add_text(page.index_num, fg="MAGENTA")
            if i % 2 == 0:
                self.move_cursor(x=9)
            else:
                self.move_cursor(x=45)
            self.add_text(page.title, fg="WHITE")

            if i % 2 == 0:
                self.move_cursor(x=36)
            else:
                self.add_newline()


i_p = IndexPage("100")
