class School:
    def __init__(self):
        self.faculty = []

    def work(self):
        for member in self.faculty:
            print(member.working())

    def __add__(self, faculty):
        if not isinstance(faculty, Teacher) and not isinstance(faculty, Counselor):
            return NotImplemented

        self.faculty += [faculty]

        return self

class Teacher:
    def working(self):
        return self.grades_students()

    def grades_students(self):
        return f"Grading students."

class Counselor:
    def working(self):
        return self.advise_students()

    def advise_students(self):
        return f"Counseling students."

school = School()
billy = Teacher()
bob = Counselor()
school += billy
school += bob
school.work()


class SpeakMixin:
    def speak(self):
        return "speaking"

class Person(PersonMixIn):
    pass

class Pet(SpeakMixin):
    pass

class Cat:
    pass

class SwimMixin:
    def swim(self):
        return "swimming."

class Fish(SwimMixin, Pet):
    pass
