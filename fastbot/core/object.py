class Object:
    def __init__(self, position=(0,0), orientation=0):
        self.position = position
        self.orientation = orientation

        # physics body will be added later
        self.body = None

    def update(self, dt):
        if self.body:
            self.position = self.body.position
            self.orientation = self.body.angle