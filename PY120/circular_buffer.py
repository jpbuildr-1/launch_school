'''
Create a class called  `CircularBuffer`
`put` to add object to the `CircularBuffer` instance
`get` to remove (and return) oldest object in the `CircularBuffer` instance
None of the values would be `None` except if they are empty spots

ds: class, list (keeps order of buffer) cap at buff limit, 

CREATE A LIST OF OBJECTS
PUT OBJECT AT CURRENT POSITION
GET OBJECT FROM OLDEST POSITION AND CHANGE OBJECT IN LIST TO NONE
    dunder init has self and capacity parameter
        set the instance variable capacity to capacity
        set the instance variable objects to a list containing `None` multiplied by capacity
        set the oldest_position instance variable to 0
        set the current_position instance variable to 0

    get instance method has self parameter
        if any objects are not None
            set old_object to object at oldest_position
            set object at oldest_position to None
            update oldest_position
            return old_object
        otherwise return None

    put instance method has self and new_object parameters
        if all objects are not None
            update oldest_position
        set object at current_position equal to new_object
        update current_position
            
    update_position function:
    if position + 1 equal to the capacity set to 0 otherwise add 1 to position


'''
class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.objects = [None] * capacity
        self.oldest_position = 0
        self.current_position = 0

    def get(self):
        if self.any_object():
            old_object = self.objects[self.oldest_position]
            self.objects[self.oldest_position] = None
            self.oldest_position = self.update_position(self.oldest_position)
            return old_object
    
    def put(self, new_object):
        if self.all_objects():
            self.oldest_position = self.update_position(self.oldest_position)
        self.objects[self.current_position] = new_object
        self.current_position = self.update_position(self.current_position)

    def update_position(self, position):
        if position + 1 == self.capacity:
            position = 0
        else:
            position += 1
        return position   

    def any_object(self):
        for obj in self.objects:
            if obj is not None:
                return True
        return False

    def all_objects(self):
        for obj in self.objects:
            if obj is None:
                return False
        return True


buffer = CircularBuffer(3)
# [None, None, None]
# oldest_position = 0
# current_position = 0

print(buffer.get() is None)          # True
# [None, None, None]
# oldest_position = 0
# current_position = 0

buffer.put(1)
# [1, None, None]
# oldest_position = 0
# current_position = 1

buffer.put(2)
# [1, 2, None]
# oldest_position = 0
# current_position = 2

print(buffer.get() == 1)             # True
# [None, 2, None]
# oldest_position = 1
# current_position = 2

buffer.put(3)
# [None, 2, 3]
# oldest_position = 1
# current_position = 0

buffer.put(4)
# [4, 2, 3]
# oldest_position = 1
# current_position = 1

print(buffer.get() == 2)             # True
# [4, None, 3]
# oldest_position = 2
# current_position = 1

buffer.put(5)
# [4, 5, 3]
# oldest_position = 2
# current_position = 2

buffer.put(6)
# [4, 5, 6]
# oldest_position = 0
# current_position = 0

buffer.put(7)
# [7, 5, 6]
# oldest_position = 1
# current_position = 1

print(buffer.get() == 5)             # True
# [7, None, 6]
# oldest_position = 2
# current_position = 1

print(buffer.get() == 6)             # True
# [7, None, None]
# oldest_position = 0
# current_position = 1

print(buffer.get()== 7)             # True
# [None, None, None]
# oldest_position = 1
# current_position = 1

print(buffer.get() is None)          # True
# [None, None, None]
# oldest_position = 1
# current_position = 1


buffer2 = CircularBuffer(4)
# [None, None, None, None]
# oldest_position = 0
# current_position = 0

print(buffer2.get() is None)         # True
# [None, None, None, None]
# oldest_position = 0
# current_position = 0

buffer2.put(1)
# [1, None, None, None]
# oldest_position = 0
# current_position = 1

buffer2.put(2)
# [1, 2, None, None]
# oldest_position = 0
# current_position = 2

print(buffer2.get() == 1)            # True
# [None, 2, None, None]
# oldest_position = 1
# current_position = 2

buffer2.put(3)
# [None, 2, 3, None]
# oldest_position = 1
# current_position = 3

buffer2.put(4)
# [None, 2, 3, 4]
# oldest_position = 1
# current_position = 0

print(buffer2.get() == 2)            # True
# [None, None, 3, 4]
# oldest_position = 2
# current_position = 0

buffer2.put(5)
# [5, None, 3, 4]
# oldest_position = 2
# current_position = 1

buffer2.put(6)
# [5, 6, 3, 4]
# oldest_position = 2
# current_position = 2

buffer2.put(7)
# [5, 6, 7, 4]
# oldest_position = 3
# current_position = 3

print(buffer2.get() == 4)            # True
# [5, 6, 7, None]
# oldest_position = 0
# current_position = 0

print(buffer2.get() == 5)            # True
# [None, 6, 7, None]
# oldest_position = 1
# current_position = 1

print(buffer2.get() == 6)            # True
# [None, None, 7, None]
# oldest_position = 2
# current_position = 2

print(buffer2.get() == 7)            # True
# [None, None, None, None]
# oldest_position = 0
# current_position = 0

print(buffer2.get() is None)         # True
# [None, None, None, None]
# oldest_position = 0
# current_position = 0