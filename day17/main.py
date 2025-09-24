from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    question_bank.append(Question(ques["text"], ques["answer"]))

# print(question_bank)
question = QuizBrain(question_bank)
while question.still_has_question():
    question.next_question()

print("You have completed the Quiz!!")
print(f"Your final score is: {question.score}/{question.question_number}")