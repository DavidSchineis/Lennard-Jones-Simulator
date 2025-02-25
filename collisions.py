# Collision Handling

# Collision Detection by Distance Check
def check_collision(particle1, particle2):
    distance_sq = (particle1.position - particle2.position).magnitude_squared()
    radii_sum_sq = (particle1.radius + particle2.radius) ** 2
    return distance_sq < (radii_sum_sq * 0.95)  # Determines if particles are touching


# Collision Resolution by Impulse
def resolve_collision(particle1, particle2, max_impulse=50):

    # Compute Normal
    normal = (particle2.position - particle1.position).normalized()
    relative_velocity = particle2.velocity - particle1.velocity
    velocity_along_normal = relative_velocity.dot(normal)

    # If Particles are Separating, No Need
    if velocity_along_normal > 0:
        return

    # Compute Restitution
    restitution = min(particle1.restitution, particle2.restitution)  
    impulse_magnitude = -(1 + restitution) * velocity_along_normal
    impulse_magnitude /= (1 / particle1.mass + 1 / particle2.mass)

    # Cap Impulse Magnitude to Avoid Jitters
    impulse_magnitude = min(impulse_magnitude, max_impulse)
    impulse = normal * impulse_magnitude

    # Apply Impulse to Velocities
    particle1.velocity -= impulse * (1 / particle1.mass)
    particle2.velocity += impulse * (1 / particle2.mass)


# Positional Correction to Prevent Object Sinking
def positional_correction(particle1, particle2):
    correction_factor = 0.2  # Controls how much correction
    slop = 0.05  # Prevents unnecessary micro-adjustments
    normal = (particle2.position - particle1.position).normalized()
    penetration_depth = (particle1.radius + particle2.radius) - (particle1.position - particle2.position).magnitude()

    # Shifts Particles Apart Slightly After Collisions
    if penetration_depth > slop:
        correction = normal * (penetration_depth * correction_factor)
        total_mass = particle1.mass + particle2.mass

        # Distribute Correction Based on Mass
        particle1.position -= correction * (particle2.mass / total_mass)
        particle2.position += correction * (particle1.mass / total_mass)

# Wall Restitution Values
WALL_RESTITUTION = {
    "top": 0.9,
    "bottom": 0.9,
    "left": 0.9,
    "right": 0.9
}

# Wall Collision Handling
def handle_wall_collision(particle, screen_width, screen_height, damping_factor=0.9):

    # Top Wall Collision
    if particle.position.y - particle.radius < 0:
        particle.velocity.y = -particle.velocity.y * WALL_RESTITUTION["top"] * damping_factor
        particle.position.y = particle.radius

    # Bottom Wall Collision
    elif particle.position.y + particle.radius > screen_height:
        particle.velocity.y = -particle.velocity.y * WALL_RESTITUTION["bottom"] * damping_factor
        particle.position.y = screen_height - particle.radius

    # Left Wall Collision
    if particle.position.x - particle.radius < 0:
        particle.velocity.x = -particle.velocity.x * WALL_RESTITUTION["left"] * damping_factor
        particle.position.x = particle.radius

    # Right Wall Collision
    elif particle.position.x + particle.radius > screen_width:
        particle.velocity.x = -particle.velocity.x * WALL_RESTITUTION["right"] * damping_factor
        particle.position.x = screen_width - particle.radius
