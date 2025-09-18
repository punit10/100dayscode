class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return True if self.question_number < len(self.question_list) else False

    def next_question(self):
        current_question = self.question_list[self.question_number]

        print(f"Q {self.question_number}. {current_question.text}")
        user_answer = input()
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == str(correct_answer).lower():
            self.score += 1
            print("Correct")
        else:
            print("Wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")
