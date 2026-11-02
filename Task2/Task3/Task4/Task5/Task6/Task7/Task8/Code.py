
students = int(input("Enter number of students: "))
questions = int(input("Enter number of questions: "))

key = []

print("\nEnter correct answers:")
for i in range(questions):
    ans = input("Question " + str(i + 1) + ": ")
    key.append(ans)

answers = []

for i in range(students):

    print("\nStudent", i + 1)

    student_answers = []

    for j in range(questions):
        ans = input("Answer for Q" + str(j + 1) + ": ")
        student_answers.append(ans)

    answers.append(student_answers)

print("\n--- Question Performance Report ---")

missed = []

for j in range(questions):

    correct = 0

    for i in range(students):

        if answers[i][j] == key[j]:
            correct = correct + 1

    success = (correct / students) * 100
    wrong = students - correct

    print("\nQuestion:", j + 1)
    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Success Rate:", success, "%")

    if success > 70:
        print("Difficulty: Easy")

    elif success >= 40:
        print("Difficulty: Medium")

    else:
        print("Difficulty: Difficult")

    missed.append(wrong)

maximum = max(missed)

print("\nMost Frequently Missed Questions:")

for j in range(questions):
    if missed[j] == maximum:
        print("Question", j + 1, "-", maximum, "wrong answers")

print("\nAnalysis Completed")

