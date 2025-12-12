
error = f'Invalid input!'  #error message

course_message = {
    "0": "First Course? ",
    "1": "Second Course? ",
    "2": "Third Course? ",
    "3": "Fourth Course? ",
    "4": "Fifth Course? ",
    "5": "Sixth Course? ",
    "6": "Seventh Course? ",
    "7": "Eighth Course? ",
    "8": "Ninth Course? ",
    "9": "Tenth Course? "
}

grades = {

}
courses = []
course_scores = []
score_message = f"What was your score? "
goodbye = "GoodBye"

def check_number_of_courses():  #1. get number of courses
    while True:
        number_of_courses = input(f"How many courses do you offer? ").strip()
        if number_of_courses.isdigit():
            break
        else:
            print(error)
    return number_of_courses


def score():
    while True:
        course_score = input(score_message).strip()
        if course_score.isdigit():
            course_scores.append(course_score)
            break
        else:
            print(error)
    return course_score


def check_grade():   #3. pair grade with course and scores
    grade = ' '
    while True:
        course_score = int(score())
        if 0 <= course_score <= 100:  # Check if c_a_s is within the range 0 to 100
            if 70 <= course_score <= 100:  # Grade A
                grade = 'A'
            elif 60 <= course_score <= 69:  # Grade B
                grade = 'B'
            elif 50 <= course_score <= 59:  # Grade C
                grade = 'C'
            elif 40 <= course_score <= 49:  # Grade D
                grade = 'D'
            elif 0 <= course_score <= 39:  # Grade F
                grade = 'F'
            break
        else:
            print('Please Enter a Valid Input')  # Input outside 0–100
    return grade


def course_collection():    #2. get course name and pair with scores
    number_of_courses: int = int(check_number_of_courses())
    for i in range(int(number_of_courses)):
        course_name = input(course_message.get(str(i), "!")).strip()
        courses.append(course_name)
        grades.setdefault(course_name, check_grade())
    for name,grade in grades.items():
        print(f"{name}    {grade}")
    print(f"Thank You ")


course_collection()
