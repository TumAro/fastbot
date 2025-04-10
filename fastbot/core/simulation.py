import time
from fastbot.physics.engine import PhysicsEngine
from fastbot.visualisation.renderer import Renderer

class Simulation:
    def __init__(self, realtime=True):
        self.physics_engine = PhysicsEngine()
        self.renderer = Renderer(width=800, height=600)
        self.realtime = realtime
        self.running = False
        self.dt = 1/60  # 60 FPS
        self.objects = []
        
    def add_object(self, obj):
        # <--- Add an object to the simulation --->
        self.objects.append(obj)
        
    def add_robot(self, robot):
        # <--- Add a robot to the simulation --->
        robot.sim = self
        self.add_object(robot)
        
    def start(self):
        # <--- Start the simulation loop --->
        self.running = True
        self._run_loop()
        
    def stop(self):
        # <--- Stop the simulation --->
        self.running = False
        
    def step(self):
        # <--- Run a single simulation step --->
        self.physics_engine.step(self.dt)
        for obj in self.objects:
            obj.update(self.dt)
        self.renderer.render(self.objects)
        
    def wait(self, seconds):
        # <--- Wait for the specified number of seconds --->
        if self.realtime:
            time.sleep(seconds)
        else:
            steps = int(seconds / self.dt)
            for _ in range(steps):
                self.step()
                
    def _run_loop(self):
        # <--- Main simulation loop --->
        last_time = time.time()
        
        while self.running:
            # Calculate time delta
            current_time = time.time()
            elapsed = current_time - last_time
            last_time = current_time
            
            # Process events (quit, etc.)
            if not self.renderer.process_events():
                self.running = False
                break
                
            # Run simulation step
            self.step()
            
            # Sleep to maintain framerate if realtime
            if self.realtime:
                sleep_time = max(0, self.dt - elapsed)
                time.sleep(sleep_time)