# isキーワード

class Person:
    def __int__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

anather_bob = Person()
print(bob is anather_bob)
