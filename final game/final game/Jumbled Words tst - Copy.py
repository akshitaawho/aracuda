import mysql.connector
import random
import pygame
import sys



Start = True

# window 1
pygame.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode([WIDTH, HEIGHT])
WORD_FONT = pygame.font.SysFont('arial', 80)
SECOND_FONT = pygame.font.SysFont('arial', 40)
pygame.display.set_caption('Jumbled_words')
BG = pygame.transform.scale(pygame.image.load('Background_jumbled_words.png'), (WIDTH, HEIGHT))
WIDTH, HEIGHT = 900, 500

quit_rect = pygame.Rect(50, 250, 525, 50)


line1_surface = WORD_FONT.render("""Welcome to Jumbled words!""", True, (0, 0, 0))
line1_surface_white = WORD_FONT.render("""Welcome to Jumbled words!""", True, (255, 255, 255))
line2_surface = WORD_FONT.render("""There are 5 rounds...""", True, (0, 0, 0))
line2_surface_white = WORD_FONT.render("""There are 5 rounds...""", True, (255, 255, 255))
line3_surface = SECOND_FONT.render("""(You can quit anytime by pressing x)""", True, (0, 0, 0))
line3_surface_white = SECOND_FONT.render("""(You can quit anytime by pressing x)""", True, (255, 255, 255))
line4_surface = WORD_FONT.render("""Press Spacebar to Play!""", True, (255, 255, 255))
WIN.blit(BG, (0, 0))
pygame.draw.rect(WIN, (0, 0, 0), quit_rect)
WIN.blit(line1_surface, (50, 0))
WIN.blit(line1_surface_white, (52, 0))
WIN.blit(line2_surface, (50, 100))
WIN.blit(line2_surface_white, (52, 100))
WIN.blit(line3_surface_white, (54, 250))
WIN.blit(line4_surface, (50, 300))
pygame.display.flip()


running = True
quit = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
            else:
                Start = False
        if event.type == pygame.QUIT:
            quit = True
            running = False

# window 2
if quit != True:
    pygame.init()
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode([WIDTH, HEIGHT])
    SECOND_FONT = pygame.font.SysFont('arial', 50)
    pygame.display.set_caption('Jumbled_words')
    BG = pygame.transform.scale(pygame.image.load('Background_jumbled_words.png'), (WIDTH, HEIGHT))
    WIDTH, HEIGHT = 900, 500


    quit_rect = pygame.Rect(50, 250, 525, 50)
    level_surface = SECOND_FONT.render("""  Press H for hard level and E for easy level""", True, (255, 255, 255))
    WIN.blit(BG, (0, 0))
    WIN.blit(level_surface, (55, 300))
    pygame.display.flip()
    running = True
    level = ""
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    level = "hard"
                    running = False
                if event.key == pygame.K_e:
                    level = "easy"
                    running = False
            if event.type == pygame.QUIT:
                quit = True
                running = False
#print(Start)
#print(quit)
# game start
if Start == True and quit != True:
    pygame.init()

    def score_count(mylist):
        score = 0
        for k in mylist:
            if k == True:
                score += 1
        return score


    # sql part
    def jumble(word):
        while True:
            pre_jum = random.sample(word, len(word))
            jumbled = ''.join(pre_jum)
            if word != jumbled:
                return jumbled


    var1 = False
    var2 = False
    var3 = False
    var4 = False
    var5 = False
    mylist = [var1, var2, var3, var4, var5]
    mylist_new = []


    def jumbled_words(num, level):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234abcd@456", database="game_info")
        mycursor = mydb.cursor()
        #print(level)
        mycursor.execute("Select*from " + str(level) + " where sno=" + str(num))
        row = mycursor.fetchall()
        #print(level)
        ans = row[0][1]
        word = ans.upper()
        req_word = jumble(word)
        quest = req_word.upper()
        global l
        l = l + 1
        # pygame part
        WIDTH, HEIGHT = 900, 500
        WIN = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Jumbled Words")
        FPS = 60
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 255)
        WORD_FONT = pygame.font.SysFont('arial', 80)
        ROUND_FONT = pygame.font.SysFont('comicsans', 50)
        BG = pygame.transform.scale(pygame.image.load('Background_jumbled_words.png'), (WIDTH, HEIGHT))

        input_rect = pygame.Rect(350, HEIGHT // 2, 400, 100)
        question_rect = pygame.Rect(0, HEIGHT // 2 - 100, WIDTH, 100)

        def correct_or_wrong(USER_TEXT):
            if USER_TEXT.upper() == word:
                RESULT = "CORRECT!"
                pygame.time.delay(1000)
                global i
                i = True
                global mylist_new
                mylist_new.append(i)
                return True

        def score(USER_TEXT):
            SCORE = 0
            if USER_TEXT.upper() == word:
                SCORE += 1
            return SCORE

        def draw_window(USER_TEXT, RESULT, SCORE):
            WIN.blit(BG, (0, 0))

            pygame.draw.rect(WIN, WHITE, input_rect)
            pygame.draw.rect(WIN, WHITE, question_rect)
            question_text = WORD_FONT.render(quest, True, (0, 0, 0))
            result_text = WORD_FONT.render(RESULT, True, (0, 0, 0))
            text_surface = WORD_FONT.render(USER_TEXT.upper(), True, (0, 0, 0))
            round_surface = ROUND_FONT.render("Round: "+ str(num), True, (255, 255, 255))
            round_surface_black = ROUND_FONT.render("Round: " + str(num), True, (0, 0, 0))
            WIN.blit(question_text, (HEIGHT // 2 - 100, 160))
            WIN.blit(result_text, (400, 200))
            WIN.blit(round_surface_black, (0, 3))
            WIN.blit(round_surface, (0, 0))
            WIN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

            input_rect.w = max(100, text_surface.get_width() + 60)

            pygame.display.flip()

        def main():
            clock = pygame.time.Clock()
            USER_TEXT = ''
            RESULT = ''
            SCORE = 0

            while True:

                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()


                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            USER_TEXT = USER_TEXT[:-1]
                        else:
                            USER_TEXT += event.unicode
                    SCORE = score(USER_TEXT)

                draw_window(USER_TEXT, RESULT, SCORE)

                if correct_or_wrong(USER_TEXT):
                    global i
                    i = True
                    break
            pygame.quit()

        if __name__ == '__main__':
            main()


    numbers = [1, 2, 3, 4, 5]
    l = 1
    for i in mylist:
        score = 0
        if i == False:
            try:
                pygame.init()

                jumbled_words(l, level)
                score += 1
                i = True
            except:
                break

    SCORE = score_count(mylist_new)
    #print(SCORE)
    pygame.init()
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode([WIDTH, HEIGHT])
    WORD_FONT = pygame.font.SysFont('arial', 80)
    pygame.display.set_caption('Jumbled_words')
    BG = pygame.transform.scale(pygame.image.load('Background_jumbled_words.png'), (WIDTH, HEIGHT))
    WIDTH, HEIGHT = 900, 500
    SCORE_surface = WORD_FONT.render("Your score is: " + str(SCORE), True, (255, 255, 255))
    WIN.blit(BG, (0, 0))
    WIN.blit(SCORE_surface, (WIDTH / 2 - 225, HEIGHT / 2 + 100))
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
