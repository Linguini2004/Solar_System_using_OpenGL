from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *

class Test(Base):

    def initialize(self):
        print("initializing program...")

        vsCode = '''
        void main()
        {
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
        }
        '''
        fsCode = '''
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0 , 1.0);
        }
        '''

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        glPointSize(10)

    def update(self):

        glUseProgram(self.programRef)

        glDrawArrays(GL_POINTS, 0, 1)

Test().run()