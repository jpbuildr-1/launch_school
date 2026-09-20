'''
given a triangle return one of the three types (equilateral, isosceles, scalene)

equilateral -> all side lengths are equal
isosceles   -> two side lengths are equal
scalene     -> all side lengths are not equal

A shape is a triangle when
1. All sides are greater than 0
2. Sum of any two sides are greater than 3rd side


ds: list of side lengths, ValueError if not a triangle, integers

CHECK IF SIDES GIVEN MAKE A TRIANGLE
DETERMINE IF ONE OF THE THREE TYPES
    If not triangle
        raise ValueError
    If equilateral
        return equilateral as a string
    If isosceles
        return isosceles as a string
    If scalene
        return scalene as a string
    
IS A TRIANGLE
    Set greatest_side to max of sides
    Set two_sides_only to an sum of sides subtract greatest
    Set minimum_side to min of sides
    If two_sides_only is less than or equal to greatest_side or minimum_side is less than zero
        Return False
    Return True

IS EQUILATERAL
    Return True if sum of all sides divided by 3 is equal to one side else False

IS ISOSCELES
    return True if first and second side are equal or first and third sides are equal or second and third side are equal else False

IS SCALENE
    return True if first and second are not equal and second and third are not equal and first and third are not equal

'''
class Triangle:
    def __init__(self, *sides):
        self._kind = self.set_triangle(sides)

    @property
    def kind(self):
        return self._kind

    def set_triangle(self, sides):
        if not self.is_triangle(sides):
            raise ValueError
        if self.is_equilateral(sides):
            return "equilateral"
        if self.is_isosceles(sides):
            return "isosceles"
        if self.is_scalene(sides):
            return "scalene"
            
    def is_triangle(self, sides):
        greatest_side = max(sides)
        two_sides_only = sum(sides) - greatest_side
        minimum_side = min(sides)

        if two_sides_only <= greatest_side or minimum_side < 0:
            return False
        return True

    def is_equilateral(self, sides):
        return sides[0] == sides[1] == sides[2]

    def is_isosceles(self, sides):
        return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]

    def is_scalene(self, sides):
        return sides[0] != sides[1] != sides[2]


    