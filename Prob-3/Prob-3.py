# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Caleb Howard

def letterGrade(score):

    if score == 0:
        letterGrade = "F"
    elif score == 1:
        letterGrade = "F"
    elif score == 2:
        letterGrade = "D"
    elif score == 3:
        letterGrade = "C"
    elif score == 4:
        letterGrade = "B"
    elif score == 5:
        letterGrade = "A"

    return letterGrade

def unitTest():
    print("0 returns a grade of:", letterGrade(0))
    print("1 returns a grade of:", letterGrade(1))
    print("2 returns a grade of:", letterGrade(2))
    print("3 returns a grade of:", letterGrade(3))
    print("4 returns a grade of:", letterGrade(4))
    print("5 returns a grade of:", letterGrade(5))
    

if __name__ == "__main__":
    unitTest()