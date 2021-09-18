from tkinter import *
#Importing tkinter

root = Tk()
root.title("Wiktarina")
root.geometry("300x300")

 #Doing the first quiz
def que_one():
    question = Label(root, text="Wisit gruza i ee nelza skuzat?")
    answer = Entry()
    btn = Button(root, text="Otwetit!", command=lambda: game1(que_two()))
    question.grid(row=0)
    answer.grid(row=1)
    btn.grid(row=2)

    def game1(que_two):
        if answer.get().lower() == "lampo4ka":
            que_two()
        else:
            messagebox.showerror("Ozibka, poprobui izy raz")
            
#Doing the second quiz
def que_two():
    question_2 = Label(root, text="Zimoi i letom odnowo zweta?")
    answer_2 = Entry()
    btn_2 = Button(root, text="Otwet!")
    question_2.grid(row=0)
    answer_2.grid(row=1)
    btn_2.grid(row=2)

root.mainloop()
