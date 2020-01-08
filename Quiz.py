import random


def get_question_answer_list(file_name):
    file = open(file_name, "r") # open and read the file
    question_answer_list = [] # create lists to contain the questions
    # iterate over each line
    for line in file:
        question_answer_list.append(line[0:-1]) # add the questions to list, without adding '\n'
    question_answer_list = random.sample(question_answer_list, 10) # randomly choose 10 questions from the list
    return question_answer_list


def get_question_list(question_answer_list):
    questions = []
    for element in question_answer_list:
        questions.append(element.split(",")[0])
    return questions


def get_answer_list(question_answer_list):
    answers = []
    for element in question_answer_list:
        answers.append(element.split(",")[1])
    return answers


file_name = str(input("What is the name of the question file?"))
QA_list = get_question_answer_list(file_name)
questions = get_question_list(QA_list)
answers = get_answer_list(QA_list)
correct = 0
for i in range(10):
    answer = str(input(questions[i]))
    if answer == answers[i]:
        print("Correct!")
        correct += 1
    else:
        print("Incorrect! The answer is", answers[i])
print("You got", correct, "out of 10, which is", 100*correct/10, "%.")
