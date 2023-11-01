class shape():
    def area(self):
        raise NotImplementedError
    def display(self):
        raise NotImplementedError

class circle(shape):
    def area(self, r):
        self.r = r
    def display(self):
        print("THe area of the circle is ", 3.14* self.r * self.r)

class triagle(shape):
    def area(self, b, h):
        self.b = b
        self.h = h
    def display(self):
        print("The area of the triangle is ", 0.5 * self.b * self.h)

class rectangle(shape):
    def area(self,l,b):
        self.l = l
        self.b = b
    def display(self):
        print("The area of the rectangle is ", self.b* self.l)

obj_c = circle()
r = int(input("Enter Radius: "))
obj_c.area(r)
obj_c.display()
obj_t = triagle()
b= int(input("Enter the base for the triangle: "))
h = int(input("Enter the height for the triangle: "))
obj_t.area(b,h)
obj_t.display()
obj_r = rectangle()
l= int(input("Enter the length of the rectangle: "))
br= int(input("Enter the breadth of the rectangle: "))
obj_r.area(l,br)
obj_r.display()
