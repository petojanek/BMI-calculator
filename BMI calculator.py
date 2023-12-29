height_in_meters = float(input("Enter your height in meters: "))
weight_in_kilograms = int(input("Enter your weight in kilograms: "))

bmi = weight_in_kilograms / height_in_meters ** 2

rounded_bmi = round(bmi, 2)

if rounded_bmi < 18.5:
    print(f"Your BMI is {rounded_bmi}, you are underweight.")
elif rounded_bmi < 25:
    print(f"Your BMI is {rounded_bmi}, you have a normal weight.")
elif rounded_bmi < 30:
    print(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
elif rounded_bmi < 35:
    print(f"Your BMI is {rounded_bmi}, you are obese.")
else:
    print(f"Your BMI is {rounded_bmi}, you are clinically obese.")
  