"""
LJ-Simulator: 2D Lennard-Jones Potential Simulation
Author: David Schineis
Description: A 2D Lennard-Jones simulator implemented in Python
"""

# Import Libraries
import os; os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
import random
from particle import Particle
from vector import Vector2D
from forces import lennard_jones_force
from collisions import check_collision, resolve_collision, positional_correction, handle_wall_collision

# Simulation Parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500  # Dimensions of the window
NUM_PARTICLES = 150  # Total number of particles
DT = 0.01  # Time step

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("LJ Simulator")

# Create Particles
particles = []
for _ in range(NUM_PARTICLES):
    pos = Vector2D(random.randint(10, SCREEN_WIDTH - 10), random.randint(10, SCREEN_HEIGHT - 10)) # Random initial postion
    radius = 5  # Particle size
    mass = 5  # Particle mass 
    velocity = Vector2D(random.uniform(-10, 10), random.uniform(-10, 10))  # Random initial velocity
    particle = Particle(pos, radius, mass)
    particle.velocity = velocity 
    particles.append(particle)

# Main Simulation Loop
running = True
frame_count = 0
while running:

    # Handle Pygame Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Particle Positions Using Velocity-Verlet Integration
    for p in particles:
        p.update_position(DT)

    # Handle Wall Collisions
    for p in particles:
        handle_wall_collision(p, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Initialize Forces
    new_forces = {p: Vector2D(0, 0) for p in particles}

    # Compute Lennard-Jones Forces and Resolve Collisions
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            force_i, force_j = lennard_jones_force(particles[i], particles[j])
            
            # Compute Forces Acting on Each Particle
            new_forces[particles[i]] += force_i
            new_forces[particles[j]] += force_j

            # Check and Resolve Particle Collisions
            if check_collision(particles[i], particles[j]):
                resolve_collision(particles[i], particles[j])
                positional_correction(particles[i], particles[j])

    # Compute New Accelerations 
    new_accelerations = {p: new_forces[p] * (1 / p.mass) for p in particles}

    # Update Velocities Using Velocity-Verlet Integration
    for p in particles:
        p.update_velocity(new_accelerations[p], DT)

    # Draw Simulation Frame
    screen.fill((0, 0, 0))  # Clear screen before rendering
    for p in particles:
        p.draw(screen)  # Render each particle

    # Update Display and Control Frame Rate
    pygame.display.flip()
    pygame.time.delay(1)
    frame_count += 1

# Exit Pygame
pygame.quit()
