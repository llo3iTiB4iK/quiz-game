from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizGUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)

        false_image = PhotoImage(file="images/false.png")
        false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)

        self.choices = {"boolean": [true_button, false_button], "multiple": []}

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.change_buttons_state("active")
            self.canvas.itemconfig(self.question_text, text=question)

        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!\nYour final score is "
                                                            f"{self.quiz.score} out of {len(self.quiz.questions_list)}")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.change_buttons_state("disabled")
        self.window.after(1000, self.get_next_question)

    def change_buttons_state(self, new_state):
        current_question_type = self.quiz.current_question.type
        for button in self.choices[current_question_type]:
            button.config(state=new_state)
        if new_state == "active":
            if current_question_type == "boolean":
                for button in self.choices["multiple"]:
                    button.grid_forget()
                self.choices["multiple"].clear()
                self.choices["boolean"][0].grid(row=2, column=0)
                self.choices["boolean"][1].grid(row=2, column=1)
            else:
                row_to_place = 2
                for choice in self.quiz.current_question.get_multiple_answers():
                    new_button = Button(
                        text=choice,
                        width=30,
                        font=("Arial", 10, "normal"),
                        command=lambda c=choice: self.give_feedback(self.quiz.check_answer(c))
                    )
                    new_button.grid(row=row_to_place, column=0, columnspan=2, pady=5)
                    row_to_place += 1
                    self.choices["multiple"].append(new_button)
                self.choices["boolean"][0].grid_forget()
                self.choices["boolean"][1].grid_forget()
