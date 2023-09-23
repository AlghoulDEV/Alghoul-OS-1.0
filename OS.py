"""
--------------------------------------------------------------------------------------------------------------
All rights reversed [2023/2024] [Mahmoud Alghoul] and [alghoul DEV]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Alghoul OS"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
--------------------------------------------------------------------------------------------------------------
"""



























from datetime import datetime
from fnmatch   import  translate
from   time    import  *
from   random  import  * 
from turtle    import  *
from pyautogui import  *
from   pytube  import   YouTube
import pytube
from googletrans import Translator
sleep(0.6)
import pygame
import sys
import secret


def clear_screen():#the code that removes the text after the operation
    print("\033[H\033[J", end="")

clear_screen()
main_input = input('press enter key to boot up . . . ').lower
clear_screen()
sleep(1.2)


def click_card():
            pygame.init()

            back = (200, 255, 255) #background color
            mw = pygame.display.set_mode((500, 500)) #main window
            mw.fill(back)
            clock = pygame.time.Clock()
            class Area():
                def __init__(self, x=0, y=0, width=8, height=8, color=None):
                    self.rect = pygame.Rect(x, y, width, height) #rectangle
                    self.fill_color = color


                def color(self, new_color):
                    self.fill_color = new_color


                def fill(self):
                    pygame.draw.rect(mw, self.fill_color, self.rect)


                def outline(self, frame_color, thickness): #outline of an existing rectangle
                    pygame.draw.rect(mw, frame_color, self.rect, thickness)    
    
                def collidepoint(self, x, y):
                    return self.rect.collidepoint(x, y)


            class Label(Area):
               def set_text(self, text, fsize=9, text_color=(0, 0, 0)):
                   self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)


               def draw(self, shift_x=0, shift_y=0):
                   self.fill()
                   mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


            YELLOW = (255, 255, 0)
            DARK_BLUE = (0, 0, 100)
            BLUE = (80, 80, 255)
            GREEN = (0, 255, 0)
            RED = (255, 0, 0)

            cards = []
            num_cards = 4


            x = 50


            for i in range(num_cards):
               new_card = Label(x, 170, 70, 100, YELLOW)
               new_card.outline(BLUE, 10)
               new_card.set_text('CLICK', 20)
               cards.append(new_card)
               x = x + 100
            wait = 0


            while True:
                # for card in cards:
                #     card.draw(10, 30)

                if wait == 0:
                    wait = 20
                    click_location = randint(0, num_cards-1)
                    for i in range(num_cards):
                        cards[i].color(YELLOW)
                        if i == click_location:
                            cards[i].draw(10, 40)
                        else:
                            cards[i].fill()
                else:
                    wait -= 1
    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        clear_screen()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        x, y = event.pos
                        for i in range(num_cards):
                            if cards[i].collidepoint(x, y):
                                if i == click_location:
                                    cards[i].color(GREEN)
                                else:
                                    cards[i].color(RED)
                            cards[i].fill()
                




                pygame.display.update()
                clock.tick(30)

