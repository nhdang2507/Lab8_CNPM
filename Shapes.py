class Shapes(object):
    def AreaOfSquare(side):
        Area = side*side
        print("\nArea of a Square is: %.2f" % Area)

    side = int(input('Please Enter the side of a Square: '))
    AreaOfSquare(side)
