
from OpenGL.GL import glColor3ub, glVertex2f, glBegin, glEnd, glClearColor, GL_QUADS, glClear, GL_COLOR_BUFFER_BIT
from OpenGL.GLU import gluOrtho2D
from OpenGL.GLUT import glutTimerFunc, glutInit, glutInitDisplayMode, glutPostRedisplay, glutInitWindowSize, glutInitWindowPosition, glutSwapBuffers, glutCreateWindow, glutDisplayFunc, glutMainLoop, GLUT_DOUBLE, GLUT_RGB, glutSetOption, GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_CONTINUE_EXECUTION
from OpenGL.WGL.EXT import swap_control
#from time import sleep, time
from math import floor, cos, sin, sqrt, pi#, copysign
import sys

WINDOW_SIZE = (500,500)
GRID_SIDE_SIZE_PX = 25
VSYNC = True
TICKRATE_MS = 17
MATH_PRECISION = 5
PIXEL_PRECISION_LIMIT = ()

#Just makes things look nicer
CORNER_ANGLES = {
    "tl": 45,
    "bl": 135,
    "br": 225,
    "tr": 315
}

#Defines the color of each type of element
ELEMENT_TYPES = []
ELEMENT_TYPES.append([0, 0, 0]) # Type # 0; DEFAULT_COLOR
ELEMENT_TYPES.append([66, 255, 0]) # Type # 1; SNAKE_HEAD
ELEMENT_TYPES.append([40, 150, 0]) # Type # 2; SNAKE_TAIL
ELEMENT_TYPES.append([0, 84, 166]) # Type # 3; OBJECTIVE


class Grid(object):
    def __init__(self, grid_side_size_px=GRID_SIDE_SIZE_PX):
        super(Grid, self).__init__()
        self.rows = floor(WINDOW_SIZE[0]/GRID_SIDE_SIZE_PX)
        self.cols = floor(WINDOW_SIZE[1]/GRID_SIDE_SIZE_PX)
        self.grid_side_size_px = grid_side_size_px
        self.active_grid_elements = {}
        
    def get_grid_element(self, grid_index_tuple):
        if self.active_grid_elements.has_key(grid_index_tuple):
            return self.active_grid_elements[grid_index_tuple]
        else:
            return None
    
    def create_grid_element(self, element_type, grid_index_tuple):
        #Figure out the coords of the top-left corner
        x_coord = self.grid_side_size_px * grid_index_tuple[0]
        y_coord = self.grid_side_size_px * grid_index_tuple[1]
        print (x_coord, y_coord)
        new_grid_element = GridElement(self.grid_side_size_px, (x_coord, y_coord), element_type)
        self.active_grid_elements[(x_coord, y_coord)] = new_grid_element
    
    def delete_grid_element(self, grid_index_tuple):
        if self.active_grid_elements.has_key(grid_index_tuple):
            del(self.active_grid_elements[grid_index_tuple])
            return True
        else:
            #Replace-me after debugging
            raise Exception("Tried to delete non-existent grid element at index %s" % repr(grid_index_tuple))
            #return False

class GridElement(object):
    def __init__(self, size_side_px, origin_coords, element_type):
        super(GridElement, self).__init__()
        self.type = element_type
        self.color = ELEMENT_TYPES[element_type]
        self.origin_coords = origin_coords
        self.size_px = size_side_px
        x1 = origin_coords[0]
        y1 = origin_coords[1]
        x2 = origin_coords[0]+self.size_px
        y2 = origin_coords[1]-self.size_px
        #Simple maths now, and it looks clean! Rounding just cause things get out of hand fast with floats.
        self.absolute_center = (round((x1+x2)/2, MATH_PRECISION), round((y1+y2)/2, MATH_PRECISION))
        
    def get_vertices(self):
        return_vertices = {}
        
        return_vertices["tl"] = (self.origin_coords[0], self.origin_coords[1])
        return_vertices["bl"] = (self.origin_coords[0], self.origin_coords[1]+self.size_px)
        return_vertices["br"] = (self.origin_coords[0]+self.size_px, self.origin_coords[1]+self.size_px)
        return_vertices["tr"] = (self.origin_coords[0]+self.size_px, self.origin_coords[1])
        
        return return_vertices
    
    
    def draw(self):
        vertices = self.get_vertices()
        glColor3ub(*self.color)
        glBegin(GL_QUADS)
        glVertex2f(*vertices["tl"])
        glVertex2f(*vertices["bl"])
        glVertex2f(*vertices["br"])
        glVertex2f(*vertices["tr"])
        glEnd()



class RenderManager(object):
    def __init__(self, grid_instance):
        super(RenderManager, self).__init__()
        self.grid_instance = grid_instance

    
    def calc_movement_all_shapes(self, _):
        #Reset our timer
        
        '''
        ############################################
        ## REMOVE AND REPLACE ME WITH SNAKE LOGIC ##
        ############################################
        
        
        for s in self.grid_instance.active_grid_elements:
            s.calc_movement()
            s.calc_collision_mod(self.grid_instance.active_grid_elements)
        
        '''
        glutTimerFunc(TICKRATE_MS, self.calc_movement_all_shapes, 0)
        glutPostRedisplay()
    
    def render_all_shapes(self):
        glClear(GL_COLOR_BUFFER_BIT)
        for index, s in self.grid_instance.active_grid_elements.iteritems():
            s.draw()
        glutSwapBuffers()

def init():
    glClearColor(*(ELEMENT_TYPES[0]+[255])) #All our colors are 3-ints, this one needs alpha channel too so we just tack it on
    gluOrtho2D(0, WINDOW_SIZE[0], WINDOW_SIZE[1], 0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    glutInitWindowSize(*WINDOW_SIZE)
    glutInitWindowPosition(50,50)
    glutCreateWindow("PyGLSnake")
    
    Game_Grid = Grid()
    #Just showin off it working
    Game_Grid.create_grid_element(3, (0,0))
    Game_Grid.create_grid_element(3, (1,1))
    Game_Grid.create_grid_element(3, (2,2))
    Game_Grid.create_grid_element(3, (3,3))
    
    renderman = RenderManager(Game_Grid)
    glutDisplayFunc(renderman.render_all_shapes)
    
    glutTimerFunc(TICKRATE_MS, renderman.calc_movement_all_shapes, 0)
    init()
    
    #Tell Glut to continue execution after we exit the main loop
    #Komodo's code profiler will not return any results unless you shut down just right
    glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_CONTINUE_EXECUTION)
    
    #set vsync
    swap_control.wglSwapIntervalEXT(VSYNC)
    
    #Start everything up
    glutMainLoop()



main()
# End of Program 