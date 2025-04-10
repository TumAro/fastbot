class BaseSensor:
    def __init__(self):
        self.robot = None  # Reference to parent robot
        self.position = None  # Position name on robot
        
    @property
    def value(self):
        # <--- Get current sensor reading --->
        return self.get_reading()
        
    def get_reading(self):
        # <--- Get sensor reading (to be overridden by subclasses) --->
        return None
        
    @property
    def global_position(self):
        # <--- Get sensor position in world coordinates --->
        if not self.robot or not self.robot.body:
            return (0, 0)
            
        # Calculate offset based on position name
        offset = (0, 0)
        if self.position == "front":
            offset = (self.robot.radius, 0)
        elif self.position == "back":
            offset = (-self.robot.radius, 0)
        elif self.position == "left":
            offset = (0, self.robot.radius)
        elif self.position == "right":
            offset = (0, -self.robot.radius)
            
        # Transform to world coordinates
        return self.robot.body.local_to_world(offset)