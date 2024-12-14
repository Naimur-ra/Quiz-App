def read_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(';')
            question = parts[0]
            options = parts[1:5]
            correct_answer = parts[5]
            questions.append((question, options, correct_answer))
    return questions

def display_question(question, options):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= 4:
                return answer - 1
            else:
                print("Invalid option. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def evaluate_answers(questions, student_answers):
    score = 0
    for i, (question, options, correct_answer) in enumerate(questions):
        if options[student_answers[i]] == correct_answer:
            score += 2
    return score

def save_marks(student_id, score, file_path):
    updated = False
    lines = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        pass

    with open(file_path, 'w') as file:
        for line in lines:
            id, marks = line.strip().split(',')
            if id == student_id:
                if score > int(marks):
                    file.write(f"{student_id},{score}\n")
                else:
                    file.write(line)
                updated = True
            else:
                file.write(line)
        if not updated:
            file.write(f"{student_id},{score}\n")

def main():
    student_id = input("Enter your student ID: ")
    questions = read_questions('questions.txt')
    student_answers = []
    
    for question, options, correct_answer in questions:
        answer = display_question(question, options)
        student_answers.append(answer)
    
    score = evaluate_answers(questions, student_answers)
    print(f"Your total score is: {score}")
    
    save_marks(student_id, score, 'marks.txt')

if __name__ == "__main__":
    main()
