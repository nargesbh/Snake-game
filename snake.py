class Snake:
    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -10, 'RIGHT': 10}
    dy = {'UP': -10, 'DOWN': 10, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, cells, color, direction, speed):
        #pos is a 2D list that include the snake's body cells , the last element of the list is the head of the snake 
        self.cells = cells
        self.color = color
        self.direction = direction
        self.speed = speed

    def find_direction(self, inp_key):
        if inp_key == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if inp_key == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if inp_key == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if inp_key == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
    
    def move_handler(self):
        head_y = 0
        head_x = 0
        if self.direction == 'UP':
            head_y =  self.cells[-1][1] + Snake.dy['UP']
            head_x = self.cells[-1][0]
        
        elif self.direction == 'DOWN':
            head_y  = self.cells[-1][1] + Snake.dy['DOWN']
            head_x = self.cells[-1][0]

        elif self.direction == 'LEFT':
            head_x = self.cells[-1][0] + Snake.dx['LEFT']
            head_y = self.cells[-1][1]

        elif self.direction == 'RIGHT':
            head_x  = self.cells[-1][0] + Snake.dx['RIGHT'] 
            head_y = self.cells[-1][1] 

        self.cells.append([head_x, head_y])




