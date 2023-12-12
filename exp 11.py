def is_rightangled(a, b, c):
    # Check if the triangle is right-angled using Pythagorean theorem
    sides = [a, b, c]
    sides.sort()

    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

def calculate_area(a, b, c):
    # Calculate the area using Heron's formula
    s = (a + b + c) / 2  # Semi-perimeter
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Get user input for the lengths of the sides
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

# Check if the triangle is right-angled
if is_rightangled(side_a, side_b, side_c):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")

# Calculate and display the area using Heron's formula
area = calculate_area(side_a, side_b, side_c)
print(f"The area of the triangle is: {area}")
