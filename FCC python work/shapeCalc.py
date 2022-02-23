class Rectangle:
    num_shapes = 0

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, value):
        self.width = value
    
    def set_height(self, value):
        self.height = value

    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return (2*self.width) + (2*self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height>50:
            return 'Too big for picture.'
        else:
            picture = ''
            for i in range(self.height):
                picture += '*' * (self.width) + '\n'
            return picture
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def get_amount_inside(self, item):
        count = 0
        if item.height>self.height or item.width>self.width:
            return count
        else:
            count = (self.height//item.height) * (self.width//item.width)
        return count

class Square(Rectangle):
    def __init__(self, sidelength ) -> None:
        super().__init__(sidelength, sidelength)
        self.side = sidelength

    def set_side(self, value):
        self.side = value
        self.width = value
        self.height = value

    def set_width(self, value):
        self.side = value
        self.width = value
        self.height = value
    
    def set_height(self, value):
        self.side = value
        self.width = value
        self.height = value

    def __str__(self):
        return f'Square(side={self.side})'
    




rect = Rectangle(4,4)
sq = Square(4)

print(rect.get_amount_inside(sq))
