import pymunk

class PhysicsEngine:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)  # No gravity by default
        
    def step(self, dt):
        # <--- Advance physics simulation by dt seconds --->
        self.space.step(dt)
        
    def create_body(self, mass, position, moment=None):
        # <--- Create a physics body --->
        if moment is None:
            moment = pymunk.moment_for_box(mass, (1, 1))  # Default moment
            
        body = pymunk.Body(mass, moment)
        body.position = position
        self.space.add(body)
        return body
        
    def create_circle_shape(self, body, radius, offset=(0, 0)):
        # <--- Create a circle collision shape --->
        shape = pymunk.Circle(body, radius, offset)
        shape.friction = 0.5
        self.space.add(shape)
        return shape
        
    def create_box_shape(self, body, size, offset=(0, 0)):
        # <--- Create a box collision shape --->
        shape = pymunk.Poly.create_box(body, size, offset)
        shape.friction = 0.5
        self.space.add(shape)
        return shape