from random import shuffle
import html


class Question:
    def __init__(self, text, correct_answer, wrong_answers, q_type):
        self.text = html.unescape(text)
        self.correct_answer = html.unescape(correct_answer)
        self.wrong_answers = html.unescape(wrong_answers)
        self.type = q_type

    def get_answers(self):
        if self.type == 'boolean':
            return "True / False"
        else:
            possible_answers = self.wrong_answers + [self.correct_answer]
            shuffle(possible_answers)
            return ' / '.join(possible_answers)
