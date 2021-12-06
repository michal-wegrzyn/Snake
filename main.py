import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(6, 5), Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)]
        self.deleted_block = Vector2(2, 5)
        self.direction = Vector2(1, 0)
        self.grow = False
        self.near_apple = False
        self.bodya = pygame.image.load("Images/bodya.png").convert_alpha()
        self.bodya = pygame.transform.scale(self.bodya, (40, 40))
        self.bodyb = pygame.image.load("Images/bodyb.png").convert_alpha()
        self.bodyb = pygame.transform.scale(self.bodyb, (40, 40))
        self.tail = pygame.image.load("Images/tail.png").convert_alpha()
        self.tail = pygame.transform.scale(self.tail, (40, 40))
        self.head = pygame.image.load("Images/head.png").convert_alpha()
        self.head = pygame.transform.scale(self.head, (40, 40))
        self.head_eat = pygame.image.load("Images/head_eat.png").convert_alpha()
        self.head_eat = pygame.transform.scale(self.head_eat, (40, 40))
        self.dead_head = pygame.image.load("Images/dead.png").convert_alpha()
        self.dead_head = pygame.transform.scale(self.dead_head, (40, 40))
        self.dead_head_left = pygame.image.load("Images/deadl.png").convert_alpha()
        self.dead_head_left = pygame.transform.scale(self.dead_head_left, (40, 40))
        self.dead_head_right = pygame.image.load("Images/deadr.png").convert_alpha()
        self.dead_head_right = pygame.transform.scale(self.dead_head_right, (40, 40))
        self.crunch_sound = pygame.mixer.Sound('Sounds/apple-crunch.wav')
        self.game_over_sound = pygame.mixer.Sound('Sounds/game_over.wav')
        self.dead = False
        self.stop = True

    def direction_to_number(self, vector):
        if vector == Vector2(0, 1):
            return 0 #up
        elif vector == Vector2(-1, 0):
            return 1 #right
        elif vector == Vector2(0, -1):
            return 2 #down
        elif vector == Vector2(1, 0):
            return 3 #left
        print(vector.x, vector.y)

    def draw_snake(self):
        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                rel = self.body[1] - self.body[0]
                if not self.dead:
                    if self.near_apple:
                        head = self.head_eat
                    else:
                        head = self.head
                    if rel == Vector2(1, 0):
                        screen.blit(pygame.transform.rotate(head, 90), block_rect)
                    elif rel == Vector2(-1, 0):
                        screen.blit(pygame.transform.rotate(head, 270), block_rect)
                    elif rel == Vector2(0, 1):
                        screen.blit(head, block_rect)
                    elif rel == Vector2(0, -1):
                        screen.blit(pygame.transform.rotate(head, 180), block_rect)
                else:
                    prev_direction = self.body[0] - self.body[1]
                    dead_rel = self.direction_to_number(self.direction) - self.direction_to_number(prev_direction)
                    dead_head = self.dead_head
                    if dead_rel == -1 or dead_rel == 3:
                        dead_head = self.dead_head_left
                    elif dead_rel == 1 or dead_rel == -3:
                        dead_head = self.dead_head_right
                    else:
                        dead_head = self.dead_head
                    if rel == Vector2(1, 0):
                        screen.blit(pygame.transform.rotate(dead_head, 90), block_rect)
                    elif rel == Vector2(-1, 0):
                        screen.blit(pygame.transform.rotate(dead_head, 270), block_rect)
                    elif rel == Vector2(0, 1):
                        screen.blit(dead_head, block_rect)
                    elif rel == Vector2(0, -1):
                        screen.blit(pygame.transform.rotate(dead_head, 180), block_rect)
            elif index == len(self.body)-1:
                rel = self.body[-2] - self.body[-1]
                if rel == Vector2(1, 0):
                    screen.blit(pygame.transform.rotate(self.tail, 90), block_rect)
                elif rel == Vector2(-1, 0):
                    screen.blit(pygame.transform.rotate(self.tail, 270), block_rect)
                elif rel == Vector2(0, 1):
                    screen.blit(self.tail, block_rect)
                elif rel == Vector2(0, -1):
                    screen.blit(pygame.transform.rotate(self.tail, 180), block_rect)
            else:
                prev = self.body[index+1]-block
                next = self.body[index-1]-block
                if prev.x == next.x:
                    screen.blit(self.bodya, block_rect)
                elif prev.y == next.y:
                    screen.blit(pygame.transform.rotate(self.bodya, 90), block_rect)
                elif prev.x == -1 and next.y == -1 or prev.y == -1 and next.x == -1:
                    screen.blit(pygame.transform.rotate(self.bodyb, 270), block_rect)
                elif prev.x == -1 and next.y == 1 or prev.y == 1 and next.x == -1:
                    screen.blit(self.bodyb, block_rect)
                elif prev.x == 1 and next.y == -1 or prev.y == -1 and next.x == 1:
                    screen.blit(pygame.transform.rotate(self.bodyb, 180), block_rect)
                elif prev.x == 1 and next.y == 1 or prev.y == 1 and next.x == 1:
                    screen.blit(pygame.transform.rotate(self.bodyb, 90), block_rect)

    def move(self):
        if not self.stop:
            self.direction = direction
            if self.grow == False:
                self.deleted_block = self.body[-1]
                body_copy = self.body[:-1]
            else:
                body_copy = self.body[:]
                self.grow = False
            body_copy.insert(0, body_copy[0]+self.direction)
            self.body = body_copy

    def eat(self):
        self.grow = True

