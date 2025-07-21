
from student_utils import load_data, save_data, Student, get_name, get_score

def addStudent():
    name = get_name("Student")
    if not name or name.lower() == 'done':
        print("Error adding student")
        return
    
    print(f"\nWelcome {name}")
    subject_scores = {}
    while True:    
        subject = get_name("Subject")
        if len(subject_scores) == 0 and subject == "done":
            print("Error adding student")
            return
        if subject == "done":
            break
        if subject is None:
            continue
        score = get_score(subject)
        if not score:
            continue
        subject_scores[subject] = score
    stud = Student(name, subject_scores)
    return stud.to_dict()

def view_report_cards(entry):
    print()
    print(f"Student Name: {entry["name"]}")
    print(f"Student Average: {entry["average"]}")
    print("-"*35)
    print(f"{"Subject":^15} {"Score":^10} {"Grade":^6}")
    print("-"*35)
    for subject, data in entry["subjects"].items():
        print(f"{subject:<15} {data["score"]:^9} {data["grade"]:^6}")
    print("-"*35)

def update_report_card(entry):

    print("What do you want to update?")
    print("1. Student Name")
    print("2. Subjects and Scores")
    print("3. Cancel Update")

    try:
        choice = input('\nEnter your choice: ').strip()
    except:
        print("Invalid Option: Choose from 1-3")

    match choice:
        case "1":
            student_name = get_name("Student")
            if student_name:
                entry["name"] = student_name
                print("Student name updated")
                return entry
        case "2":
            subject_scores = {}
            while True:    
                subject = get_name("Subject")
                if len(subject_scores) == 0 and subject == "done":
                    print("Error updating report card")
                    return
                if subject == "done":
                    break
                if subject is None:
                    continue
                score = get_score(subject)
                if not score:
                    continue
                subject_scores[subject] = score
            stud = Student(entry["name"], subject_scores)
            print("subject and score updated")
            return stud.to_dict()
        case "3":
            print("Update cancelled")
            return None
        case _:
            print("Invalid Option: Choose from 1-3")
            return None

def main():
    print("\nStudent Report Card App")

    students_report_card_list = load_data()
    while True:
        print("\n--- Student Report Card Menu ---")
        print("1. Add Student Report Card")
        print("2. View All Student Report Cards")
        print("3. View Student Report Card")
        print("4. Update Student Report Card")
        print("5. Save & Exit")

        try:
            choice = input('\nEnter your choice: ').strip()
        except:
            print("Invalid Option: Choose from 1-5")
            continue

        match choice:
            case "1":
                student_data = addStudent()
                if student_data:
                    print("Student Report Card Added successfully")
                    students_report_card_list.append(student_data)

            case "2":
                if students_report_card_list:
                    for entry in students_report_card_list:
                        view_report_cards(entry)
                else:
                    print("No student report card record")

            case "3":
                if students_report_card_list:
                    student_name = get_name("Student")
                    found = False
                    for entry in students_report_card_list:
                        if entry["name"].lower() == student_name.lower():
                            found = True
                            view_report_cards(entry)
                            break
                    if not found:
                        print(f"Student not found ")
                else:
                    print("No student report card record")

            case "4":
                if students_report_card_list:
                    student_name = get_name("Student")
                    found = False
                    for idx, entry in enumerate(students_report_card_list, 0):
                        if entry["name"].lower() == student_name.lower():
                            found = True
                            updated_student = update_report_card(entry)
                            if updated_student is not None:
                                students_report_card_list[idx] = updated_student
                            break
                    if not found:
                        print(f"No with name '{student_name}' not found ")
                else:
                    print("No student report card record")

            case "5":
                save_data(students_report_card_list)
                print("Thank you for using Student Report Card App\nGoodbye!...\n")
                break

            case _:
                print("Invalid Option: Choose from 1-5")
                continue

if __name__ == "__main__":
    main()