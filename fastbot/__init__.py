"""
FastBot: A beginner-friendly 2D robotics simulation library
"""

__version__ = "0.1.0"

from fastbot.core.simulation import Simulation
from fastbot.core.object import Object
from fastbot.robots.base import Robot

# Import subpackages for namespace organization
from fastbot import sensors
from fastbot import robots