class FOOD:
    def __init__(self):
        self.randpos()

    def randpos(self):
        self.x = random.randint(0, grid_x_size-1)
        self.y = random.randint(0, grid_y_size - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_food(self):
        food_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, food_rect)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()

    def update(self):
        self.snake.move()
        self.check_eat()
        if not self.snake.dead:
            self.check_game_over()

    def draw(self):
        self.draw_grass()
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_score()
        self.draw_highscore()
        self.draw_restart_button()

    def check_eat(self):
        if -1 <= self.food.pos.x-self.snake.body[0].x <= 1 and -1 <= self.food.pos.y-self.snake.body[0].y <= 1:
            self.snake.near_apple = True
        else:
            self.snake.near_apple = False

        if self.food.pos == self.snake.body[0]:
            self.snake.crunch_sound.play()
            self.food.randpos()
            self.snake.eat()
            while self.food.pos in self.snake.body[:]:
                self.food.randpos()

    def check_game_over(self):
        if not 0 <= self.snake.body[0].x < grid_x_size or not 0 <= self.snake.body[0].y < grid_y_size:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.body.append(self.snake.deleted_block)
        self.snake.body = self.snake.body[1:]
        global highscore
        score = len(self.snake.body)-4
        if score > highscore:
            highscore_file = open("highscore.txt", "w")
            highscore_file.write(str(score))
            highscore_file.close()
            highscore = score
        self.snake.dead = True
        self.snake.stop = True
        self.snake.game_over_sound.play()

    def restart(self):
        self.snake.body = [Vector2(6, 5), Vector2(5, 5), Vector2(4, 5), Vector2(3, 5)]
        self.snake.direction = Vector2(1, 0)
        self.snake.dead = False
        self.snake.stop = True
        self.food.randpos()
        while self.food.pos in self.snake.body[:]:
            self.food.randpos()

    def draw_grass(self):
        grass_color = (170, 200, 65)
        grass_color2 = (175, 215, 10)
        for row in range(grid_y_size):
            if row % 2 == 0:
                for col in range(grid_x_size):
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    if col % 2 == 0:
                        pygame.draw.rect(screen, grass_color, grass_rect)
                    else:
                        pygame.draw.rect(screen, grass_color2, grass_rect)
            else:
                for col in range(grid_x_size):
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    if col % 2 != 0:
                        pygame.draw.rect(screen, grass_color, grass_rect)
                    else:
                        pygame.draw.rect(screen, grass_color2, grass_rect)

    def draw_score(self):
        score = str(len(self.snake.body)-4)
        score_surface = game_font.render(score, True, (57, 74, 12))
        score_rect = score_surface.get_rect(topleft=(70, HEIGHT-50), bottomright=(120, HEIGHT-10))
        score_rect.left = 70
        screen.blit(score_surface, score_rect)
        screen.blit(apple, (20, HEIGHT-45, 40, 40))

    def draw_highscore(self):
        highscore_surface = game_font.render(str(highscore), True, (57, 74, 12))
        highscore_rect = highscore_surface.get_rect(topleft=(260, HEIGHT - 50), bottomright=(320, HEIGHT - 10))
        highscore_rect.left = 260
        screen.blit(highscore_surface, highscore_rect)
        screen.blit(trophy, (200, HEIGHT - 45, 40, 40))

    def draw_restart_button(self):
        button_rect = pygame.Rect(WIDTH-125, HEIGHT-40, 100, 30)
        button_color = (175, 215, 10)
        pygame.draw.rect(screen, button_color, button_rect)
        text_surface = game_font.render('Restart', True, (57, 74, 12))
        text_rect = text_surface.get_rect(midtop = (WIDTH-75, HEIGHT-35))
        screen.blit(text_surface, text_rect)


highscore_file = open('highscore.txt', encoding='UTF-8')
highscore = int(highscore_file.read())
highscore_file.close()

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

grid_x_size = 15
grid_y_size = 10
cell_size = 40
screen = pygame.display.set_mode((grid_x_size * cell_size, grid_y_size * cell_size+50))
apple = pygame.image.load("Images/apple.png").convert_alpha()
apple = pygame.transform.scale(apple, (40, 40))
trophy = pygame.image.load("Images/trophy.png").convert_alpha()
trophy = pygame.transform.scale(trophy, (40, 40))
icon = pygame.image.load("Images/icon.png").convert_alpha()
icon = pygame.transform.scale(icon, (32, 32))
main_game = MAIN()
clock = pygame.time.Clock()
WIDTH = grid_x_size * cell_size
HEIGHT = grid_y_size * cell_size + 50

game_font = pygame.font.Font(None, 40)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
pygame.display.set_icon(icon)
pygame.display.set_caption('Snake')

direction = main_game.snake.direction

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if WIDTH-125 <= mouse[0] <= WIDTH-25 and HEIGHT-40 <= mouse[1] <= HEIGHT-10:
                main_game.restart()

        if event.type == pygame.KEYDOWN and not main_game.snake.dead:
            direction = main_game.snake.direction
            if event.key == pygame.K_UP and main_game.snake.direction != Vector2(0, 1):
                direction = Vector2(0, -1)
            elif event.key == pygame.K_RIGHT and main_game.snake.direction != Vector2(-1, 0):
                direction = Vector2(1, 0)
            elif event.key == pygame.K_DOWN and main_game.snake.direction != Vector2(0, -1):
                direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT and main_game.snake.direction != Vector2(1, 0):
                direction = Vector2(-1, 0)

            main_game.snake.stop = False


    screen.fill((105, 150, 10))
    main_game.draw()
    pygame.display.update()
    clock.tick(60)