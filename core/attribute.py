from OpenGL.GL import *
import numpy


class Attribute(object):

    def __init__(self, dataType, data):

        self.dataType = dataType

        self.data = data

        self.bufferRef = glGenBuffers(1)
        # Generates a single buffer reference

        self.uploadData()

    def uploadData(self):

        data = numpy.array(self.data).astype(numpy.float32)
        # Creates an array from the provided data

        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        # Specifies the intention of this buffer to be used as a GL_ARRAY_BUFFER

        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)
        # This allocates storage to the buffer bound to GL_ARRAY_BUFFER and stores
        # the flattened data with GL_STATIC_DRAW indicating the data will not be modified again

    def associateVariable(self, programRef, variableName):

        variableRef = glGetAttribLocation(programRef, variableName)
        # This is called from the main program and receives the program object as well as any
        # "in" variables that the C code requires
        # the function returns a reference for the variable

        if variableRef == -1:
            return
        # -1 if the variable specified does not exist

        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        # Rebinds our buffer object with the target just in case

        if self.dataType == "int":
            glVertexAttribPointer(variableRef, 1, GL_INT, False, 0, None)
        elif self.dataType == "float":
            glVertexAttribPointer(variableRef, 1, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec2":
            glVertexAttribPointer(variableRef, 2, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableRef, 3, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec4":
            glVertexAttribPointer(variableRef, 4, GL_FLOAT, False, 0, None)
        # This states that the referenced variable will receive its data from the buffer
        # object bound to the GL_ARRAY_BUFFER

        glEnableVertexAttribArray(variableRef)
        # Specifies that the data stored in our buffer object that is now bound to the
        # variable will be accessed during rendering
