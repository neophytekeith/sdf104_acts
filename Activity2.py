oneCanCoverage = 5 #coverage san usad na can

height = int(input("enter the height: ")) #request san user input for height
width = int(input("enter the width: ")) #request san user input for width

#formula para icalculate an need bakalon na pinta
def formula(height, width):
    numOfCans = height * width / oneCanCoverage
    return numOfCans

#displaying part
print(f"You will need {round(formula(height, width))} cans of paint.") #gamit an function round para ma round up/off

#codenikeith
