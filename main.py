from math import sqrt
from tkinter import *

# global variable initialisation
math_operation = ""
answer = 0

# function to display coresponding value of button clicked
def button_click(value):
    global math_operation
    math_operation = math_operation + value
    text_element.set(math_operation)

# function to clear the text entry boxes
def clear():
    text_element.set("")
    out_.set("")
    global math_operation, answer
    math_operation = ""
    answer = ""


 # functon to calculate the results and display in answer_field
def equal():
    try:
        global math_operation
        global answer
        answer = eval(math_operation)
        out_.set(str(answer))
        math_operation = ""

    except ArithmeticError:
        out_.set("Error!")
        math_operation = ""


# function to find the square root
def square_rt():
    global math_operation
    answer_ = sqrt(int(math_operation))
    out_.set(str(answer_))


# function to find the percentage
def percentage():
    global answer
    global math_operation
    if answer != 0:
        per = (answer / 100)
        text_element.set(str(per))
    else:
        first_var = int(math_operation)
        per = (first_var / 100)
        text_element.set(str(per))


 # function to remove the last inserted value
def back_space():
    global math_operation
    out_.set("")
    length = len(math_operation)
    math_operation = math_operation[0:(length - 1)]
    text_element.set(math_operation)




# creating window
window = Tk()
window.geometry("585x336")
window.title("Calculator")
window.configure(bg="#2b2e33")

# instances of StringVar
text_element = StringVar()
out_ = StringVar()

# creating text entry boxes
display_field = Entry(window, textvariable=text_element, width=30, bd=0,
                      bg="#2b2e33", fg="light grey", justify="right", font=("poppins", 14))
answer_field = Entry(window, textvariable=out_, width=30, bd=0,
                     bg="#2b2e33", fg="light grey", justify="right", font=("poppins", 24))

# Text field layout
display_field.grid(row=0, column=0, columnspan=5, pady=5, sticky="nsew")
answer_field.grid(row=1, column=0, columnspan=5, pady=5, sticky="nsew")


# creating buttons
button1 = Button(text=" 1 ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                 activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("1"))

button2 = Button(text=" 2 ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                 activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("2"))

button3 = Button(text=" 3 ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                 activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("3"))

button4 = Button(text=" 4 ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                 activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("4"))

button5 = Button(text=" 5 ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                 activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("5"))

button6 = Button(text=" 6 ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                 activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("6"))

button7 = Button(text=" 7 ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                 activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("7"))

button8 = Button(text=" 8 ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                 activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("8"))
button9 = Button(text=" 9 ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                 activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("9"))
button0 = Button(text=" 0 ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                 activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("0"))

button_dot = Button(text=" .", width="10", height="2", bd=0, font=("poppins", 12, "bold"), bg="light grey",
                    activebackground="#686c7a", activeforeground="#9b9fab", command=lambda: button_click("."))

# creating operator buttons
btn_plus = Button(text=" + ", width="10", height="2", bd=0, font=("poppins", 14, "bold"), bg="#0b74a9", padx=2, pady=5,
                  activebackground="#105e85", activeforeground="#F9F9F9", command=lambda: button_click("+"))

btn_Sub = Button(text=" - ", width="10", height="2", bd=0, font=("poppins", 14, "bold"), bg="#0b74a9", padx=2,
                 activebackground="#105e85", activeforeground="#F9F9F9", command=lambda: button_click("-"))

btn_mul = Button(text="x", width="10", height="2", bd=0, font=("poppins", 14, "bold"), bg="#0b74a9", padx=2,
                 activebackground="#105e85", activeforeground="#F9F9F9", command=lambda: button_click("*"))

btn_div = Button(text=" / ", width="10", height="2", bd=0, font=("poppins", 14, "bold"), bg="#0b74a9", padx=3,
                 activebackground="#105e85", activeforeground="#F9F9F9", command=lambda: button_click("/"))

btn_percentage = Button(text=" % ", width="10", height="2", bd=0, font=("poppins", 14, "bold"), bg="#0b74a9", padx=3,
                        pady=5, activebackground="#105e85", activeforeground="#F9F9F9", command=percentage)

btn_square_root = Button(text=" sqrt ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), padx=3, pady=5,
                         bg="#0b74a9", activebackground="#105e85", activeforeground="#F9F9F9", command=square_rt)

btn_back_space = Button(text="DEL", width="10", height="2", fg="#F9F9F9", bd=0, font=("poppins", 12, "bold"), padx=2,
                        pady=5, bg="#32558C", activebackground="#1e3a56", activeforeground="#5f9de3",
                        command=back_space)

button_clr = Button(text=" CLR ", width="10", height="2", fg="#F9F9F9", bd=0, padx=3, font=("poppins", 12, "bold"),
                    pady=5, bg="#32558C", activebackground="#1e3a56", activeforeground="#5f9de3", command=clear)

btn_equ = Button(text=" = ", width="10", height="2", bd=0, font=("poppins", 12, "bold"), padx=5, pady=5, bg="#878c96",
                 activebackground="#202430", activeforeground="#9b9fab", command=equal)


# label
label_ = Label(window, text="Developed By SAFAD TM", bg="#1d1e22", fg="#d4d4dc", padx=1, font=("poppins", 10))

# Button layout
button7.grid(row=3, column=0, sticky="nsew")
button8.grid(row=3, column=1, sticky="nsew")
button9.grid(row=3, column=2, sticky="nsew")
btn_back_space.grid(row=3, column=3, sticky="nsew")
button_clr.grid(row=3, column=4, sticky="nsew")

button4.grid(row=4, column=0, sticky="nsew")
button5.grid(row=4, column=1, sticky="nsew")
button6.grid(row=4, column=2, sticky="nsew")
btn_mul.grid(row=4, column=3, sticky="nsew")
btn_div.grid(row=4, column=4, sticky="nsew")

button1.grid(row=5, column=0, sticky="nsew")
button2.grid(row=5, column=1, sticky="nsew")
button3.grid(row=5, column=2, sticky="nsew")
btn_Sub.grid(row=5, column=3, sticky="nsew")
btn_square_root.grid(row=5, column=4, sticky="nsew")

button0.grid(row=6, column=0, sticky="nsew")
button_dot.grid(row=6, column=1, sticky="nsew")
btn_equ.grid(row=6, column=2, sticky="nsew")
btn_plus.grid(row=6, column=3, sticky="nsew")
btn_percentage.grid(row=6, column=4, sticky="nsew")

# label layout
label_.grid(row=7, column=0, columnspan=5, sticky="nsew")

window.mainloop()