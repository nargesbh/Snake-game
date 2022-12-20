import sys
import pygame
import time
import random
import snake

class screen:
    def __init__(self, window_x, window_y, snake_direction, snake_speed, snake_cells):
        self.window_x = window_x
        self.window_y = window_y

        self.score = 0

        self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10, random.randrange(1, (self.window_y//10)) * 10]
        self.fruit_spawn = True

        #this is the game mode
        self.open_wall = True

        self.make_screen()
        fps = pygame.time.Clock()

        self.snake = snake.Snake(snake_cells, self.snake_color, snake_direction, snake_speed)


        while True:
            
            inp = self.snake.direction
            # handling key events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        inp = 'UP'
                    if event.key == pygame.K_DOWN:
                        inp = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        inp = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        inp = 'RIGHT'

            self.snake.find_direction(inp)

            self.snake.move_handler()

            self.after_move_coloring()

            self.show_score(pygame.Color(255,0,0), 'times new roman', 20)

            pygame.display.update()

            fps.tick(self.snake.speed)

    def make_screen(self):
        pygame.display.set_caption('Snake game')
        self.game_window = pygame.display.set_mode((self.window_x, self.window_y))
        
        self.screen_mode()

    def screen_mode(self):
        user_text = ""
        my_font = pygame.font.SysFont('times new roman', 25)
        screen_color_surface = my_font.render('please enter the screen mode : (1 for night mode and 2 for day mode)', True, pygame.Color(0,255,255))
        screen_color_rect = screen_color_surface.get_rect()
        
        screen_color_rect.midtop = (self.window_x/2, self.window_y/4)
        
        self.game_window.blit(screen_color_surface, screen_color_rect)
        pygame.display.flip()

        time.sleep(6)
        # finding the screen mode
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                user_text = event.unicode

        if user_text == "1": #black screen with green snake and red fruit
            self.screen_color = pygame.Color(0, 0, 0) 
            self.snake_color = pygame.Color(0, 255, 0)
            self.fruit_color = pygame.Color(255, 0, 0)

        else: #white screen with pink snake and yellow fruit
            self.screen_color = pygame.Color(255, 255, 255)
            self.snake_color = pygame.Color(255,100,180)
            self.fruit_color = pygame.Color(50,50,50)


        self.game_window.fill(self.screen_color)
        self.game_mode()

    def game_mode(self):
        user_inp = ""
        my_font = pygame.font.SysFont('times new roman', 25)
        game_mode_surface = my_font.render('do you want your snake to die when it hits the walls : (1 for yes , 0 for no)', True, pygame.Color(0,255,255))
        game_mode_rect = game_mode_surface.get_rect()
        
        game_mode_rect.midtop = (self.window_x/2, self.window_y/4)
        
        self.game_window.blit(game_mode_surface, game_mode_rect)
        pygame.display.flip()

        time.sleep(6)
        # finding the screen mode
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                user_inp = event.unicode
        if user_inp == "1": 
            self.open_wall= False
        
        self.game_window.fill(self.screen_color)

    def game_over(self):

        my_font = pygame.font.SysFont('times new roman', 50)

        game_over_surface = my_font.render(
            'Your Score is : ' + str(self.score), True, pygame.Color(255, 0, 0))
        
        game_over_rect = game_over_surface.get_rect()
        
        game_over_rect.midtop = (self.window_x/2, self.window_y/4)
        
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        
        # the program will get closed after 1 seconds
        time.sleep(1)

        pygame.quit()
        
        # quit the program
        quit()

    def show_score(self, color, font, size):

        score_font = pygame.font.SysFont(font, size)
        
        score_surface = score_font.render('Score : ' + str(self.score), True, color)

        score_rect = score_surface.get_rect()
        
        # displaying text
        self.game_window.blit(score_surface, score_rect)
    
    def after_move_coloring(self):
        
        if self.snake.cells[-1][0] == self.fruit_position[0] and self.snake.cells[-1][1] == self.fruit_position[1]:
            self.score += 10
            self.fruit_spawn = False
        else:
            self.snake.cells.pop(0)
        
        if self.open_wall:
            if self.snake.cells[-1][0] < 0:
                self.snake.cells[-1][0] = self.window_x-10

            if self.snake.cells[-1][1] < 0:
                self.snake.cells[-1][1] = self.window_y-10

            if self.snake.cells[-1][0] > self.window_x-10:
                self.snake.cells[-1][0] = 10

            if self.snake.cells[-1][1] > self.window_y-10:
                self.snake.cells[-1][1] = 10

        if not self.fruit_spawn:
            self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10,
                            random.randrange(1, (self.window_y//10)) * 10]     
        self.fruit_spawn = True
        self.game_window.fill(self.screen_color)

        #coloring the snake
        for pos in self.snake.cells:
            pygame.draw.rect(self.game_window, self.snake.color,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(self.game_window, self.fruit_color, pygame.Rect(
            self.fruit_position[0], self.fruit_position[1], 10, 10))

        if self.open_wall == False:
            if self.snake.cells[-1][0] < 0 or self.snake.cells[-1][0] > self.window_x-10:
                self.game_over()
                
            if self.snake.cells[-1][1] < 0 or self.snake.cells[-1][1] > self.window_y-10:
                self.game_over()
        
        #checking if the snake has touched its body
        for block in self.snake.cells[:len(self.snake.cells)-1]:
            if self.snake.cells[-1][0] == block[0] and self.snake.cells[-1][1] == block[1]:
                self.game_over()