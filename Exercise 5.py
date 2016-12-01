# TODO: store the length and width in floating point variables 
#Assign values to length and width
length = input('How long is your rectangle in inches?')
width = input('How wide is your rectangle in inches?')
#Converts length and width into floats
length_count = float(length)
width_count = float(width)
# TODO: Use Python's arithmatic functions to multiply the length by the width, and assign the result to the variable named area
#Multiplies length float by width float
area = length_count * width_count

# TODO: Modify this line to print the area
#Prints out the result as a string
print('The area of your rectangle is '+ str(area) + ' square inches')
