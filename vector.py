# Vector Class
class Vector2D:
    # Initialize Vector Components
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Adds Two Vectors
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # Subtracts Two Vectors
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    # Scales Vector by a Scalar
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    # Computes Dot Product Between Two Vectors
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Computes the Magnitude of the Vector
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    # Computes the Squared Magnitude
    def magnitude_squared(self):
        return self.x ** 2 + self.y ** 2

    # Returns a Normalized Version of the Vector (Unit Vector)
    def normalized(self):
        mag = self.magnitude()
        return Vector2D(self.x / mag, self.y / mag) if mag > 0 else Vector2D()
