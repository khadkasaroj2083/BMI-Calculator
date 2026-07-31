def calculate_BMI():
    height = float(input("Your height in meter (e.g. 1.81) :"))
    weight = float(input("Your Weight in Kilograms (e.g. 60) : "))
    BMI = weight/(height*height) # formula to calculate BMI.
    return BMI,height,weight

def interpret_BMI(BMI,height,weight):
    if BMI < 18.5:
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print("Category : Underweight")
    elif BMI > 18.5 and BMI < 24.9:
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print("Category: Normal Weight")
    elif BMI > 25 and BMI < 29.9:
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print("Category: Overweight")
    else:
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print("Category: Obese")

    
BMI,height,weight = calculate_BMI()
interpret_BMI(BMI,height,weight)
