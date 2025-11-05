import math

class ShapeError(Exception): pass
class InvalidTypeError(ShapeError): pass
class NonPositiveValueError(ShapeError): pass
class TriangleInequalityError(ShapeError): pass
class ScaleFactorError(ShapeError): pass


class Shape:
    """Base shape class with common validation."""
    @staticmethod
    def _ensure_number(value, name):
        if not isinstance(value, (int, float)):
            raise InvalidTypeError(f"'{name}' must be numeric. Got {type(value).__name__}")

    @staticmethod
    def _ensure_positive(value, name):
        Shape._ensure_number(value, name)
        if value <= 0:
            raise NonPositiveValueError(f"'{name}' must be > 0. Got {value}")

    def scale(self, factor):
        self._ensure_number(factor, "factor")
        if factor <= 0:
            raise ScaleFactorError("Scale factor must be > 0.")
        self._scale_impl(factor)


class Circle(Shape):
    def __init__(self, radius):
        self._ensure_positive(radius, "radius")
        self.radius = radius
    def area(self): return math.pi * self.radius ** 2
    def perimeter(self): return 2 * math.pi * self.radius
    def _scale_impl(self, f): self.radius *= f
    def __repr__(self): return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    def __init__(self, width, height):
        self._ensure_positive(width, "width")
        self._ensure_positive(height, "height")
        self.width, self.height = width, height
    def area(self): return self.width * self.height
    def perimeter(self): return 2 * (self.width + self.height)
    def _scale_impl(self, f):
        self.width *= f; self.height *= f
    def __repr__(self): return f"Rectangle(width={self.width}, height={self.height})"


class Triangle(Shape):
    def __init__(self, a, b, c):
        self._ensure_positive(a, "a")
        self._ensure_positive(b, "b")
        self._ensure_positive(c, "c")
        if not (a + b > c and a + c > b and b + c > a):
            raise TriangleInequalityError("Triangle inequality violated.")
        self.a, self.b, self.c = a, b, c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self): return self.a + self.b + self.c
    def _scale_impl(self, f):
        self.a *= f; self.b *= f; self.c *= f
    def __repr__(self): return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


if __name__ == "__main__":
    c = Circle(3)
    r = Rectangle(4, 6)
    t = Triangle(3, 4, 5)
    print(c, "area:", c.area())
    print(r, "perimeter:", r.perimeter())
    print(t, "area:", t.area())

