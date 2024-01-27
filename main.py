from question_model import Question
from quiz_brain import QuizBrain
from art import logo
from urllib.request import urlretrieve

NUM = 5  # number of questions, can be 1-50
DIFFICULTY = 'easy'  # quiz difficulty, can be easy/medium/hard, None stands for questions of any difficulty

url = f'https://opentdb.com/api.php?amount={NUM}&type=boolean'
if DIFFICULTY:
    url += f'&difficulty={DIFFICULTY}'
print(url)

urlretrieve(url, 'data.py')

with open('data.py', 'r') as file:
    data = file.read()

square_bracket_index = data.index('[')
data_clean = 'question_data = ' + data[square_bracket_index:-1:]

with open('data.py', 'w') as file:
    file.write(data_clean)


from data import question_data

questions = [Question(q['question'], q['correct_answer']) for q in question_data]
quiz = QuizBrain(questions)

print(logo)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(questions)}")
