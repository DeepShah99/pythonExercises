class Cookies:
    def __init__(self, colour):
        self.colour = colour
    
    def get_colour(self):
        return self.colour
    
    def change_colour(self, colour):
        self.colour = colour


cookie_one = Cookies("orange")
cookie_two = Cookies("yellow")

print("Cookie one is " + cookie_one.get_colour())
print("Cookie two is " + cookie_two.get_colour())
print("\n")

cookie_two.change_colour("blue")

print("Cookie one is still " + cookie_one.get_colour())
print("But Cookie two is " + cookie_two.get_colour())