student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for k in student_scores:
    score = student_scores[k]
    print(score)
    match score:
        case int(score) if score>91:
            student_grades[k] = "Outstanding"
        case int(score) if score > 81 and 90 >= score:
            student_grades[k] = "Exceeds Expectations"
        case int(score) if score > 71 and 80 >= score:
            student_grades[k] = "Acceptable"
        case int(score) if 70 >= score:
            student_grades[k] = "Fail"
print(student_grades)