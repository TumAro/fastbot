"""
FastBot: A beginner-friendly 2D robotics simulation library
"""

__version__ = "0.1.0"

# Import main classes for easy access
from fastbot.core.simulation import Simulation
from fastbot.robots.base import Robot
from fastbot.sensors.base import Sensor

# Import modules
from fastbot import robots
from fastbot import sensors
from fastbot import physics
from fastbot import visualization

# Convenient factory functions
def create_simulation(**kwargs):
    """Create a new simulation with default settings."""
    return Simulation(**kwargs)

def create_robot(robot_type="differential_drive", **kwargs):
    """Create a robot of the specified type."""
    if robot_type == "differential_drive":
        from fastbot.robots.differential import DifferentialDriveRobot
        return DifferentialDriveRobot(**kwargs)
    else:
        raise ValueError(f"Unknown robot type: {robot_type}")