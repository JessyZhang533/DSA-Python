class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        " Return the color of the cookie. This method doesn't take arguments"
        return self.color

    def change_color(self, color):
        " Reset the color of the cookie.The only argument should be color"
        self.color = color


cookie_1 = Cookie('green')
cookie_2 = Cookie('blue')
cookie_2.change_color('yellow')  # Write the variable name 'cookie_2' before calling the method

print("Cookie 1 is {}.".format(cookie_1.get_color()))
print("Cookie 2 is now {}.".format(cookie_2.get_color()))
