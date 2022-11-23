from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.ellipsoidGeometry import EllipsoidGeometry
from material.surfaceMaterial import SurfaceMaterial
from math import sin, cos, tan, pi, atan
from numpy import array, linalg
import time

class Solar1(Base):

    def initialize(self):
        print("Initializing system...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=1600 / 1000, angleOfView=80, far=100000000)
        #self.camera.setPosition([0, 0, 400])
        self.camera.setPosition([0, 1000, 0])
        self.camera.rotateX(-pi/2)
        self.total_cam_change = 0

        self.size_scale = 0.00000005
        self.time_step = 360*24
        self.days = 0

        self.Bodies = []

        self.create_bodies()

    def create_bodies(self):
        #global_scale = self.global_scale
        size_scale = self.size_scale

        Sun = Solar_body(696000000 * size_scale, 1, [1, 1, 0], 1.989 * 10 ** 30, "sun")
        Mercury = Solar_body(2440000 * size_scale, 10, [0.91, 0.91, 0.93], 3.285 * 10**23, "mercury")
        Venus = Solar_body(6051000 * size_scale, 10, [1, 0.77, 0.29], 4.867 * 10**24, "venus")
        Earth = Solar_body(6370000 * size_scale, 10, [0.52, 0.81, 0.92], 5.972 * 10**24, "earth")
        #Moon = Solar_body(1740000 * size_scale, 10, [0.91, 0.91, 0.93], 7.35 * 10**22, "moon")
        Mars = Solar_body(3390000 * size_scale, 10, [0.68, 0.38, 0.26], 6.4 * 10**23, "mars")
        Jupiter = Solar_body(69900000 * size_scale, 10, [0.89, 0.86, 0.80], 1.9 * 10**27, "jupiter")
        Saturn = Solar_body(58200000 * size_scale, 10, [0.77, 0.67, 0.43], 5.68 * 10**26, "saturn")
        Uranus = Solar_body(25400000 * size_scale, 10, [0.93, 0.93, 1], 8.61 * 10**25, "uranus")
        Neptune = Solar_body(24600000 * size_scale, 10, [0.16, 0.56, 0.71], 1.024 * 10**26, "neptune")

        self.bodies = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]
        #self.bodies = [Sun, Earth]
        # moon --> [(1.495 * 10 ** 11), 0, 0] and array([0.0, 1000.0, 30000.0])

        positions = [[0, 0, 0], [(0.596 * 10 ** 11), 0, 0], [(1.082 * 10 ** 11), 0, 0], [(1.49 * 10 ** 11), 0, 0], [(2.24 * 10 ** 11), 0, 0], [(7.75 * 10 ** 11), 0, 0], [(14.2 * 10 ** 11), 0, 0], [(29.5 * 10 ** 11), 0, 0], [(44.7 * 10 ** 11), 0, 0]]
        velocities = [array([0.0, 0.0, 0.0]), array([0.0, 0.0, 47400.0]), array([0.0, 0.0, 35000.0]), array([0.0, 0.0, 30000.0]), array([0.0, 0.0, 24100.0]), array([0.0, 0.0, 13100.0]), array([0.0, 0.0, 9690.0]), array([0.0, 0.0, 6810.0]), array([0.0, 0.0, 5430])]
        #positions = [[0, 0, 0], [(1.49 * 10 ** 11), 0, 0]]
        #velocities = [array([0.0, 0.0, 0.0]), array([0.0, 0.0, 30000.0])]

        for e, body in enumerate(self.bodies):
            self.scene.add(body.mesh)
            body.set_initial_position([i for i in positions[e]])
            body.set_velocity(velocities[e])

    def calculate_acceleration_from_gravity(self):
        #for i in range(self.speed):
        for body1 in self.bodies:
            rest = list(self.bodies)
            rest.remove(body1)
            force = array([0.0, 0.0, 0.0])
            for body2 in rest:

                p = array(body1.position)
                q = array(body2.position)
                pq = q - p
                pq_unit = pq / linalg.norm(pq)
                force += (pq_unit * ((6.6743 * 10 ** -11) * ((body1.mass * body2.mass))) / (linalg.norm(pq))**2)

            acceleration = force / body1.mass
            body1.update_position(self.time_step * acceleration, self.time_step)

            self.days += self.time_step / (24*3600)

        for body in self.bodies:
            body.translate()

    '''

    def calculate_positions(self):
        positions = {"sun": array([0.0, 0.0, 0.0]), "earth": array([(1.49 * 10 ** 11), 0.0, 0.0])}
        velocities = {"sun": array([0.0, 0.0, 0.0]), "earth": array([0.0, 0.0, 30000.0])}
        masses = {"sun": 1.989 * 10 ** 30, "earth": 5.972 * 10 ** 24}
        bodies = ["sun", "earth"]
        stored_positions = {"sun": [], "earth": []}

        for i in range(100000):
            for body1 in bodies:
                rest = list(bodies)
                rest.remove(body1)
                force = array([0.0, 0.0, 0.0])
                for body2 in rest:
                    p = array(positions[body1])
                    q = array(positions[body2])
                    pq = q - p
                    pq_unit = pq / linalg.norm(pq)
                    force += ((6.6743 * 10 ** -11) * ((masses[body1] * masses[body2])) / (linalg.norm(pq))**2) * pq_unit

                stored_positions[body1].append(positions[body1])
                #print(stored_positions)

                #print(force / masses[body1])
                #print(positions["earth"])
                positions[body1] += (force/masses[body1])


                #positions.update({body1: positions[body1] + (force / masses[body1])})

        return stored_positions
    
    
    def set_positions_from_stored(self):
        #print(self.stored_positions["earth"][int(self.time)])
        for body in self.bodies:
            body.translate(from_stored= True, stored_pos=self.stored_positions[body.name][int(self.time)])

        self.time += 1
    
    '''

    def get_inputs(self):
        mc = self.input.get_mouse_pos()
        fl = 1000

        self.camera.rotateY(-atan(mc[0] / fl), localCoord=False)

        self.total_cam_change += -atan(mc[0] / fl)

        self.camera.rotateX(cos(self.total_cam_change) * -atan(mc[1] / fl), localCoord=False)
        self.camera.rotateZ(sin(self.total_cam_change) * atan(mc[1] / fl), localCoord=False)

        if self.input.isMousePressed(4):
            self.camera.translate(0, 0, -50)

        if self.input.isMousePressed(5):
            self.camera.translate(0, 0, 50)

        if self.input.isKeyPressed("w"):
            self.camera.translate(0, 0, -0.01)

        if self.input.isKeyPressed("s"):
            self.camera.translate(0, 0, 0.01)

        if self.input.isKeyPressed("z"):
            self.time_step -= 1000

        if self.input.isKeyPressed("x"):
            self.time_step += 1000

    def update(self):

        self.calculate_acceleration_from_gravity()

        self.renderer.render(self.scene, self.camera)

        self.get_inputs()

class Solar_body:

    def __init__(self, radius, sf, color, mass, name):
        self.global_scale = 0.000000001
        self.name = name
        self.radius = radius
        self.sf = sf

        dim = 2 * self.sf * self.radius
        self.geometry = EllipsoidGeometry(dim, dim, dim)
        self.material = SurfaceMaterial({"useVertexColors": False, "baseColor": color})
        self.mesh = Mesh(self.geometry, self.material)
        self.mass = mass
        self.position = None
        self.velocity = array([0, 0, 0])

    def update_position(self, deltav, time):
        self.velocity += deltav
        self.position += self.velocity * time

    def translate(self, from_stored=False, stored_pos=None):
        if not from_stored:
            new_pos = self.position * self.global_scale
            #print(new_pos)
        else:
            new_pos = stored_pos * self.global_scale
            #print(new_pos)
        self.mesh.setPosition(new_pos.tolist())

    def set_initial_position(self, position):
        self.position = position

        self.mesh.setPosition([i * self.global_scale for i in position])

    def set_velocity(self, velocity):
        self.velocity = velocity

Solar1(screenSize=[1600, 1000]).run()
