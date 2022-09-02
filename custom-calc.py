# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

# calculates the peak rainfall discharge, Q = CiA
# Q = peak discharge
# C = runoff coefficient
# i = intensity
# A = area

def peak_discharge(runoff, intensity, area):
    return (runoff * intensity * area)

# notifies user about purpose of this calculator
print("Calculate The Peak Rainfall Discharge From Drainage Areas")

# collects information on land type
land_type = input("What is the land type? (Rural or Urban)? ")

# receives runoff input and converts to float/number
runoff = float(input("What is the Runoff Coefficient? (value between 0.0 and 1.0) "))


# receives intensity input and converts to float/number
intensity = float(input("What is the rainfall intensity? (value between 1.0 and 10.0) "))


# receives area input and converts to float/number
area = float(input("What is the drainage area? (any positive value) "))


# prints peak discharge value based on user input
print(f"Peak rainfall discharge for the {land_type} drainage area with a runoff coefficient of {runoff}, a rainfall intensity of {intensity} inches per hour, \nand a drainage area of {area} acres is {peak_discharge(runoff, intensity, area)} cubic feet per second")

