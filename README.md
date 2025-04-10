# FastBot

A beginner-friendly 2D robotics simulation library. FastBot makes robotics accessible to non-engineers by providing a simple, intuitive interface for creating and controlling virtual robots.

## Features

- **Simple API**: Create robots and environments with just a few lines of code
- **Physics-based**: Realistic 2D physics using Pymunk/Pygame
- **Sensor Integration**: Easy-to-use distance sensors, cameras, and more
- **Control Systems**: Built-in PID controllers and basic motion planning
- **Visualization**: Real-time visualization with minimal setup

## Quick Start

```python
from fastbot import Simulation, Robot, sensors

# Create a simulation
sim = Simulation()

# Add a robot with sensors
robot = Robot.create("differential_drive")
robot.add_sensor(sensors.Distance(position="front"))

# Create a simple environment
sim.create_environment("empty_room", size=(10, 10))

# Run the simulation
sim.start()

# Move the robot
robot.move_forward(1.0)  # Move forward 1 meter
robot.turn(90)  # Turn 90 degrees

# Access sensor data
distance = robot.sensors["front"].value
if distance < 0.5:  # If obstacle closer than 0.5 meters
    robot.stop()
```

## Installation

```bash
pip install fastbot
```

## Documentation

- [API Documentation](docs/API.md)
- [Examples](examples/)
- [Tutorials](docs/tutorials/)

## Who is this for?

- Students learning robotics fundamentals
- Educators teaching robotics concepts
- Hobbyists interested in robotics without hardware
- Anyone who wants a simple platform to experiment with robot control

## Why FastBot2D?

Most robotics frameworks have steep learning curves and require engineering backgrounds. FastBot2D focuses on making robotics concepts accessible through:

1. Simplified API design
2. Visual feedback from the first line of code
3. Hiding unnecessary complexity
4. Focusing on core robotics concepts

## Project Status

FastBot2D is in early development. Feedback and contributions welcome!