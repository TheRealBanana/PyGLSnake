class Snake(object):
    def __init__(self, game_grid_instance):
        super(Snake, self).__init__()
        self.game_grid_instance = game_grid_instance
        self.tickno = 0
        self.tickoffset = 0
        #self.current_mode = self.test_mode_init #Test mode for now
        self.current_mode = self.snake_mode
        self.current_grid = (5, 5)
        self.direction = "down"
        self.snake_grids = [self.current_grid]
        self.game_grid_instance.create_grid_element(1, self.current_grid)
        self.objective_list = []
        self.length = 5
        self.alive = True
        #self.test_pattern1()
        
    def game_tick(self):
        #print "Tick tock motherfucker"
        self.current_mode()
        
    
    def snake_mode(self):
        #self.moveSnake()
        self.snake_move_test()
    
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
            #Color the block we ran into red
            self.game_grid_instance.create_grid_element(next_move, 4)
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
            print "UGH WE DED"
            self.current_mode = self.game_over
    
    
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
        
    
    def changeDirection(self, newdir):
        if self.alive == True:
            #Dont allow direction change in the direct opposite (run backwards)
            if self.getMove(newdir) != self.snake_grids[-2]:
                self.direction = newdir
    
    
    
    
    #Didnt really need a test mode but it helps get a feel for how to code the real logic
    #Might also help later when I try to make the grid scale in size
    
    def snake_move_test(self):
        square_size = 5
        right_square_path = ["right","down","left","up"]
        left_square_path = ["up","left","down","right"]
        
        self.moveSnake()
        self.tickoffset += 1
        if self.tickoffset > square_size:
            self.direction = right_square_path[right_square_path.index(self.direction)-1]
            self.tickoffset = 0
        
    
    
    def test_mode_init(self):
        print "Test mode init"
        #Run each test pattern 5 times
        self.test_patterns = [self.test_pattern1]
        self.current_test_pattern = self.test_pattern1
        self.test_iteration = 0
        self.current_mode = self.test_mode
    
    def test_mode(self):
        #print "Test mode run"
        self.current_test_pattern()
        self.test_iteration += 1
        if self.tickno + self.tickoffset >= self.game_grid_instance.cols:
            print "HIT THE END"
            self.tickno = 0
            print "ITERATE TICK OFFSET"
            self.test_iteration = 0
            self.tickoffset += 3
            if self.tickoffset >= self.game_grid_instance.cols:
                print "HIT THE SECOND END"
                self.tickoffset = 0
            #self.current_test_pattern = self.test_patterns[self.test_patterns.index(self.current_test_pattern)-1]
        
        
    def test_pattern1(self):
        
        #Countdown Y first then countdown X (count down being count up really ugh confusing.)
        
        updown_offset = self.tickno + self.tickoffset
        print (0+self.tickno,0+updown_offset)
        #Just showin off it working
        self.game_grid_instance.clear_grid()
        self.game_grid_instance.create_grid_element((self.tickno%3)+1, (0+self.tickno,0+updown_offset))
        self.game_grid_instance.create_grid_element((self.tickno%3)+1, (1+self.tickno,1+updown_offset))
        self.game_grid_instance.create_grid_element((self.tickno%3)+1, (2+self.tickno,2+updown_offset))
        self.game_grid_instance.create_grid_element((self.tickno%3)+1, (3+self.tickno,3+updown_offset))
        self.tickno += 1