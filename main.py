from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
LIGHTGREEN = "#E8FFCE"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    green_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        green_label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        green_label.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)
        green_label.config(text="WORK")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamodoro")
window.config(pady=50, padx=100, bg=LIGHTGREEN)



green_label = Label(text="TIMER", font=(FONT_NAME, 40), bg=LIGHTGREEN, fg=GREEN)
green_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=LIGHTGREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_btn = Button(text="Start", highlightthickness=0, highlightbackground=LIGHTGREEN, command=start_timer)
start_btn.grid(row=2, column=0)

check_marks = Label( bg=LIGHTGREEN, fg=GREEN)
check_marks.grid(row=3, column=1)

reset_btn = Button(text="Reset", highlightthickness=0, bg=LIGHTGREEN, highlightbackground=LIGHTGREEN,
                   command=reset_timer)
reset_btn.grid(row=2, column=2)





window.mainloop()
