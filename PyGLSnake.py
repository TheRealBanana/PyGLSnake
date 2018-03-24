
from OpenGL.GL import glColor3f, glVertex2f, glBegin, glEnd, glClearColor, GL_QUADS, glClear, GL_COLOR_BUFFER_BIT
from OpenGL.GLU import gluOrtho2D
from OpenGL.GLUT import glutTimerFunc, glutInit, glutInitDisplayMode, glutPostRedisplay, glutInitWindowSize, glutInitWindowPosition, glutSwapBuffers, glutCreateWindow, glutDisplayFunc, glutMainLoop, GLUT_DOUBLE, GLUT_RGB, glutSetOption, GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_CONTINUE_EXECUTION
from OpenGL.WGL.EXT import swap_control
#from time import sleep, time
from math import cos, sin, sqrt, pi#, copysign
import sys



WINDOW_SIZE = (500,500)
VSYNC = True
TICKRATE_MS = 17
MATH_PRECISION = 5


ELEMENT_TYPES = {}
ELEMENT_TYPES["SNAKE_HEAD"] = []
ELEMENT_TYPES["SNAKE_TAIL"] = []
ELEMENT_TYPES["OBJECTIVE"]  = []


def float_to_analog(colorf):
    return int(round(colorf*255))

def analog_to_float(colora):
    return (colora/255.0)-1

class Grid(object):
    def __init__(self, rows, cols):
        super(Grid, self).__init__()
        self.rows = rows
        self.cols = cols
        min_side = min(WINDOW_SIZE)
        self.grid_element_size = (min_side/rows, min_side/cols)
        self.active_grid_elements = {}
        
    def get_grid_element(self, grid_index_tuple):
        if self.active_grid_elements.has_key(grid_index_tuple) is True:
            return self.active_grid_elements[grid_index_tuple]
        else:
            return None
    
    def create_grid_element(self, element_type, grid_index_tuple):
        #Figure out the coords of the top-left corner
        
        pass

class GridElement(object):
    def __init__(self, size_side_px, origin_coords):
        super(GridElement, self).__init__()








class RenderManager(object):
    def __init__(self):
        super(RenderManager, self).__init__()
        self.shapes = []
    
    
    def calc_movement_all_shapes(self, _):
        #Reset our timer
        glutTimerFunc(TICKRATE_MS, self.calc_movement_all_shapes, 0)
        for s in self.shapes:
            s.calc_movement()
            s.calc_collision_mod(self.shapes)
        glutPostRedisplay()
    
    def render_all_shapes(self):
        glClear(GL_COLOR_BUFFER_BIT)
        for s in self.shapes:
            s.render()
        glutSwapBuffers()
    
    def add_shape(self, shape):
        if shape not in self.shapes:
            self.shapes.append(shape)
        
    def remove_shape(self, shape):
        if shape in self.shapes:
            del(self.shapes[self.shapes.index(shape)])

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE)
    glutInitWindowPosition(50,50)
    glutCreateWindow("BouncySquare 2.0")
    renderman = RenderManager()
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