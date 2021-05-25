from constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

def cubeMesh():
    glClearColor (225/255, 207/255, 57/255, 1)

    glBegin(GL_QUADS)
    for face in cube_faces_vector4:
        x = 0
        for vertex in face:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(cube_verticies_vector3[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in cube_edges_vector2:
        for vertex in edge:
            glVertex3fv(cube_verticies_vector3[vertex])
    glEnd()