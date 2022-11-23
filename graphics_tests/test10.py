from core.base import Base

class Test(Base):

    def initialize(self):
        print("Initializing program...")

    def update(self):

        if self.input.isKeyDown("space"):
            print("The 'space' key was just pressed down")

        if self.input.isKeyPressed("right"):
            print("The 'right' key is currently being pressed")


Test().run()