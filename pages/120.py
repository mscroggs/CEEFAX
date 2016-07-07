#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from printer import size4_instance as size4_printer
from time import strftime
import screen


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "Patronus"
        self.tagline = "EXPECTO PATRONUM!"

    def generate_content(self):
        import random
        squirrel = u"""
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
        chicken = """     ,~.
   ,-'__ `-,
  {,-'  `. }              ,')
 ,( a )   `-.__         ,',')~,
<=.) (         `-.__,==' ' ' '}
  (   )                      /)
   `-'\   ,                    )
       |  \        `~.        /
       \   `._        \      /
        \     `._____,'    ,'
         `-.             ,'
            `-._     _,-'
                77jj'
               //_||
            __//--'/`         
          ,--'/`  '"""
        
        cat = """                 .-.   _                __
                `  )`'-,`\        .-''``.-'
   _.-''-.      _.'       `'--._.' ,-'  /
   `\    _`'--'`                      .'
     '._ _`-       .--.   .--.      (`
        `.'       /    '.'    \      '.
       .'         \  0  |  0  /        '.
      /   _        '._.---._.'      _    \
      /    `'-.      (     )    .-'`     \
      / .---'_.   .   `-,-`  .  ._'---.  \
      |   -'`   .       |      .  `'-    |
      /_       .   '   /;\  '    .     ,_\
        '-.     '-..-`( ' )`-..-'     /
           '._         '-'         _.'
              '-..,__       __,..-'
                     `'---'`"""
                     
        magpie = """                                                 ,::::.._
                                               ,':::::::::.
                                           _,-'`:::,::(o)::`-,.._
                                        _.', ', `:::::::::;'-..__`.
                                   _.-'' ' ,' ,' ,\:::,'::-`'''
                               _.-'' , ' , ,'  ' ,' `:::/
                         _..-'' , ' , ' ,' , ,' ',' '/::
                 _...:::'`-..'_, ' , ,'  , ' ,'' , ,'::|
              _`.:::::,':::::,'::`-:..'_',_'_,'..-'::,'|
      _..-:::'::,':::::::,':::,':,'::,':::,'::::::,':::;
        `':,'::::::,:,':::::::::::::::::':::,'::_:::,'/
        __..:'::,':::::::--''' `-:,':,':::'::-' ,':::/
   _.::::::,:::.-''-`-`..'_,'. ,',  , ' , ,'  ', `','
 ,::SSt:''''`                 \:. . ,' '  ,',' '_,'
                               ``::._,'_'_,',.-'
                                   \\ \\
                                    \\_\\
                                     \\`-`.-'_
                                  .`-.\\__`. ``
                                     ``-.-._"""

        giraffe = """             .-.  .-.
             |  \/  |
            /,   ,_  `'-.
          .-|\   /`\     '.
        .'  0/   | 0\  \_  `".
     .-'  _,/    '--'.'|#''---'
      `--'  |       /   \#
            |      /     \#
            \     ;|\    .\#
            |' ' //  \   ::\#
            \   /`    \   ':\#
             `"`       \..   \#
                        \::.  \#
                         \::   \#
                          \'  .:\#
                           \  :::\#
                            \  '::\#
                             \     \#
                              \ """

              
        wombat = '''                               ,.--""""--.._
                             ."     .'      `-.
                            ;      ;           ;
                           '      ;             )
                          /     '             . ;
                         /     ;     `.        `;
                       ,.'     :         .     : )
                       ;|\'    :      `./|) \  ;/
                       ;| \"  -,-   "-./ |;  ).;
                       /\/              \/   );
                      :                 \    ;
                      :     _      _     ;   )
                      `.   \;\    /;/    ;  /
                        !    :   :     ,/  ;
                         (`. : _ : ,/""   ;
                          \\\`"^" ` :    ;
                                   (    )
                                   //// '''
        
        kestral = '''((
\\``.
\_`.``-. 
( `.`.` `._  
 `._`-.    `._ 
   \`--.   ,' `. 
    `--._  `.  .`. 
     `--.--- `. ` `. 
         `.--  `;  .`._ 
           :-   :   ;. `.__,.,__ __ 
            `\  :       ,-(     ';o`>.
              `-.`:   ,'   `._ .:  (,-`,
                 \    ;      ;.  ,: 
             ,"`-._>-:        ;,'  `---.,---.
             `>'"  "-`       ,'   "":::::".. `-.
              `;"'_,  (\`\ _ `:::::::::::'"     `---.
               `-(_,' -'),)\`.       _      .::::"'  `----._,-"")
                   \_,': `.-' `-----' `--;-.   `.   ``.`--.____/ 
                     `-^--'                \(-.  `.``-.`-=:-.__)
                                            `  `.`.`._`.-._`--.)
                                                 `-^---^--.`-- '''
        
        fox = '''                                                            ,-,
                                                      _.-=;~ /_
                                                   _-~   '     ;.
                                               _.-~     '   .-~-~`-._
                                         _.--~~:.             --.____88
                              ____...-~~~. .' .  .        _..-------~~
                     _..--~~~~        .' .'             ,'
                 _.-~                 .       .     ` ,'
               .'                             :.    ./
             .:     ,/          `            ::.   ,'
           .:'     ,(            ;.         ::. ,-'
          .'     ./'.`.     . . /:::..... _/:.o/
         /     ./'. . .)  . _.,'        `88;?88|
       ,'  . .,/'._,-~ /_.o8P'           88P ?8b
    _,'' . .,/',-~    d888P'             88'  88|
 _.'~  . .,:oP'        ?88b          --- 88.--'8b.--..__
:     ...' 88o __,------.88o ...__...    `~~   `~~      ~-.
`.;;;:='    ~~            ~~~         ~-    -       -   - '''

        
        elephant = '''              ___.-~"~-._   __....__
            .'    `    \ ~"~        ``-.
           /` _      )  `\              `\
          /`  a)    /     |               `\
         :`        /      |                 \
    <`-._|`  .-.  (      /   .            `;\\
     `-. `--'_.'-.;\___/'   .      .       | \\
  _     /:--`     |        /     /        .'  \\
 ("\   /`/        |       '     '         /    :`;
 `\'\_/`/         .\     /`~`=-.:        /     ``
   `._.'          /`\    |      `\      /(
                 /  /\   |        `Y   /  \
                J  /  Y  |         |  /`\  \
               /  |   |  |         |  |  |  |
              "---"  /___|        /___|  /__|
                     '"""         '"""  '""" '''
                     
        hyena = '''                     /
                 _,     _,
                /)|    /)\
                \_'-"`/(_/```",,
                  /   <        ``--._
                  |. _ )     `    *  ',
                  ^  ^/_,     *     (\*\
                  (#_/  `\)  /'  * - ))_|
                   U      \  \*   _,//_ *
                           ) >\_* ((|\_/
                           \ | \  | # (
                            \#  \#\ \ #
                             \\  \(  )/
                             _)> _))/(_
                   .-\\,, , /\\//\//\\/),, ,,)/
                     ,\.        .-    -'-,)\/.')) '''
 
        
        j = random.choice(range(10))
        title = ["Chunxin","Sam","Anna","Huda","Raf","Scroggs","Pietro","Ginbelg","Olly","Adam"][j]
        picture = [squirrel,chicken,cat,magpie,giraffe,wombat,kestral,fox,elephant,hyena][j]
        
        
        content = colour_print(size4_printer.text_to_ascii(title,fill=True),
                                self.colours.Background.BLUE, self.colours.Foreground.MAGENTA+self.colours.Style.BOLD)
        content += "\n"
        content += picture
        self.content = content



page = JigPage("120")
