# Label 1 Object oriented program last April 27.
def Sample():
    print("Week 2 Act.3 Object oriented program")

# Label 2
def show_line():
    print("-" * 30)


class Person:
    def __init__(self, name):
        self.name = name

    # condition 1
    def say_name(self):
        return f"My name is {self.name}"

    # condition 2
    def change_name(self, new_name):
        self.name = new_name

    # comdition 3
    def introduce(self):
        return f"Hi, I'm {self.name}. Glad to meet you!"


# Program starts here edited last April 27,2026
Sample()
show_line()

p = Person("Darling")
print(p.say_name())
print(p.introduce())

p.change_name(" Darling Lywin")
print(p.introduce())