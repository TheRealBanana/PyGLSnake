class Snake(object):
    def __init__(self, game_grid_instance):
        super(Snake, self).__init__()
        self.game_grid_instance = game_grid_instance
        self.tickno = 0
        #self.current_mode = self.test_mode_init #Test mode for now
        self.current_mode = self.snake_mode
        self.current_grid = (9, 7)
        self.direction = "None"
        self.snake_grids = [self.current_grid]
        self.game_grid_instance.create_grid_element(1, self.current_grid)
        self.objective_list = []
        self.length = 25
        self.alive = True
        
    def game_tick(self):
        self.current_mode()
        self.tickno += 1 #not sure why im doing this.
        
    
    def snake_dead(self):
        #Color the snake head red to indicate we ded
        self.game_grid_instance.create_grid_element(4, self.current_grid)
        print "UGH WE DED"
        self.current_mode = self.game_over
    
    def snake_mode(self):
        if self.direction == "None":
            #Just starting out. Do stuffs for just starting out...
            self.direction = "right"
        
        self.moveSnake()
        #self.snake_move_test()
    
    def game_over(self):
        pass
    
    def moveSnake(self):
        #Figure out the next grid from our current grid and our direction
        next_move = self.getMove()
        
        
        #Hit a wall, game over man. Game over!
        if ((0 <= next_move[0] < self.game_grid_instance.rows) and (0 <= next_move[1] < self.game_grid_instance.cols)) is False:
            self.alive = False
        
        #Hit ourself! X(
        elif next_move in self.snake_grids:
            self.alive = False
            
        
        #good move
        else:
            #Move snake head, change old square color to snake body (state 7), cut off snake tail by changing to white if current snake size == max snake size
            self.game_grid_instance.create_grid_element(1, next_move) #Snake head is state 1
            self.game_grid_instance.create_grid_element(2, self.current_grid) #Snake tail is state 2
            
            self.snake_grids.append(next_move)
            
            #Check our length before we see if we collected an objective
            #Truncate our tail if we are too long
            if len(self.snake_grids) >= self.length:
                self.game_grid_instance.delete_grid_element(self.snake_grids.pop(0)) #State 0 is white
            
            #see if we collected an objective (state 1)
            if next_move in self.objective_list:
                self.collectedObj(next_move)
            
            self.current_grid = next_move
        if self.alive == False:
            self.snake_dead()
    
    
    def getMove(self, direction=None):
        if direction is None: direction = self.direction
        
        if direction == "down":
            next_grid = (self.current_grid[0], self.current_grid[1]+1)
            
        elif direction == "up":
            next_grid = (self.current_grid[0], self.current_grid[1]-1)
            
        elif direction == "right":
            next_grid = (self.current_grid[0]+1, self.current_grid[1])
        
        elif direction == "left":
            next_grid = (self.current_grid[0]-1, self.current_grid[1])
        
        return next_grid
        
    
    #Getting input from GLUT's special input func
    def keypress_callback_GLUT(self, keycode, _, __): #Last two args are the x and y coords but we dont care about them
        if keycode == 100: self.changeDirection("left")
        elif keycode == 101: self.changeDirection("up")
        elif keycode == 102: self.changeDirection("right")
        elif keycode == 103: self.changeDirection("down")
    
    def changeDirection(self, newdir):
        if self.alive == True:
            #Dont allow direction change in the direct opposite (run backwards)
            if self.getMove(newdir) != self.snake_grids[-2]:
                self.direction = newdir

