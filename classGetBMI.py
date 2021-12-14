class BMI:
    def bmi_Formula(**kwargs):
         weight = kwargs['weight']
         height = kwargs['height']
    
         return weight/(height**2)
    
    def bmi_Result(res):
        if res < 18.5:
            return "Underweight"
        elif res == 18.5 or res <=24.9:
            return "Normal Weight"
        elif res == 25.0 or res <=29.9:
            return "Overweight"
        elif res == 30.0 or res <=34.9:
            return "Obesity Class I"
        elif res == 35.0 or res  <= 39.9:
            return "Obesity Class II"
        elif res >= 40:
            return "Obesity Class III"
        else:
            return "Invalid Input"
    

if __name__ == "__main__":
    h = float(input("Enter height in cm:  "))
    w = float(input("Enter weight in kg: "))

    b = BMI
    res = b.bmi_Formula(weight=w,height=h)
    
    action = b.bmi_Result(res)
    print(action)
    



    




