import pygame
import random
import time

pygame.init()

screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("두더지 잡기 게임")

clock = pygame.time.Clock()
start_time = int(time.time())
remain_time = 30
penalty_time = 0

score = 0

large_font = pygame.font.SysFont('malgungothic', 80)
small_font = pygame.font.SysFont('malgungothic', 40)

game_over = False

mole_image = pygame.image.load('mole.png')
moles = []
big_mole_image = pygame.image.load('big_mole.png')
big_moles = []
bomb_image = pygame.image.load('bomb.png')
bombs = []

for i in range(4):
    mole = mole_image.get_rect(left=random.randint(0, screen_width - mole_image.get_width()), top=random.randint(0, screen_height - mole_image.get_height() - 10))
    after_time = random.randint(0, 3)
    during_time = random.randint(1, 3)
    appear_time = int(time.time()) + after_time
    disappear_time = int(time.time()) + after_time + during_time
    moles.append((mole, appear_time, disappear_time))
for i in range(2):
    big_mole = big_mole_image.get_rect(left=random.randint(0, screen_width - big_mole_image.get_width()), top=random.randint(0, screen_height - big_mole_image.get_height() - 10))
    after_time = random.randint(0, 3)
    during_time = random.randint(1, 3)
    appear_time = int(time.time()) + after_time
    disappear_time = int(time.time()) + after_time + during_time
    big_moles.append((big_mole, appear_time, disappear_time))
for i in range(5):
    bomb = bomb_image.get_rect(left=random.randint(0, screen_width - bomb_image.get_width()), top=random.randint(0, screen_height - bomb_image.get_height() - 10))
    after_time = random.randint(0, 3)
    during_time = random.randint(1, 3)
    appear_time = int(time.time()) + after_time
    disappear_time = int(time.time()) + after_time + during_time
    bombs.append((bomb, appear_time, disappear_time))

while True:
    screen.fill('Black')

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
        print(event.pos[0], event.pos[1])
        for mole, appear_time, disappear_time in moles:
            if mole.collidepoint(event.pos):
                print(mole)
                moles.remove((mole, appear_time, disappear_time))
                mole = mole_image.get_rect(left=random.randint(0, screen_width - mole_image.get_width()), top=random.randint(0, screen_height - mole_image.get_height() - 10))
                after_time = random.randint(0, 3)
                during_time = random.randint(1, 3)
                appear_time = int(time.time()) + after_time
                disappear_time = int(time.time()) + after_time + during_time
                moles.append((mole, appear_time, disappear_time))
                score += 10
        for big_mole, appear_time, disappear_time in big_moles:
            if big_mole.collidepoint(event.pos):
                print(big_mole)
                big_moles.remove((big_mole, appear_time, disappear_time))
                big_mole = big_mole_image.get_rect(left=random.randint(0, screen_width - big_mole_image.get_width()), top=random.randint(0, screen_height - big_mole_image.get_height() - 10))
                after_time = random.randint(0, 3)
                during_time = random.randint(1, 3)
                appear_time = int(time.time()) + after_time
                disappear_time = int(time.time()) + after_time + during_time
                big_moles.append((big_mole, appear_time, disappear_time))
                score += 30
        for bomb, appear_time, disappear_time in bombs:
            if bomb.collidepoint(event.pos):
                print(bomb)
                bombs.remove((bomb, appear_time, disappear_time))
                bomb = bomb_image.get_rect(left=random.randint(0, screen_width - bomb_image.get_width()), top=random.randint(0, screen_height - bomb_image.get_height() - 10))
                after_time = random.randint(0, 3)
                during_time = random.randint(1, 3)
                appear_time = int(time.time()) + after_time
                disappear_time = int(time.time()) + after_time + during_time
                bombs.append((bomb, appear_time, disappear_time))
                score -= 50

    if not game_over:
        current_time = int(time.time())
        remain_time = 30 - (current_time - start_time) - penalty_time

        if remain_time <= 0:
            game_over = True
            for mole, appear_time, disappear_time in moles:
                current_time = int(time.time())
                if appear_time > current_time:
                    moles.remove((mole, appear_time, disappear_time))

            for big_mole, appear_time, disappear_time in big_moles:
                current_time = int(time.time())
                if appear_time > current_time:
                    big_moles.remove((big_mole, appear_time, disappear_time))

            for bomb, appear_time, disappear_time in bombs:
                current_time = int(time.time())
                if appear_time > current_time:
                    bombs.remove((bomb, appear_time, disappear_time))

        for mole, appear_time, disappear_time in moles:
            current_time = int(time.time())
            if current_time > disappear_time:
                moles.remove((mole, appear_time, disappear_time))
                mole = mole_image.get_rect(left=random.randint(0, screen_width - mole_image.get_width()), top=random.randint(0, screen_height - mole_image.get_height() - 10))
                after_time = random.randint(0, 3)
                during_time = random.randint(1, 3)
                appear_time = int(time.time()) + after_time
                disappear_time = int(time.time()) + after_time + during_time
                moles.append((mole, appear_time, disappear_time))

        for big_mole, appear_time, disappear_time in big_moles:
            current_time = int(time.time())
            if current_time > disappear_time:
                big_moles.remove((big_mole, appear_time, disappear_time))
                big_mole = big_mole_image.get_rect(left=random.randint(0, screen_width - big_mole_image.get_width()), top=random.randint(0, screen_height - big_mole_image.get_height() - 10))
                after_time = random.randint(0, 3)
                during_time = random.randint(1, 3)
                appear_time = int(time.time()) + after_time
                disappear_time = int(time.time()) + after_time + during_time
                big_moles.append((big_mole, appear_time, disappear_time))

        for bomb, appear_time, disappear_time in bombs:
            current_time = int(time.time())
            if current_time > disappear_time:
                bombs.remove((bomb, appear_time, disappear_time))
                bomb = bomb_image.get_rect(left=random.randint(0, screen_width - bomb_image.get_width()), top=random.randint(0, screen_height - bomb_image.get_height() - 10))
                after_time = random.randint(0, 3)
                during_time = random.randint(1, 3)
                appear_time = int(time.time()) + after_time
                disappear_time = int(time.time()) + after_time + during_time
                bombs.append((bomb, appear_time, disappear_time))

    for mole, appear_time, disappear_time in moles:
        current_time = int(time.time())
        if current_time >= appear_time:
            screen.blit(mole_image, mole)
            screen.blit(big_mole_image, big_mole)
            screen.blit(bomb_image, bomb)

    score_image = small_font.render('점수 {}'.format(score), True, 'yellow')
    screen.blit(score_image, (10, 10))

    remain_time_image = small_font.render('남은 시간 {}'.format(remain_time), True, 'yellow')
    screen.blit(remain_time_image, remain_time_image.get_rect(right=screen_width - 10, top=10))

    if game_over:
        game_over_image = large_font.render('게임 종료', True, 'red')
        screen.blit(game_over_image, game_over_image.get_rect(centerx=screen_width // 2, centery=screen_height // 2))

    pygame.display.update()
    clock.tick(30)