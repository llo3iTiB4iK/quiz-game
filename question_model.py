from random import shuffle


class Question:
    def __init__(self, text, correct_answer, wrong_answers, q_type):
        self.text = text
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers
        self.type = q_type

    def get_answers(self):
        if self.type == 'boolean':
            return "True / False"
        else:
            possible_answers = self.wrong_answers + [self.correct_answer]
            shuffle(possible_answers)
            return ' / '.join(possible_answers)
