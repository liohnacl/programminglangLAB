# height cm
# weight kg
def bmi_Formula(**kwargs):
    weight = kwargs['weight']
    height = kwargs['height']
    
    return weight/(height**2)

h = float(input("Enter height in cm:  "))
w = float(input("Enter weight in kg: "))

res = bmi_Formula(weight=w,height=h)

if res < 18.5:
    print("Underweight")
elif res == 18.5 or res <=24.9:
    print("Normal Weight")
elif res == 25.0 or res <=29.9:
    print("Overweight")
elif res == 30.0 or res <=34.9:
    print("Obesity Class I")
elif res == 35.0 or res  <= 39.9:
    print("Obesity Class II")
elif res >= 40:
    print("Obesity Class III")
else:
    print("Invalid Input")


