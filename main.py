from tkinter import Tk, Label, Button, Text
from pynput import keyboard

counter = 5
timer = ''


# ------------------------------- Key function --------------------------------- #

def on_release(key: keyboard.Key) -> None:

    if textbox['state'] != 'disabled':
        reset_countdown()


# ------------------------------- start timer --------------------------------- #

def start_timer() -> None:
    start_button.config(state='disabled')
    textbox.config(state='normal', bg='white')
    countdown(count=counter)


# ------------------------------- clock timer --------------------------------- #

def countdown(count) -> None:
    global timer
    if count > 0:
        if count == 5:
            textbox.config(highlightcolor='#44ce1b', highlightbackground='#44ce1b')
        elif count == 4:
            textbox.config(highlightcolor='#bbdb44', highlightbackground='#bbdb44')
        elif count == 3:
            textbox.config(highlightcolor='#f7e379', highlightbackground='#f7e379')
        elif count == 2:
            textbox.config(highlightcolor='#f2a134', highlightbackground='#f2a134')
        elif count == 1:
            textbox.config(highlightcolor='#e51f1f', highlightbackground='#e51f1f')

        timer = window.after(1000, countdown, count - 1)
    else:
        textbox.config(bg='#fff0f0')
        textbox.delete('1.0', 'end')
        start_button.config(state='normal')
        textbox.config(state='disabled')
        window.after_cancel(timer)


# ------------------------------- reset timer --------------------------------- #

def reset_countdown() -> None:
    window.after_cancel(timer)
    countdown(count=counter)


# ------------------------------- tkinter UI --------------------------------- #

window = Tk()
window.title('Dangerous Writing App')
window.config(background='#FFFFFF', width='200', height='600', padx=20, pady=20)

main_heading = Label(text='Dangerous Writing App', font=('Myriad Pro', 25, 'bold'), fg='crimson', bg='#FFFFFF')
main_heading.pack(pady=20)

info = Label(text='Type... something within 5 sec or your text will be deleted!', font=('Myriad Pro', 13, 'normal'),
             bg='#FFFFFF', fg='#525252')
info.pack(pady=10)

start_button = Button(text='Start', background='#ffffff', command=start_timer, fg='#525252', disabledforeground='#9d9d9d',
                      font=('Myriad Pro', 15, 'bold'), width='20', height='2', borderwidth=0, relief='solid')
start_button.pack()

textbox = Text(height=15, width=100, startline=5, font=('Myriad pro', 12), fg='#525252', bg='#FFFFFF', state='disabled',
               highlightthickness=3)
textbox.pack(pady=10, padx=20)

# key listener
listener = keyboard.Listener(on_release=on_release)
listener.start()

window.mainloop()
