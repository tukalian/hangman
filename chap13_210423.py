# 継承

class Shape:    # 親クラス
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("{} by {}".format(self.width, self.len))


class Square(Shape):    # 子クラス
    def area(self):
        return self.width * self.len

a_square_1 = Square(40, 20)
a_square_2 = Square(80, 20)

print(a_square_1.area())
print(a_square_2.area())