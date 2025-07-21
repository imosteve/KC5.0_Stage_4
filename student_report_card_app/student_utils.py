
import os
import json

FILENAME = 'student_report_card_app/students.json'

def load_data():
    try:
        if not os.path.exists(FILENAME) or not os.path.getsize(FILENAME) > 0:
            return []
        with open(FILENAME, 'r') as file:
            students = json.load(file)
        return students
    except Exception as e:
        print(f'Error loading file: {e}')
        return 
    
def save_data(students_data):
    try:
        with open(FILENAME, 'w') as file:
            json.dump(students_data, file, indent=4)
    except Exception as e:
        print(f'Error saving file: {e}')
        return
    
class Student:
    def __init__(self, name, subject_scores):
        self.name = name
        self.subject_scores = subject_scores
    
    def get_subjects(self):
        subjects = list(self.subject_scores.keys())
        return subjects

    def get_scores(self):
        scores =  list(self.subject_scores.values())
        if not scores:
            scores = 0
        return scores

    def calculate_grades(self):
        grades = []
        for score in self.get_scores():
            if score >= 70:
                grade = "A"
            elif score >= 60:
                grade = "B"
            elif score >= 50:
                grade = "C"
            elif score >= 45:
                grade = "D"
            elif score >= 40:
                grade = "E"
            else:
                grade = "F"
            grades.append(grade)
        return grades
    
    def calculate_average(self):
        average =  round((sum(self.get_scores()) / len(self.get_scores())), 2)
        return average

    def to_dict(self):
        subjects_to_dict = {}
        for idx in range(len(self.get_subjects())):
            to_dict = {"score": self.get_scores()[idx], "grade": self.calculate_grades()[idx]}
            subjects_to_dict[self.get_subjects()[idx]] = to_dict

        return {
            "name": self.name,
            "subjects": subjects_to_dict,
            "average": self.calculate_average()
        }

def get_name(prompt):
    if prompt.lower() == "student":
        name = input(f"Enter {prompt}'s name: ").title()
    else:
        name = input(f"Enter {prompt} name (or 'done' to finish): ").title()
    if not name.replace(" ", "").isalpha():
        print('Error: Name cannot be blank or contain numbers')
        return None
    if name.lower() == 'done':
        return name.lower()
    return ' '.join(name.split())

def get_score(subject):
    try:
        score = float(input(f"Enter {subject}'s Score: "))
        if not (0 <= score <= 100):
            print("Invalid Input: Number must be between 0 and 100")
            return False
        else:
            return score
    except:
        print("Invalid Input: Must be a number")
        return False

