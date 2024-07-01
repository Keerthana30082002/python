class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Create two instances of the Vector class
vector1 = Vector(3, 4)
vector2 = Vector(1, 2)

# Add the two vectors
result_addition = vector1 + vector2
print("Vector addition:", result_addition)

# Multiply one of the vectors by a scalar
scalar = 2
result_scalar_multiplication = vector1 * scalar
print("Scalar multiplication:", result_scalar_multiplication)

# Compare two vectors for equality
print("Vector equality:", vector1 == vector2)
