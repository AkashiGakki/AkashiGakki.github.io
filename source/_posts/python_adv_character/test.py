# class Solution:
#     def rotate(self, nums, k):
#         return nums[-k:] + nums[:-k]


# if __name__ == "__main__":
#     lst = Solution()
#     nums = [1, 2, 3, 4, 5, 6, 7]
#     k = 3
#     res = lst.rotate(nums, k)
#     print(res)
        

# class Bird:
#     def __init__(self):
#         self.hungry = True

#     def eat(self):
#         if self.hungry:
#             print('Aaaah...')
#             self.hungry = False
#         else:
#             print('No, thanks!')


# class SongBird(Bird):
#     def __init__(self):
#         super().__init__()
#         self.sound = 'Squawk!'
    
#     def sing(self):
#         print(self.sound)

# if __name__ == "__main__":
#     s = SongBird()
#     s.sing()
 

# def check_index(key):
#     if not isinstance(key, int):
#         raise TypeError
#     if key < 0:
#         raise IndexError

# class ArithmeticSequence:
#     def __init__(self, start=0, step=1):
#         self.start = start
#         self.step = step
#         self.changed = {}

#     def __getitem__(self, key):
#         check_index(key)
#         try:
#             return self.changed[key]
#         except KeyError:
#             return self.start + key * self.step

#     def __setitem__(self, key, value):
#         check_index(key)
#         self.changed[key] = value

# if __name__ == "__main__":
#     # 创建一个从1开始，步长为2的无穷序列
#     s = ArithmeticSequence(1, 2)
#     print(s[4])

# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0

#     def get_size(self):
#         return self.width, self.height

#     def set_size(self, size):
#         self.width, self.height = size

#     size = property(get_size, set_size)


# if __name__ == "__main__":
#     r = Rectangle()
#     r.width = 5
#     r.height = 10
#     print(r.size)


# class MyClass:
#     def smeth():
#         print('This is a static method')
#     smeth = staticmethod(smeth)

#     def cmeth(cls):
#         print('Tish is a class method of', cls)
#     cmeth = classmethod(cmeth)

# class MyClass:
#     @staticmethod
#     def smeth():
#         print('This is a static method')
    
#     @classmethod
#     def cmeth(cls):
#         print('Tish is a class method of', cls)

# if __name__ == "__main__":
#     MyClass.smeth()
#     MyClass.cmeth()

# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0

#     @property
#     def size(self):
#         return self.width, self.height

# if __name__ == "__main__":
#     r = Rectangle()
#     print(r.size)


# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0

#     @property
#     def size(self):
#         return self.width, self.height
    
#     @size.setter
#     def size(self, size):
#         self.width, self.height = size
    
# if __name__ == "__main__":
#     r = Rectangle()
#     r.width = 5
#     r.height = 10
#     print(r.size)


# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 1

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a

#     def __iter__(self):
#         return self

# if __name__ == "__main__":
#     fibs = Fibs()
#     for f in fibs:
#         print(f)
#         if f > 100:
#             break


# class TestIterator:
#     value = 0
#     def __next__(self):
#         self.value += 1
#         if self.value > 10:
#             raise StopIteration
#         return self.value
    
#     def __iter__(self):
#         return self

# if __name__ == "__main__":
#     t = TestIterator()
#     print(list(t))    

def flatten(nested):
    try:
        for sublist in nested:
            for element in sublist:
                yield element
    except TypeError:
        yield nested

# nested = [[[1], 2, 3], 4, 5, [6, 7]]
nested = [[1, 2], 3, 4, [5]]
print(list(flatten(nested)))
