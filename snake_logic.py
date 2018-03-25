class Snake(object):
    def __init__(self, game_grid_instance):
        super(Snake, self).__init__()
        self.game_grid_instance = game_grid_instance
        self.tickno = 0
        self.tickoffset = 0
        self.current_mode = self.test_mode_init #Test mode for now
        #self.test_pattern1()
        
    def game_tick(self):
        #print "Tick tock motherfucker"
        self.current_mode()
        
    
    
    
    
    
    
    
    
    #Didnt really need a test mode but it helps get a feel for how to code the real logic
    #Might also help later when I try to make the grid scale in size
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