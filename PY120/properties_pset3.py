class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

rectangle = Rectangle(1, 2)
print(rectangle.width)          # 1
print(rectangle.height)         # 2

rectangle.width = 8
# AttributeError