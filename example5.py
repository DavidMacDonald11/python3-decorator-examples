class LineChar:
    objs = 0

    def __init__(self, string):
        LineChar.objs += 1
        self.string = string
        self.i = -1

    @property
    def my_char(self):
        self.i += 1
        return self.string[self.i]

    @my_char.setter
    def my_char(self, value):
        self.i = value

    @classmethod
    def get_count(cls):
        return cls.objs

    @classmethod
    @property
    def my_count(cls):
        return cls.objs

line = LineChar("ABCDEFG")
print(line.my_char, line.my_char, line.my_char)
line.my_char = -1
print(line.my_char)
print(LineChar.get_count(), LineChar.my_count)
