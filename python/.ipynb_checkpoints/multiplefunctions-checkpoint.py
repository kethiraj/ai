class ethiraj():
    def oddeven():
        inputs=int(input())
        if((inputs % 2)==0):
            print("even")
            message="even"
        else:
            print("odd")
            message="odd"    
        return message    
        
    def BMI():
        bmi=float(input("Enter the BMI Index:"))
        if(bmi<18.5):
            print("Underweight")
            message="Underweight"
        elif(bmi>=18.5 and bmi<=24.9):
            print("Healthy weight")
            message="Healthyweight"
        elif(bmi>=25 and bmi<=29.9):
            print("Overweight")
            message="Overweight"
        else:
            print("Very Overweight") 
            message="veryoverweight"
        return message