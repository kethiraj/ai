class classassignments():
    def subfields():
        subcategoryofAI = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech processing", "Netural Language Processing"]
        print("sub-fields in AI are:")
        for i in subcategoryofAI:
            print(i)

    def oddEven():
        oddeven=int(input("Enter a number:"))
        if oddeven%2 == 0:
            print(oddeven, "is Even number")
        else:
            print(oddeven, "is odd number")

    def Elegible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
    
        if (gender == "Male" and age > 20) or (gender == "Female" and age > 17):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        mark = []
        for i in range(1,6):
            sub = int(input(f"Subjects{i}= "))
            mark.append(sub)
        
        total = sum(mark)
        print("Total :", total)

        percentage=total / len(mark)
        print("Percentage :", percentage)        

    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Areaformula=(Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ", Areaformula)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        perimeterbreadth=int(input("Breadth:"))
        perimeterformula=(Height1+Height2+Breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ", perimeterformula)      