def draw_config():
        t = Turtle('circle')
        t.color('black')
        t.pensize(3)

        sc = t.getscreen()

        def draw(x, y):
            t.goto(x, y)

        t.ondrag(draw)

        def move(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        sc.onscreenclick(move)

        sc.listen()

        # controls
        def k_up():
            t.setheading(90)
            t.forward(10)

        def k_down():
            t.setheading(270)
            t.forward(10)

        def k_left():
            t.setheading(180)
            t.forward(10)

        def k_right():
            t.setheading(0)
            t.forward(10)#controls end 
    
        def boldp():
            t.pensize() + 1
        def boldm():
            t.pensize() + 1
        #colors -_-
        def red():  t.color('red')
        def green():    t.color('green')
        def blue():    t.color('blue')
        def yellow():   t.color('yellow')
        def blk():    t.color('black')
        def gray():    t.color('gray')
        def violet():   t.color('violet')
        #
        def fill1():
            t.begin_fill()
        def fill2():
            t.end_fill()
        #config
        sc.onkey(k_up, 'Up')
        sc.onkey(k_down, 'Down')
        sc.onkey(k_left, 'Left')
        sc.onkey(k_right, 'Right')
        sc.onkey(red, 'r')
        sc.onkey(green, 'g')
        sc.onkey(blue, 'b')
        sc.onkey(yellow, 'y')
        sc.onkey(blk, '0')
        sc.onkey(gray, '9')
        sc.onkey(violet, 'v')
        sc.onkey(fill1, '1')
        sc.onkey(fill2, '2')
        sc.onkey(boldp, '+')
        sc.onkey(boldm, '-')
        sc.mainloop()


def youtube_downloader(url, save_path):
    try:
        youtube = YouTube(url)

        video_stream = youtube.streams.get_highest_resolution()


        # Start downloading
        print(f"Downloading: {youtube.title}")
        sleep(4)

        video_stream.download(output_path=save_path)
        print(f"{youtube.title} Downlaoded")
        print(f"{youtube.title}: '{youtube.description}'")
        print(f"Video ID: {youtube.video_id}")
        
        
    #if there is Erorrs
    except Exception as e:
        print(f"An error occurred: {e}")
  

def start_menu():
    clear_screen()
    print('Alghoul OS \n')
    start = ['apps', 'games', 'settings']
    i = 1 
    for s in start:
       print(i, '-', s)
       i += 1
    print('4 - shutdown OS')

def apps():
    if main_input == '1' or main_input == 'apps':#from the start menu to apps
        clear_screen()
        print('<- back\n::::::::::::::::::::::::::::')
        print(':.apps.:')
        print('::::::::::::::::::::::::::::')
        apps = ['youtube installer', 'translator', 'symbol counter', 'randomizer', 'timer', 'auto sender', 'paint', 'calculator']
        i = 1 
        for app in apps:
           print(i, '-', app)
           i += 1
           

def settings():
    if main_input == '3' or main_input == 'settings':
        clear_screen()
        print('<- back\n::::::::::::::::::::::::::::')        
        print(':.settings.:')
        print('::::::::::::::::::::::::::::')
        settings = ['text color', 'languge', 'system info', 'copyright']
        e = 1 
        for setting in settings:
           print(e, '-', setting)
           e += 1

no_length = 20
serial_no = ''
for i in range(no_length):
    serial_no = serial_no + str(randint(0,9))

def settings_config():
    if main_input == '3' or main_input == 'settings':
        settings_input = input('>>> ')
        if settings_input == 'back' or settings_input == '<-':
            clear_screen()
            start_menu()
        if settings_input == '1' or settings_input == 'text color':
            clear_screen()
            print('<- back\n::::::::::::::::::::::::::::')
            print(':.text color display.:')
            print('::::::::::::::::::::::::::::')
            text_colors = ['deafult','blue','red','yellow','purple','cyan', 'green']
            k = 1 
            for color in text_colors:
               print(k, '-', color)
               k += 1
            text_color_setting = input('>>> ')

            if text_color_setting == '1':
                print("\033[0m")#deafult 
            if text_color_setting == '2':
                print("\033[34m")#blue
            if text_color_setting == '3':
                print("\033[31m")#red
            if text_color_setting == '4':
                print("\033[33m")#yellow
            if text_color_setting == '5':
                print("\033[35m")#purple
            if text_color_setting == '6':
                print("\033[36m")#cyan
            if text_color_setting == '7':
                print('\033[32m')
            start_menu()
        if settings_input == '2' or settings_input == 'languge':
            clear_screen()
            print('<- back\n::::::::::::::::::::::::::::')
            print(':.system languge.:')
            print('::::::::::::::::::::::::::::')
            print('Supported languges')
            print('ar - arabic (coming soon)')
            print('en - english(current)')
        if settings_input == '3' or settings_input == 'system info':
            clear_screen()
            print('<- back\n::::::::::::::::::::::::::::')
            print(':.system information.:')
            print('::::::::::::::::::::::::::::')
            print('OS name        | alghoulOS')
            print('OS version     | 1.0')
            print(f'Season number  | {serial_no}')
        if settings_input == '4' or settings_input == 'copyright':
            def copyright_os():
                print('''
Copyright ©️ (2023/2024) [Mahmoud ALghoul] and [Alghoul DEV]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (ALGHOUL OS), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.''')
            def copyright_os_2():
                print("\033[31m")
                print('''
THE SOFTWARE IS PROVIDED , WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.''')
                print("\033[0m")

            clear_screen()
            copyright_os()
            copyright_os_2()
        


def apps_config():
    #config 1
    if main_input == '1' or main_input == 'apps':
        apps_input = input('>>> ').lower()
        if apps_input == 'back' or apps_input == '<-':
            clear_screen()
            start_menu()
            
        #youtube installer config
        if apps_input == '1' or apps_input == 'youtube installer':
            clear_screen()
            print('<- back\n ::::::::::::::::::::::::::::')
            print(':.youtube video downloader.:')
            print('::::::::::::::::::::::::::::')
            video_url = input("enter the video URL: ")     
            save_folder = input("enter the path of the video: ")
            config_vid = input('sure? (y/n): ')
            if config_vid == 'y':
                youtube_downloader(video_url, save_folder)
            else:
                apps()
        #translator
        if apps_input == '2' or apps_input == 'text translator':
            clear_screen()
            print('<- back\n ::::::::::::::::::::::::::::')
            print(':.text translator.:')
            print('::::::::::::::::::::::::::::')
            
            translator = Translator()
            text_translate = str(input("text :"))
            translate_languge = str(input('translate text to (en/fr/ar) and more: '))
            languages = ["en", "es", "fr", "de", "it", "pt", "nl", "ru", "zh-cn", "ja", "ko", "ar", "hi", "tr", "th", "sv", "fi", "pl", "da", "no", "cs", "el"]
            if translate_languge in languages:
                translated = translator.translate(text_translate, dest=translate_languge)
                clear_screen()
                print('<- back\n ::::::::::::::::::::::::::::')
                print(':.text translator.:')
                print('::::::::::::::::::::::::::::')
                print(f"Original Text: {text_translate}")
                print(f"Translated Text ({translated.dest}): {translated.text}")
        #symbol counter
        if apps_input == '3' or apps_input == 'symbol counter':
            clear_screen()
            print('<- back\n :::::::::::::::::::::::::::: ')
            print(':.symbol counter.:')
            print('::::::::::::::::::::::::::::')
            symbol = input('text :')
            symbol_2= len(symbol)
            symbol_3 = symbol_2 
            print(f"your text has {symbol_3} symbols")
        #randomizer
        if apps_input == '4' or apps_input == 'randomizer':
            clear_screen()
            print('<- back\n ::::::::::::::::::::::::::::')
            print(':.Randomizer.:')
            print('::::::::::::::::::::::::::::')
            random_range_inp = int(input('random range: '))                                                                                                 
            random_progress = randint(0, random_range_inp)
            print(f'number: {random_progress}')
        #timer
        if apps_input == '5' or apps_input == 'timer':
            clear_screen()
            print('<- back\n ::::::::::::::::::::::::::::')
            print(':.timer.:')
            print('::::::::::::::::::::::::::::')
            seconds = int(input('seconds: '))
            for i in range(seconds):
                print(seconds)
                sleep(1)
                seconds -= 1
        if apps_input == '6' or apps_input == 'auto sender':
            clear_screen()
            print('<- back\n ::::::::::::::::::::::::::::')
            print(':.auto sender.:')
            print('::::::::::::::::::::::::::::')
            print('before you start ?')
            print('sure ?! *this may be harmful')
            config_auto_sender = input('sure (y/n):')
            if config_auto_sender == 'y':
                auto_sender = input('text: ')
                times = int(input('times: '))
                for i in range(times):
                    write(auto_sender)
                    press('enter')
                    sleep(0.5)
                    
        if apps_input == '7' or apps_input == 'paint':
            clear_screen()
            print('<- back\n::::::::::::::::::::::::::::')
            print(':.paint.:')
            print('::::::::::::::::::::::::::::')
            print('How to use ?')
            print('1 - Draw -> Use arrows to draw')
            print('2 - Nevagate -> Click on any place on screen to nevagate')
            print('3 - fill shapes -> To start fill press(1), to end fill press(2)')
            print('4 - Change colors -> (R): red, (G): green, (B): blue, (Y): yellow, (0): blk, (V): violet')
            sleep(10)
            draw_config()
        if apps_input == '8' or apps_input == 'calculator':
            clear_screen()
            print('<- back\n::::::::::::::::::::::::::::')
            print(':.calculator.:')
            print('::::::::::::::::::::::::::::')
            first_no = float(input('first number: '))
            second_number = float(input('second number: '))
            operations = ['addition', 'subtraction', 'multiplication', 'division']
            q = 1 
            for op in operations:
               print(q, '-', op)
               q += 1
            op_input = input('operation: ')
            clear_screen()
            print('<- back\n::::::::::::::::::::::::::::')
            print(':.calculator.:')
            print('::::::::::::::::::::::::::::')
            if op_input == '<-' or op_input == 'back':
                start_menu()
            if op_input == '1':
                add = first_no + second_number
                print(first_no,'+',second_number,'=',add)
            if op_input == '2':
                sub = first_no - second_number
                print(first_no,'-',second_number,'=',sub)
            if op_input == '3':
                multi = first_no * second_number
                print(first_no,'×',second_number,'=',multi)
            if op_input == '4':
                divi = first_no / second_number
                print(first_no,'÷',second_number,'=',divi)
            
   

def games():
    if main_input == '2' or main_input == 'games':
        clear_screen()
        print('<- back\n::::::::::::::::::::::::::::')
        print(':.games.:')
        print('::::::::::::::::::::::::::::')
        l = 1 
        games = ['card clicker', 'guess the country']
        for game in games:
            print(l,'-',game)
            l += 1
        games_input = input('>>> ')
        if games_input == '<-' or games_input == 'back':
            start_menu()
        if games_input == '1' or games_input == 'card clicker':
            click_card()
        if games_input == '2' or games_input == 'guess the flag':
                clear_screen()
                print('<- back\n::::::::::::::::::::::::::::')
                print(':.guess the flag.:')
                print('::::::::::::::::::::::::::::')
                flag = str(input('flag: '))
                if flag == '<-' or flag == 'back':
                    start_menu()
                    
def main_program():
    start_menu()
    apps()
    apps_config()
    games()
    settings()
    settings_config()
    
# R U N 

clear_screen()
stop_forms = ['stop','0',0,'false','close','end','exit', 4,'4']

while main_input not in stop_forms:
    main_program()
    main_input = input('>>> ').lower()
    clear_screen()
    
sys.exit()
False
