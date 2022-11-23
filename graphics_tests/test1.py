from core.base import Base

class Test(Base):

    def initialize(self):
        print("Initializing program...")

    def update(self):
        pass

Test().run()
