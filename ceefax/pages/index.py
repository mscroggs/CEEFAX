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
        plist = []
        for num, page in Ceefax().page_manager.sorted_pages():
            if page.enabled and page.index_num is not None:
                plist.append((page.index_num, page.title))
        plist.sort(lambda x: x[0])
        for i, (num, title) in enumerate(plist):
            self.add_text((num + "         ")[:8] + title, fg="MAGENTA")
            if i % 2 == 0:
                self.move_cursor(x=36)
            else:
                self.add_newline()


i_p = IndexPage("100")
