#Write a Python program that declares a class describing your favorite animal
#Have the data members of the class represent the following physical parameters of the animal:
#length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool) 
#Write an initialization function that sets the values of the data members when an instance of the class is created. 
#Write a member function of the class to print out and describe the data members 
#representing the physical characteristics of the animal.

class Flyings_squirrel:
    
    def __init__(self, arms, legs, eyes, tail, fur):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes 
        self.tail = tail
        self.fur = fur

    def measurements(self):
        print('Measurements of a flying squirrel')
        print(f'Arm length: {self.arms} in')
        print(f'Leg length: {self.legs} in')
        print(f'Number of eyes: {self.eyes}')
        # Bool=True or false / yes or no 
        #shows how to do bool 
        if self.tail:
            print('Has a Tail: YES')
        else:
            print('Has a tail: NO')

        if self.fur:
            print('Does it have fur?: YES')
        else:
            print('Does it have fur?: NO')

favorite_animal = Flyings_squirrel(3.1, 2.5, 2, True, True)
favorite_animal.measurements()
		
