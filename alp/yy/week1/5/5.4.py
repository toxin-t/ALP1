test_mark = int(input("Enter your test mark: "))
if test_mark < 1 or test_mark > 100:
    print("Invalid test mark. Please enter a number between 1 and 100.")
else:
    Fail = ""
    if test_mark < 40:
        Fail = "Y"
    else:
        Fail = "N"
    if Fail != "N":
        print("Retake required.")
    else:
        print("Congratulations, you passed the test!")
