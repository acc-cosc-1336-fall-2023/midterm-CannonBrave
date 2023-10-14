import question_c

while True:

    print('1. Determine assessement value and tax')
    print('2. Exit')
    choice = int(input('Enter a choice: '))

    if choice == 1:
        while True:
            property_value = float(input("Enter property value: "))
            assessment_value = question_c.get_assessment_value(property_value)
            print(f'The assessement value is: ${assessment_value:.2f}')

            tax_assessed = question_c.get_tax_assessed(assessment_value)
            print(f'Property tax: ${tax_assessed:.2f}')
            break

    elif choice == 2:
        exit_choice = input('Do you want to continue (y/n)? ')
        if exit_choice == "n":
            break



