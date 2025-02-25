# Force Calculation

# Import Vector
from vector import Vector2D

# Computes the Lennard-Jones Force Between Two Particles
def lennard_jones_force(p1, p2, epsilon=1, sigma=17.82, cutoff=100, max_force=5000):
    r_vector = p2.position - p1.position  # Relative position vector
    r = r_vector.magnitude()  # Distance between particles

    # If Particles are Beyond Cutoff Distance or Overlapping, No Need
    if r > cutoff or r == 0:
        return Vector2D(0, 0), Vector2D(0, 0)

    # Precompute Powers
    r7 = r ** 7
    r13 = r ** 13
    sig6 = sigma ** 6
    sig12 = sigma ** 12

    # Compute Lennard-Jones Force Magnitude
    force_mag = 48 * epsilon * ((sig12 / r13) - (sig6 / (2 * r7)))

    # Cap The Force to Prevent Instability
    force_mag = min(force_mag, max_force)

    # Compute Force Vector Along the Normal
    force_vector = r_vector.normalized() * force_mag

    # Return Equal and Opposite Forces Acting on Both Particles
    return force_vector, force_vector * -1
