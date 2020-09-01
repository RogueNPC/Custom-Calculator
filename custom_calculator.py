#rectangular prism surface area and volume calculator

#asking the user to input their variables
length = int(input('Input variable length: '))
width = int(input('Input variable width: '))
height = int(input('Input variable height: '))

#funtion to calculate surface area
def rectangular_prism_sa(length, width, height):
    surface_area = 2 * (length * width + length * height + width * height)
    return surface_area
#function to calculate volume
def rectangular_prism_vol(length, width, height):
    volume = length * width * height
    return volume

#prints out the results from the surface area and the volume functions
print(f"surface area of rectangular prism: {rectangular_prism_sa(length, width, height)} units squared")
print(f"volume of rectangular prism: {rectangular_prism_vol(length, width, height)} units cubed")