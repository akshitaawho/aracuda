import mysql.connector
import random
import pygame
import sys
import math

# start menu
pygame.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode([WIDTH, HEIGHT])
WORD_FONT = pygame.font.SysFont('black owl', 45)
TITLE_FONT = pygame.font.SysFont('blood thirst', 70)
pygame.display.set_caption('Arcade')
BG = pygame.transform.scale(pygame.image.load('bg1.jpg'), (WIDTH, HEIGHT))
WIDTH, HEIGHT = 900, 500
WIN.blit(BG, (0, 0))
start_surface = WORD_FONT.render("Press A to play jumbled words", True, (255, 255, 255))
start2_surface = WORD_FONT.render("Press B to play Battleship", True, (255, 255, 255))
start3_surface = TITLE_FONT.render("WELCOME TO ARKADE", True, (255, 204, 221))
start3_surface_shadow = TITLE_FONT.render("WELCOME TO ARKADE", True, (170, 0, 255))
WIN.blit(start3_surface_shadow, (50 + 50, 100))
WIN.blit(start3_surface, (50 + 50, 104))
WIN.blit(start_surface, (50, 250))
WIN.blit(start2_surface, (50, 300))
pygame.display.flip()
running = True
quit = False
choice = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                choice = "jumbled"
                running = False
            if event.key == pygame.K_b:
                choice = "battle"
                running = False
            else:
                Start = False
        if event.type == pygame.QUIT:
            quit = True
            running = False

Start = True
if choice == "jumbled":
    # window 1
    pygame.init()
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode([WIDTH, HEIGHT])
    WORD_FONT = pygame.font.SysFont('ailerons', 45)
    SECOND_FONT = pygame.font.SysFont('ailerons', 30)
    THIRD_FONT = pygame.font.SysFont('chiller', 70)
    pygame.display.set_caption('Jumbled_words')
    BG = pygame.transform.scale(pygame.image.load('bg1.jpg'), (WIDTH, HEIGHT))
    WIDTH, HEIGHT = 900, 500

    quit_rect = pygame.Rect(0, 0, 900, 50)

    line1_surface = WORD_FONT.render("""Help our brave fighter by""", True, (0, 0, 0))
    line1_surface_white = WORD_FONT.render("""Help our brave fighter by""", True, (255, 255, 255))
    line2_surface = WORD_FONT.render("""solving these rounds...""", True, (0, 0, 0))
    line2_surface_white = WORD_FONT.render("""solving these rounds...""", True, (255, 255, 255))
    # line3_surface = SECOND_FONT.render("""(You can quit anytime by pressing x)""", True, (0, 0, 0))
    line3_surface_white = SECOND_FONT.render("""(You can quit anytime by pressing x)""", True, (255, 255, 255))
    line4_surface = THIRD_FONT.render("""Press Spacebar to Play!""", True, (255, 255, 255))
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, (0, 0, 0), quit_rect)
    WIN.blit(line1_surface, (60, 150))
    WIN.blit(line1_surface_white, (62, 150))
    WIN.blit(line2_surface, (60, 200))
    WIN.blit(line2_surface_white, (62, 200))
    WIN.blit(line3_surface_white, (145, 10))
    WIN.blit(line4_surface, (60, 300))
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
    # print(Start)
    # print(quit)
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
            # print(level)
            mycursor.execute("Select*from " + str(level) + " where sno=" + str(num))
            row = mycursor.fetchall()
            # print(level)
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
                round_surface = ROUND_FONT.render("Round: " + str(num), True, (255, 255, 255))
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
        # print(SCORE)
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
elif choice == 'battle':
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Battleship")
    icon = pygame.image.load('battleship.png')
    pygame.display.set_icon(icon)

    playerImg = pygame.image.load('mainchar.png')
    playerX = 370
    playerY = 480
    playerX_change = 0

    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 5

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('enem.png'))
        enemyX.append(random.randint(0, 735))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(0.3)
        enemyY_change.append(40)

    bulletImg = pygame.image.load('bulle.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 5
    # ready means can't see bullet = under the ship and fire means moving
    bullet_state = "ready"

    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 28)

    textX = 10
    textY = 10

    over_font = pygame.font.Font('freesansbold.ttf', 50)


    def show_score(x, y):
        score = font.render("Score :" + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))


    def game_over_text():
        over_text = over_font.render("GAME OVER...", True, (255, 255, 255))
        screen.blit(over_text, (100, 200))


    def player(x, y):
        screen.blit(playerImg, (x, y))


    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))


    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 5, y + 8))


    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
        # distance formula
        if distance < 27:
            return True
        else:
            return False


    BG = pygame.transform.scale(pygame.image.load('bgg.jpg'), (WIDTH, HEIGHT))
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(100)
        screen.blit(BG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if a keystroke is pressed check whether left or right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -2
                if event.key == pygame.K_RIGHT:
                    playerX_change = 2
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        # return to battleship coordinate
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # checking boundaries and not letting it go out of boundary
        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        for i in range(num_of_enemies):

            # ending the game
            if enemyY[i] > 450:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 7

                enemyY += enemyY_change
            elif enemyX[i] >= 736:
                enemyX_change[i] = -7
                enemyY[i] += enemyY_change[i]

            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score_value += 10
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()
