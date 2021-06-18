from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score: 0", font=("Ariel", 20, ), fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=200, highlightthickness=0)
        self.question = self.canvas.create_text(150, 100, text="hello", width=250, fill=THEME_COLOR, font=("Ariel", 20, ))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.true_btn = Button(text="✅", font=("Ariel", 20,), bg=THEME_COLOR, highlightthickness=0, command=self.true_func)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(text="❌", font=("Ariel", 20,), bg=THEME_COLOR, highlightthickness=0, command=self.false_func)
        self.false_btn.grid(row=2, column=1)
        self.display_question()
        self.window.mainloop()

    def display_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=next_question)
        else:
            self.canvas.itemconfig(self.question, text="Game Over")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def give_feedback(self):
        result = self.quiz.check_answer("True")
        self.score.config(text=f"{self.quiz.score}/{self.quiz.question_number}")
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.display_question)

    def true_func(self):
        self.give_feedback()


    def false_func(self):
        self.give_feedback()


