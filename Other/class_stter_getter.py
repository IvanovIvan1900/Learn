import functools

#https://realpython.com/python-property/
# устанавливаем сеттер, геттер для свойства
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )

class CircleWichDecorator:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius

# делаем свойства только read_only
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

class PointWichValidations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"y" must be a number') from None

    # Computed Attributes
    @property
    def perimetr(self):
        return self._x*2+self._y*2

    @functools.cached_property
    def perimetr_cached(self):
        return self._x*2+self._y*2

    # Another common use case of properties is to provide an auto-formatted value for a given attribute
    @property
    def get_x_format(self):
        return f'x = {self._x:} '

if __name__ == "__main__":
    circle = CircleWichDecorator(42.0)
    print(circle.radius)
    circle.radius = 100.0
    del circle.radius

    point = PointWichValidations(12, 5)
    print(point.perimetr)
    print(point.get_x_format)
    # point.x = "one"

    # point = Point(12, 5)
    # point.x
    # point.y
    # point.x = 45
