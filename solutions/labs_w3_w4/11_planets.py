'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():

    def __init__(self, name, color, system):
        self.name = name
        self.color = color
        self.system = system

    def bears_life(self):
        if self.color.lower() == 'blue':
            return True
        else:
            return False

    def __str__(self):
        return f"Planet {self.name.title()} is a {self.color} planet in the {self.system}."


mars = Planet(name='mars', color='red', system='Solar System')
naboo = Planet('earth', 'blue', 'Naboo System')
earth = Planet('naboo', 'blue', 'Solar System')

print(mars)
print(mars.bears_life())
print(naboo)
print(naboo.bears_life())
print(earth)
print(earth.bears_life())

