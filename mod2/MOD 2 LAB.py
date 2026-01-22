# Name : Devon 
# mod 2 lab 

DEANS_LIST: float = 3.5
DEANS_LIST_MSG: str = "Congratulations! You made the Dean's List!"

HONOR_ROLL: float = 3.25
HONOR_ROLL_MSG: str = "Great job! You made the Honor Roll!"

SENTINEL:str = 'ZZZ'

INPUT_PROMPT1: str = "Enter student's first name: "
INPUT_PROMPT2: str = "Enter student's GPA: "

first_name : str
gpa: float = 0.0

while True:
    first_name = input(INPUT_PROMPT1)
    if first_name.upper() != SENTINEL:
        gpa = float(input(INPUT_PROMPT2))
        if gpa >= DEANS_LIST: 
            print(DEANS_LIST_MSG)

        elif gpa >= HONOR_ROLL:
            print(HONOR_ROLL_MSG)
    else:
        break