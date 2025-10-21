class Bird:
    def sound(self):
        print("Birds make sounds")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

class Duck(Bird):
    def sound(self):
        print("Duck quacks")

for bird in [Sparrow(), Duck()]:
    bird.sound()
