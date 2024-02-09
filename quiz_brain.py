class QuizBrain:
    def __init__(self, q_list):
        self.current_question = None
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        self.current_question = self.questions_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
