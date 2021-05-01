# class

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

or1 = Orange(4, "light orange")
print(or1.weight)
print(or1.color)
or1.weight = 100

or2 = Orange(8, "dark orange")
or3 = Orange(14, "yellow")

print(or1.weight)
print(or1.color)
print(or2.weight)
print(or2.color)
print(or3.weight)
print(or3.color)