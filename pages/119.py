#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime
import screen


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Squirrel"
        self.tagline = "As found in Belgin's garden"

    def generate_content(self):
        import random
        tit = random.choice(["Hazel","Wispy"])
		
        content = colour_print(printer.text_to_ascii(tit,fill=True,vertical_condense=True))
        content += "\n"
        content += self.colours.Foreground.YELLOW+u"""
          ¶¶¶¶¶¶¶¶¶¶¶
      ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶           ¶
        ¶¶¶¶¶¶             ¶¶¶¶      ¶¶¶¶  ¶¶
              ¶¶            ¶¶       ¶¶ ¶ ¶
             ¶¶¶          ¶¶¶     ¶¶¶¶    ¶¶
            ¶¶¶          ¶¶¶  ¶¶¶¶¶¶       ¶¶¶¶
          ¶¶¶          ¶¶¶¶¶¶¶¶¶              ¶¶
        ¶¶¶           ¶¶¶¶¶¶               ¶¶ ¶¶
      ¶¶¶            ¶¶¶¶                 ¶¶¶ ¶¶
     ¶¶¶            ¶¶¶¶             ¶¶¶      ¶¶
    ¶¶             ¶¶¶             ¶¶¶¶¶¶¶    ¶¶
   ¶¶             ¶¶¶                 ¶¶¶¶¶¶¶¶¶  ¶¶
  ¶¶              ¶¶                     ¶¶    ¶¶¶¶
  ¶¶             ¶¶¶               ¶¶¶     ¶¶¶¶¶  ¶
  ¶¶             ¶¶            ¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶  ¶
  ¶¶             ¶¶              ¶¶¶¶     ¶¶¶¶ ¶¶¶ ¶
  ¶             ¶¶                 ¶¶      ¶¶¶¶¶¶ ¶¶
  ¶¶            ¶¶                  ¶¶      ¶¶   ¶¶
  ¶¶            ¶¶                  ¶¶      ¶¶¶¶¶
    ¶        ¶¶¶¶¶                ¶¶¶¶¶¶¶
     ¶¶¶¶¶¶¶¶    ¶¶                   ¶¶
                 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶     
"""        
        self.content = content

page = JigPage("119")
