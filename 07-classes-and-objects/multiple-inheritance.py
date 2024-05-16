'''
in OO Python we may exploit inheritance to build relationships between various classes
to cut down on code duplication
and to make our code easily extendable in future
this is represented as a parent to child relationship
where the child class inherits all of the state and behaviour of the parent class
and then... either
does/has extra stuff
or does stuff differently
if a child class does no extra stuff or nothing differently
there is little point in its existence
in Python, inhertance may be from MULTIPLE parents
'''

class Human:
    def __init__(self, head_size, BMI):
        self.head_size = head_size
        self.BMI = BMI
    
class CarbonLifeForm:
    def __init__(self,cellular_composition, water_content ):
        self.cellular_composition = cellular_composition
        self.water_content = water_content

class ChildHuman(Human, CarbonLifeForm):
    def __init__(self, head_size, BMI, cellular_composition, water_content):# the ONE self, the new, sub-class self
        # super().__init__(head_size, BMI) # self not required in call to ONE superclass only (Human)
        # but calling multiple superclasses requires qualifying with each class name
        Human.__init__(self, head_size, BMI) # calling method directly on class so requires the self from that class
        CarbonLifeForm.__init__(self, cellular_composition, water_content) # and the self from the other class
    

child1 = ChildHuman(21.0, 5.5, "Nitrogen, Oxygen", "50%")
print(child1.cellular_composition)
print(child1.water_content)
print(child1.head_size)
print(child1.BMI)


# print(child1.cellular_composition)
# print(child1.water_content)