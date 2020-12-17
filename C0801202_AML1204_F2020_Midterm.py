def final_grade_calculator(studentNumber, assignmentGrade, midtermGrade, finaltermGrade, projectGrade):
    final_grade = assignmentGrade * 0.3 + midtermGrade * 0.2 + finaltermGrade * 0.2 + projectGrade * 0.3
    mark_assignment = mark_assigner(studentNumber, final_grade)
    print("Student Number:", student_Number, "has achieved the fina grade of", final_grade, "which is equivalent to",
          mark_assignment)


def mark_assigner(studentNumber, finalGrade):
    if 100 > finalGrade > 94:
        return "A+"
    elif 93 > finalGrade > 87:
        return "A"
    elif 86 > finalGrade > 80:
        return "A-"
    elif 79 > finalGrade > 77:
        return "B+"
    elif 76 > finalGrade > 73:
        return "B"
    else:
        return "B-"


student_Number = "C0801202"
assignment_Grade = 95
mid_term_grade = 93
final_term_grade = 96
project_grade = 95

final_grade_calculator(student_Number, assignment_Grade, mid_term_grade, final_term_grade, project_grade)

