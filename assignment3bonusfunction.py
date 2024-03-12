class Vehicle:
    def __init__(self, name, color, speed, make, mileage):
        self.name = name
        self.color = color
        self.speed = speed
        self.make = make
        self.mileage = mileage


    def drive(self, minutes):
        minuteSpeed = self.speed / 60
        dist = minutes*minuteSpeed
        print("You drove for" +  str(minutes) + "minutes, and covered a total distance of " + str(dist) + "km")

        self.mileage += dist

        return dist

class Bus(Vehicle): #adding bus as a sub-class to vehicle
    
    def __init__(self, name, color, speed, make, capacity):
        self.name = name
        self.color = color
        self.speed = speed
        self.make = make
        self.mileage = 0
        self.capacity = capacity


bus = Bus("schoolbus", "yellow", 60, 2002, 24)

print(bus.color)
bus.drive(120)

bus2 = Bus("shuttle", "white", 80, 2022, 18)
bus2.drive(120)

#write your own module:
def add(x,y):
    return x+y
def mult(x,y):
    return x*y
def bungee(x,y, z = 12): # the user is allowed to put in three argument, but if they only put in two, the third will be defaulted to 12
    if y != 0:
        return(x*x)/y + z
    else: 
        return "That's illegal!"

class Jumper:

    def __init__(self, bungeeFactor):
        self.bungeefactor = bungeeFactor
    def jump (self, x, y):
        return bungee(x,y,self.bungeeFactor)
    



# if you save the above file as a separate file
# then in the future you can "import mathfunction as m"
# and then call m.add to use the add function. e.g., print(add(12,29)) and 41 will be printed, or print(bungee(2,3)), and 13.33 will be printed
# or put in "calra = m.Jumper(15)" then "clara.jump(2,3)", and get 16.333 
