from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizGUI
from data import question_data

questions = [Question(q['question'], q['correct_answer'], q['incorrect_answers'], q['type']) for q in question_data]
quiz = QuizBrain(questions)
quiz_ui = QuizGUI(quiz)
