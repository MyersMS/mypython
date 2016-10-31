print "\t\t*Area & Perimeter of a Rectangle*"

Length = raw_input("\nPlease enter the length of the rectangle: ")

while not Length:
    Length = raw_input("Please enter the length of the rectangle: ")

Length = float(Length)

Width = raw_input("Please enter the width of the rectangle: ")

while not Width:
    Width = raw_input("Please enter the width of the rectangle: ")

Width = float(Width)

Area = Length * Width

print "\nThe Area =", Length, "x", Width
print "The Area =", Area

raw_input("\nPress enter for the Perimeter.")

Length_2 = 2 * Length
Width_2 = 2 * Width
Perimeter = Length_2 + Width_2

print "\nThe Perimeter = 2(", Length, ") + 2(", Width, ")"
print "The Perimeter =", Length_2, "+", Width_2
print "The Perimeter =", Perimeter

raw_input("\nPress enter to exit.")
