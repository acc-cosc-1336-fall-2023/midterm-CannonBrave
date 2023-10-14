import question_d

while True:
    age = float(input("Enter a person's age: "))
    result = question_d.get_person_category(age)
    print(F"The person is a {result}.")

    loop = input("Enter another age (Y/N): ")
    if loop != "Y":
        break


    


    
