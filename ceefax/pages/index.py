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
        i = 0
        _items = Ceefax().page_manager.sorted_pages()
        for num, page in _items:
            if page.enabled and page.index_num is not None:
                self.add_text(page.index_num, fg="MAGENTA")
                self.add_text(" " + page.title)
                if i == 0:
                    self.move_cursor(x=36)
                    i = 1
                else:
                    self.add_newline()
                    i = 0


i_p = IndexPage("100")
