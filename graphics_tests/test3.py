from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *


class Test(Base):

    def initialize(self):
        print("Initializing program...")

        vsCode = '''
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        '''

        fsCode = '''
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        '''

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        # This creates a program object with a vertex and fragment shader each with
        # the above code
        # These codes either require or output date which is handled by the attribute class

        glLineWidth(4)

        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        positionData = [[0.8, 0.0, 0.0], [0.4, 0.6, 0.0], [-0.4, 0.6, 0.0], [-0.8, 0.0, 0.0], [-0.4, -0.6, 0.0],
                        [0.4, -0.6, 0.0]]
        # The positions of the vertices that will be used in the vsCode

        self.vertexCount = len(positionData)

        positionAttribute = Attribute("vec3", positionData)
        # Creates an attribute object that will store this data to a buffer
        positionAttribute.associateVariable(self.programRef, "position")
        # Requests that said data be funnelled to the "position" variable when the program runs

    def update(self):
        glUseProgram(self.programRef)
        # Specifies what program object to use when running
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCount)
        # GL_LINE_LOOP specifies that the lines will be rendered from one point to the next
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)
        # GL_TRIANGLES groups the points into separate triangles and draws them
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)
        # GL_TRAINGLE_FAN draws the triangles so that they all share a start point and
        # each triangle shares an edge with the next



Test().run()