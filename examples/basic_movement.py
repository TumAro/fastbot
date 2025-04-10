from fastbot import Simulation, Robot

# Create simulation
sim = Simulation(realtime=True)

# Create robot
robot = Robot(position=(0, 0), orientation=0)
robot.shape = "circle"
robot.radius = 0.25

# Add robot to simulation
sim.add_robot(robot)

# Initialize physics
robot.init_physics()

# Start simulation
sim.start()

# Simple movement pattern
robot.move_forward(1.0)
sim.wait(2)  # Wait 2 seconds
robot.turn(90)  # Turn 90 degrees
sim.wait(1)  # Wait 1 second
robot.move_forward(1)  # Move forward 1 meters
sim.wait(3)  # Wait to see the results