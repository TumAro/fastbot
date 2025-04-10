from fastbot.core.object import Object
import pymunk

class Robot(Object):
    def __init__(self, position=(0,0), orientation=0):
        super().__init__(position, orientation)
        self.shape = "circle"  # Default shape
        self.radius = 0.5      # Default size (for circle shape)
        self.width = 1.0       # Default width (for rectangle shape)
        self.height = 0.5      # Default height (for rectangle shape)
        self.mass = 1.0        # Default mass
        self.sensors = {}      # Dictionary to store sensors
        self.sim = None        # Reference to simulation

    def init_physics(self):
        # <--- Initialize physics body and shape --->
        if not self.sim:
            return
        
        # create physics body
        self.body = self.sim.physics_engine.create_body(
            self.mass, self.position
        )
        self.body.angle = self.orientation
        
        # create shape
        if self.shape == "circle":
            self.sim.physics_engine.create_circle_shape(
                self.body, self.radius
            )

        elif self.shape == "rectangle":
            self.sim.physics_engine.create_box_shape(
                self.body, (self.width, self.height)
            )

    def add_sensor(self, sensor, position):
        # <--- adding sesnsor to the robot --->
        sensor.robot = self
        sensor.position = position
        self.sensors[position] = sensor

    def move_forward(self, speed):
        # <--- moving forward at speed --->
        if self.body:
            angle = self.body.angle
            force = (
                speed * 100 * pymunk.vec2d.Vec2d(1, 0).rotated(angle)
            )
            self.body.apply_force_at_local_point(force, (0, 0))

    def turn(self, angle, rad=False):
        # <--- turn by angle --->
        if self.body:
            # Convert to radians
            angle = angle * (3.14159 / 180) if not rad else angle
            # Apply torque
            self.body.apply_torque(angle * 1000)

    def stop(self):
        # <--- stop all movement --->
        if self.body:
            self.body.velocity = (0, 0)
            self.body.angular_velocity = 0