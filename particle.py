# Particle

# Import Libraries
import pygame
from vector import Vector2D

# Determines Particle Color Based on Applied Force
def force_color(particle, max_force=5000):
    force_mag = particle.acceleration.magnitude() * particle.mass  # Compute force magnitude
    intensity = min(force_mag / max_force, 1.0)  # Normalize intensity between 0 and 1
    red = int(255 * intensity)  # More Force → More Red
    green = int(255 * (1 - intensity))  # Less Force → More Green
    blue = 0  # No Blue
    return (red, green, blue)

# Particle Class
class Particle:
    def __init__(self, position, radius, mass=1):
        # Particle Properties
        self.position = position  
        self.velocity = Vector2D() 
        self.acceleration = Vector2D() 
        self.radius = radius 
        self.mass = mass 
        self.restitution = 0.95  # Energy retention during collisions

    # Applies Force to the Particle, Updating Acceleration Based on N2L (F = ma)
    def apply_force(self, force):
        self.acceleration += force * (1 / self.mass)

    # Updates Position Using Velocity-Verlet Integration
    def update_position(self, dt):
        self.position += self.velocity * dt + self.acceleration * (0.5 * dt * dt)

    # Updates Velocity Using Velocity-Verlet Integration
    def update_velocity(self, new_acceleration, dt):
        self.velocity += (self.acceleration + new_acceleration) * (0.5 * dt)
        self.acceleration = new_acceleration

    # Computes Kinetic Energy of the Particle (KE = 1/2 m v^2)
    def kinetic_energy(self):
        return 0.5 * self.mass * self.velocity ** 2

    # Draws Particle on the Screen
    def draw(self, screen):
        color = force_color(self)
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius)
