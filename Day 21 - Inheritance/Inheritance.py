class Animal():
    def __init__(self):
        self.limbs = 4
    
    def breathe(self):
        print("Inhale... Exhale...")
        
    def move(self):
        print("Animal is running and jumping - having fun!")
    
    
class Fish(Animal):             # pass Animal as super class to inherit from it
    def __init__(self): 
        super().__init__()        # call the constructor function of super class in own constructor
        self.limbs = 0
        
    def breathe(self):
        super().breathe()
        print("Doing this underwater!")
                
    def move(self):
        print("Fish is swimmin' n chillin'")    # overriding a superclass function
        

animal = Animal()
fish = Fish()

print(animal.limbs, fish.limbs)

animal.breathe()
fish.breathe()

animal.move()
fish.move()