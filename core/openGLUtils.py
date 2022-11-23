from OpenGL.GL import *


class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):
        shaderCode = '#version 330\n' + shaderCode
        # The shader code is the C code that we write in the main program

        shaderRef = glCreateShader(shaderType)
        # This creates a new shader with either the vertex or fragment type

        glShaderSource(shaderRef, shaderCode)
        glCompileShader(shaderRef)
        # This adds the shader code to the specified shader and then compiles the code
        # so that it can be run

        compileSuccess = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)
        # Checks if compile was successful

        if not compileSuccess:
            errorMessage = glGetShaderInfoLog(shaderRef)
            glDeleteShader(shaderRef)
            errorMessage = "\n" + errorMessage.decode("utf-8")
            raise Exception(errorMessage)

        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):

        vertexShaderRef = OpenGLUtils.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        # Creates a vertex shader using the InitializeShader method

        fragmentShaderRef = OpenGLUtils.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)
        # Creates a fragment shader using the InitializeShader method

        programRef = glCreateProgram()
        # Creates an empty program object to which we can attach shaders

        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)
        # Attaches both shaders to the specified program

        glLinkProgram(programRef)
        # Links the two shaders and checks that variables are referenced consistently - no contention

        linkSuccess = glGetProgramiv(programRef, GL_LINK_STATUS)
        # Checks if link was successful

        if not linkSuccess:
            errorMessage = glGetProgramInfoLog(programRef)
            glDeleteProgram(programRef)
            errorMessage = "\n" + errorMessage.decode("utf-8")
            raise Exception(errorMessage)

        return programRef

    @staticmethod
    def printSystemInfo():
        print(" Vendor: " + glGetString(GL_VENDOR).decode("utf-8"))
        print(" Renderer: " + glGetString(GL_RENDERER).decode("utf-8"))
        print(" OpenGL version supported: " + glGetString(GL_VERSION).decode("utf-8"))
        print(" GLSL version supported: " + glGetString(GL_SHADING_LANGUAGE_VERSION).decode("utf-8"))
