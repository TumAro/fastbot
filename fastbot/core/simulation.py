"""
Core simulation class for FastBot
"""
import time
import pygame

from fastbot.physics.engine import PhysicsEngine
from fastbot.visualization.renderer import Renderer


class Simulation:
    """
    The main simulation class that coordinates physics, visualization, and robot control.
    
    This is the central controller for the entire simulation system.
    """
    
    def __init__(self, realtime=True, width=800, height=600, 
                 physics_timestep=1/60, max_fps=60):
        """
        Initialize a new simulation.
        
        Args:
            realtime (bool): Whether to run in realtime or step-by-step
            width (int): Width of the visualization window in pixels
            height (int): Height of the visualization window in pixels
            physics_timestep (float): Fixed timestep for physics updates (in seconds)
            max_fps (int): Maximum frames per second for visualization
        """
        self.realtime = realtime
        self.running = False
        self.physics_timestep = physics_timestep
        self.max_fps = max_fps
        
        # Initialize physics engine
        self.physics_engine = PhysicsEngine()
        
        # Initialize visualization if realtime
        if self.realtime:
            self.renderer = Renderer(width, height)
        else:
            self.renderer = None
            
        # Lists to track objects in the simulation
        self.robots = []
        self.obstacles = []
        self.sensors = []
        self.objects = []  # All physical objects
        
    def add_robot(self, robot):
        """
        Add a robot to the simulation.
        
        Args:
            robot: The robot object to add
        """
        self.robots.append(robot)
        self.objects.append(robot)
        robot.simulation = self
        robot.init_physics(self.physics_engine)
        
    def add_obstacle(self, obstacle_type, position, size=(1, 1), **kwargs):
        """
        Add an obstacle to the simulation.
        
        Args:
            obstacle_type (str): Type of obstacle ("box", "circle", etc.)
            position (tuple): (x, y) position
            size (tuple): (width, height) or radius for the obstacle
            **kwargs: Additional parameters for the obstacle
        """
        # Create obstacle (placeholder implementation)
        from fastbot.core.object import PhysicalObject
        obstacle = PhysicalObject(position=position)
        
        # Add to lists
        self.obstacles.append(obstacle)
        self.objects.append(obstacle)
        
        # Initialize physics
        obstacle.init_physics(self.physics_engine)
        
    def create_environment(self, env_type, size=(10, 10)):
        """
        Create a predefined environment.
        
        Args:
            env_type (str): Type of environment ("empty", "room", etc.)
            size (tuple): (width, height) of the environment in meters
        """
        # Clear existing environment
        # Add walls and obstacles based on env_type
        if env_type == "empty":
            # Just create boundaries
            self._create_boundaries(size)
        elif env_type == "room":
            # Create boundaries and some obstacles
            self._create_boundaries(size)
            self.add_obstacle("box", position=(size[0]/4, size[1]/4), size=(1, 1))
            self.add_obstacle("box", position=(3*size[0]/4, 3*size[1]/4), size=(1, 1))
        else:
            raise ValueError(f"Unknown environment type: {env_type}")
    
    def _create_boundaries(self, size):
        """Create boundary walls for the environment"""
        # Add four walls (placeholder implementation)
        wall_thickness = 0.1
        
        # Bottom wall
        self.add_obstacle("box", position=(size[0]/2, 0), 
                         size=(size[0], wall_thickness))
        # Top wall
        self.add_obstacle("box", position=(size[0]/2, size[1]), 
                         size=(size[0], wall_thickness))
        # Left wall
        self.add_obstacle("box", position=(0, size[1]/2), 
                         size=(wall_thickness, size[1]))
        # Right wall
        self.add_obstacle("box", position=(size[0], size[1]/2), 
                         size=(wall_thickness, size[1]))
    
    def start(self):
        """Start the simulation"""
        if self.realtime:
            self.running = True
            self._run_realtime()
        else:
            # Just set running state for step-by-step mode
            self.running = True
    
    def stop(self):
        """Stop the simulation"""
        self.running = False
    
    def step(self):
        """
        Step the simulation forward one physics timestep.
        Only used in non-realtime mode.
        """
        if not self.running:
            return
        
        # Step physics
        self.physics_engine.step(self.physics_timestep)
        
        # Update all objects
        for obj in self.objects:
            if hasattr(obj, 'update'):
                obj.update(self.physics_timestep)
    
    def wait(self, seconds):
        """
        Wait for the specified number of seconds.
        In realtime mode, actually wait. In step mode, just step forward.
        
        Args:
            seconds (float): Seconds to wait
        """
        if self.realtime:
            start_time = time.time()
            while time.time() - start_time < seconds and self.running:
                # Process events to keep the window responsive
                self._process_events()
                time.sleep(0.01)
        else:
            # Step forward physics steps equivalent to the time
            steps = int(seconds / self.physics_timestep)
            for _ in range(steps):
                self.step()
    
    def _run_realtime(self):
        """Run the simulation in realtime mode"""
        clock = pygame.time.Clock()
        
        while self.running:
            # Process events
            self._process_events()
            
            # Step physics
            self.physics_engine.step(self.physics_timestep)
            
            # Update all objects
            for obj in self.objects:
                if hasattr(obj, 'update'):
                    obj.update(self.physics_timestep)
            
            # Render frame
            self.renderer.render(self.objects)
            
            # Cap framerate
            clock.tick(self.max_fps)
    
    def _process_events(self):
        """Process pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # Add other event handling (keyboard, mouse, etc.)