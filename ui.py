THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain): #we tell that quiz_brain is of data type QuizBrain
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz")
        # self.window.geometry("500x500")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label=Label(text="Score:00",fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=2, row=0)
        self.canvas=Canvas(width=300, height=350,highlightthickness=0)
        self.text_qs=self.canvas.create_text(150,
                                             170,
                                             width=280,
                                             text="Hello", 
                                             font=("Aerial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=3, pady=50)
        
        
        self.cross_image=PhotoImage(file="/home/ab/Documents/100-python/100 days python/Questions_pract/images/false.png")
        self.tick_image=PhotoImage(file="/home/ab/Documents/100-python/100 days python/Questions_pract/images/true.png")
        self.tick_button=Button(image=self.tick_image, highlightthickness=0, command=self.check_tick)
        self.cross_button=Button(image=self.cross_image, highlightthickness=0, command=self.check_cross)
        self.tick_button.grid(column=0, row=2)
        self.cross_button.grid(column=2, row=2)
        self.get_next_questiion()
        self.window.mainloop()

    def get_next_questiion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.text_qs, text=q_text)
        else:
            self.canvas.itemconfig(self.text_qs, text="You reached at Maximum number of question")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")
    def check_tick(self):
        self.user_answer="True"
        # self.is_right=self.quiz.check_answer(self.user_answer)
        self.get_feedback(self.quiz.check_answer(self.user_answer))
        # self.quiz.next_question()
        # self.get_next_questiion()

    def check_cross(self):
        self.user_answer="False"
        # self.is_right=self.quiz.check_answer(self.user_answer)
        self.get_feedback(self.quiz.check_answer(self.user_answer))
        # self.quiz.next_question()
        # self.get_next_questiion()

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_questiion)