from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        # Score label
        self.score = Label(text=f"Score: 0", background=THEME_COLOR, fg="white", font=("Ariel", 10, "bold"))
        self.score.grid(column=1, row=0)

        # Question canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,125,
            text="Questions",
            font=("Ariel", 20, "italic"),
            width=280
        )

        # True button
        right = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=right, bg=THEME_COLOR, highlightthickness=0, command=self.guess_true)
        self.true_button.grid(column=0, row=2)

        # False button
        wrong = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=wrong, bg=THEME_COLOR, highlightthickness=0, command=self.guess_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def guess_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def guess_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
