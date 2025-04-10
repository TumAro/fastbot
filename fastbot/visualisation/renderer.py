import pygame

class Renderer:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("FastBot Simulation")
        self.clock = pygame.time.Clock()
        
    def process_events(self):
        # <--- Process pygame events, return False if should quit --->
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
        
    def render(self, objects):
        # <--- Render all objects in the simulation --->
        # Clear screen
        self.screen.fill((255, 255, 255))
        
        # Draw all objects
        for obj in objects:
            self._draw_object(obj)
            
        # Update display
        pygame.display.flip()
        self.clock.tick(60)
        
    def _draw_object(self, obj):
        # <--- Draw a single object --->
        if hasattr(obj, 'shape') and obj.shape:
            # Convert simulation coordinates to screen coordinates
            x, y = obj.position
            screen_x = int(x * 50 + self.width/2)
            screen_y = int(self.height/2 - y * 50)
            
            # Draw based on shape type
            if obj.shape == "circle":
                pygame.draw.circle(
                    self.screen, 
                    (0, 0, 255), 
                    (screen_x, screen_y), 
                    int(obj.radius * 50)
                )
            elif obj.shape == "rectangle":
                rect = pygame.Rect(
                    screen_x - int(obj.width * 25),
                    screen_y - int(obj.height * 25),
                    int(obj.width * 50),
                    int(obj.height * 50)
                )
                pygame.draw.rect(self.screen, (0, 0, 255), rect)