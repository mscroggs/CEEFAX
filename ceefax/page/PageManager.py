import random
from ceefax import config
import os
from ceefax.page import Page
import signal
import curses
from ceefax.error import error_list
from ceefax.error.exceptions import ConfigError, PageError, TimeUp
import traceback

try:
    from imp import reload
except:
    pass


def alarm(signum, frame):
    raise TimeUp


def pass_f(signum, frame):
    pass


def is_page_file(f):
    if f[0] == "_":
        return False
    if f[-2:] != "py":
        return False
    if config.pages_dir is not None:
        if os.path.isfile(os.path.join(config.pages_dir, f)):
            return True
    if config.ceefax_lib_pages is not None:
        if os.path.isfile(os.path.join(config.ceefax_lib_pages, f)):
            return True
    return False


def get_chr(ip):
    if 48 <= ip <= 57 or 65 <= ip <= 90 or 97 <= ip <= 122:
        return chr(ip)
    return ""


class PageManager:
    def __init__(self, screen):
        self.loads = 0
        self.current_page = None
        self.pages = {}
        self.screen = screen
        self.load_all_pages()

    def load_all_pages(self):
        self.load_folder(config.ceefax_lib_pages, "ceefax.pages")
        if config.pages_dir is not None:
            self.load_folder(config.pages_dir, "pages")

    def load_folder(self, folder, import_name):
        if not os.path.exists(folder):
            raise ConfigError("The pages folder doesn't exist:"
                              " " + folder)
        only_page_files = [f for f in os.listdir(folder)
                           if is_page_file(f)]
        for page_file in only_page_files:
            page_file_no_ext = os.path.splitext(page_file)[0]
            module = getattr(__import__(import_name,
                                        fromlist=[page_file_no_ext]),
                             page_file_no_ext)
            reload(module)
            for filename in dir(module):
                obj = getattr(module, filename)
                if isinstance(obj, Page):
                    obj.cupt = self.screen.cupt
                    self.add(obj)
                elif isinstance(obj, list):
                    for thing in obj:
                        if isinstance(thing, Page):
                            thing.cupt = self.screen.cupt
                            self.add(thing)

    def add(self, page):
        if page.number in self.pages:
            raise PageError("Page " + page.number + " already exists "
                            "(" + self.pages[page.number].title + " "
                            "and " + page.title + ")")
        self.pages[page.number] = page

    def get_loaded_random(self):
        page = self.build(FailPage)
        self.loads += 1
        while not page.loaded or not page.background_loaded:
            page = random.choice(self.get_enabled_pages(
                random.randrange(1, 6)))
            if page.background_loaded:
                page.loaded = False
                try:
                    page.reload()
                    page.loaded = True
                except:
                    pass
        return page

    def print_all(self):
        for page_num, page in self.sorted_pages():
            p = ""
            if not page.enabled:
                p += "\033[31m"
            p += (page_num + " ")
            p += (page.title)
            if not page.enabled:
                p += "\033[0m"
            print(p)

    def sorted_pages(self):
        items = list(self.pages.items())
        items.sort()
        return items

    def index_pages(self):
        items = [page for page in self.pages.values()
                 if page.index_num is not None]
        items.sort(key=lambda x: x.index_num)
        return items

    def export_all_to_html(self):
        from helpers.file_handler import open_html
        for page_num, page in self.sorted_pages():
            page.cupt.ls = []
            print(page_num + " " + page.title)
            with open_html(page_num + ".html", "w") as f:
                f.write(page.as_html())
        js = "taglines = {"
        js += ",".join(['"' + str(page_num) + '":"' + page.tagline + '"'
                        for page_num, page in self.sorted_pages()])
        js += "}\npages_on=Array("
        js += ",".join(['"' + str(page_num) + '"' for page_num, page
                        in self.sorted_pages() if page.enabled])
        js += ")"
        with open_html("info.js", "w") as f:
            f.write(js)

    def get_enabled_pages(self, importance=1):
        output = [page for page in self.pages.values()
                  if page.enabled and page.importance >= importance]
        if len(output) > 0:
            return output
        elif importance > 0:
            return self.get_enabled_pages(importance - 1)
        else:
            return [page for page in self.pages.values() if page.enabled]

    def page_exists(self, page_num):
        if page_num in self.pages:
            return True

        return False

    def background_loop(self):
        from time import sleep
        while True:
            for page in self.pages.values():
                try:
                    page.background_error = None
                    if page.background is not None:
                        page.background_loaded = False
                        page.background()
                    page.background_loaded = True
                except Exception as e:
                    error_list.add(e, page.number)
                    page.background_error = e
            sleep(60 * 30)

    def start_loop(self, test=None):
        try:
            import thread
        except ImportError:
            import _thread as thread
        for page in self.pages.values():
            if page.background is None:
                page.background_loaded = True
        if test is not None:
            page = self.pages[test]
            try:
                page.background_error = None
                if page.background is not None:
                    page.background_loaded = False
                    page.background()
                page.background_loaded = True
            except Exception as e:
                error_list.add(e, page.number)
                page.background_error = e
        thread.start_new_thread(self.background_loop, ())
        self.main_loop()

    def main_loop(self):
        inp = "100"
        while True:
            self.clear_input()
            if inp is not None:
                page = self.handle_input(inp)
            else:
                page = self.get_loaded_random()
            self.show(page)
            signal.signal(signal.SIGALRM, alarm)
            signal.alarm(30)
            try:
                key = None
                inp = ""
                while key != curses.KEY_ENTER and key != 10:
                    key = self.screen.getch()
                    try:
                        if key == 43:
                            self.current_page.toggle_reveal()
                        elif key == 263:
                            inp = inp[:-1]
                        else:
                            inp += get_chr(key)
                        self.show_input(inp)
                    except ValueError:
                        pass
                signal.alarm(0)
                signal.signal(signal.SIGALRM, pass_f)
            except TimeUp:
                inp = None

    def build(self, ThePage, *args, **kwargs):
        page = ThePage(*args, **kwargs)
        page.cupt = self.screen.cupt
        return page

    def handle_input(self, the_input):
        if the_input == "1337":
            import update
            update.git_pull()

        try:
            while len(the_input) < 3:
                the_input = "0" + str(the_input)
            return self.pages[the_input]
        except KeyError:
            return self.build(FailPage, "Page " + the_input + " does "
                              "not exist. Try the index in page 100.")

    def show(self, page):
        self.current_page = page
        self.screen.cupt.show_loading()
        if not isinstance(page, FailPage):
            if page.background_error is not None:
                page = self.build(FailPage, "There was an error running "
                                  "page " + page.number + "'s background "
                                  "function.\n\n" + str(page.background_error))
            elif page.number != "100" and not page.background_loaded:
                page = self.build(FailPage, "Page " + page.number + ""
                                  " currently updating. "
                                  "Please try again in a few minutes")
        try:
            page.loaded = False
            page.reload()
            page.loaded = True
            page.show()
        except Exception as e:
            error_list.add(e, page)
            page = self.build(FailPage, e, trace=traceback.format_exc())
            page.reload()
            page.loaded = True
            page.show()

    def show_input(self, i):
        pad = curses.newpad(1, config.WIDTH)
        pad.addstr(0, 0, i[:config.WIDTH - 1])
        pad.refresh(0, 0, config.HEIGHT - 1,
                    0, config.HEIGHT - 1, config.WIDTH)

    def clear_input(self):
        self.show_input(" " * config.WIDTH)


class FailPage(Page):
    def __init__(self, e=None, trace=""):
        super(FailPage, self).__init__("---")
        self.ee = None
        self.set_exception(e)
        self.enabled = False
        self.duration_sec = 2
        self.trace = trace

    def generate_content(self):
        self.add_text("Page failed to load...")
        self.add_newline()
        self.add_newline()

        if self.ee is None:
            self.add_text("UNKNOWN ERROR")
        elif type(self.ee) == str:
            self.add_wrapped_text(self.ee)
        else:
            self.add_wrapped_text(str(self.ee))
        self.add_newline()
        self.add_wrapped_text(self.trace)

    def set_exception(self, e):
        self.ee = e
