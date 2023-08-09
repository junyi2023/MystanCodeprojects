"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    maximum001=None
    minimum001=None
    sum001=0
    average001=0
    count001=0
    maximum101=None
    minimum101=None
    sum101=0
    average101=0
    count101=0
    class_name=None
    while True:
        class_name = str(input("Which class? "))
        if class_name == "-1":
            break
        score =int(input("Score? "))
        if class_name.upper() == str("SC001"):
            if maximum001== None or minimum001== None:
                maximum001 = minimum001 = score
            if score > maximum001:
                maximum001 = score
            elif score < minimum001:
                minimum001 = score
            count001 +=1
            sum001 = score+sum001
            average001 =float(sum001/count001)
        elif class_name.upper() == str("SC101"):
            if maximum101 == None or minimum101== None:
                maximum101 = minimum101 = score
            if score > maximum101:
                maximum101 = score
            elif score < minimum101:
                minimum101 = score
            count101 +=1
            sum101 = score+sum101
            average101 =float(sum101/count101)
    if count001 or count101 !=0:        
        print("==========SC001==========")
        if maximum001 == None:
            print("No Score for SC001")
        else:
            print("Max (001):",maximum001)
            print("Min (001):",minimum001)
            print("Avg (001):",average001)
        print("==========SC101==========")
        if maximum101 == None:
            print("No Score for SC101")
        else:
            print("Max (101):",maximum101)
            print("Min (101):",minimum101)
            print("Avg (101):",average101)
    else:
        print("No class scores were entered")
# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()



