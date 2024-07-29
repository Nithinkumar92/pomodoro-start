
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
from tkinter import *
timer=None
window=Tk()
window.title("pomodoro app")
count=1
rep=0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(time_text,text="00:00")
    timel.config(text="Timer")
    check.config(text="")
    global rep
    rep=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global rep
    rep+=1

    if rep%8==0:
        count_down(LONG_BREAK_MIN*60)
        timel.config(text="Break",fg=RED,bg=PINK,font=(FONT_NAME,40,"bold"))
    elif rep%2==0:
        timel.config(text="Break", fg=YELLOW, bg=PINK, font=(FONT_NAME, 40, "bold"))
        count_down(SHORT_BREAK_MIN*60)
    else:
        timel.config(text="Work", fg=YELLOW, bg=PINK, font=(FONT_NAME, 40, "bold"))
        count_down(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=count//60
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"


    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start()
        mar=""
        for i in range(rep//2):
            mar+="✔"
        check.config(text=mar)




# ---------------------------- UI SETUP ------------------------------- #




timel=Label(text="Timer",fg=GREEN,bg=PINK,font=(FONT_NAME,40,"bold"))
timel.grid(column=2,row=1)
but1=Button(text="start",bg=PINK,highlightthickness=0,command=start)
but1.grid(column=1,row=3)
but2=Button(text="restart",bg=PINK,highlightthickness=0,command=reset)
but2.grid(column=3,row=3)
window.config(padx=50,pady=50,bg=PINK)
canvas=Canvas(width=250,height=250,bg=PINK,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(125,125,image=tomato)
time_text=canvas.create_text(120,140,text="00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

check=Label(text="",bg=PINK,fg=GREEN)
check.grid(row=3,column=2)

window.mainloop()
