start=input("Read the statement below then answer the following questions \n"
            "persons live in a street, having houses in line. Consider the following \n"
            "A lives in the corner’s house \n"
            "C is between E and G \n" 
            "There is 1 house between D and F \n"
            "F is neighbor of G \n"
            "There are two houses between A and G \n"
            "Enter Y to continue")
if start == 'y' or start == 'Y':

    Question1 = input("1. Who lives in the second corner?")

    while Question1 != 'D' and Question1 != 'd':
         Question1=input("Wrong! please try again")

    if Question1 == 'D' or Question1 == 'd':
        print("you are correct!")

    Question2 = input("2. Who lives in the middle?")
    while Question2 != 'G' and Question2 != 'g':
        Question2=input("Wrong! please try again")

    if Question2 == 'G' or Question2 == 'g':
            print("you are correct!")

    Question3 = input("3. Who lives between B and G?")
    while Question3 != 'F' and Question3 != 'f':
        Question3=input("Wrong! please try again")

    if Question3 == 'F' or Question3 == 'f':
            print("you are correct!")

    Question4 = input("4. Who is the neighbor of A?")
    while Question4 != 'E' and Question4 != 'e':
        Question4=input("Wrong! please try again")
    if Question4 == 'E' or Question4 == 'e':
            print("you are correct!")

    Question5 = input("5. How many houses are there between B and E?")
    while Question5 != '3':
        Question5=input("Wrong! please try again")
    if Question5 == '3':
            print("you are correct!")
    finish=input("Thank you for participating press 'Enter' to exit")
else:
    print("Good bye!")
    exit()