from tkinter import *
from tkinter import messagebox
import datetime

window = Tk()
window.title("Mood Tracker")
window.geometry("350x400")

#list to store mood
mood = []

def save_mood():
    m = mood_select.get()

    if m == "Select your mood.":
        messagebox.showwarning("Warning","Please select a mood")
        return
    
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    mood_entry = f"{date}-{m}"
    mood.append(mood_entry)

    #update mood history display
    mood_listbox.insert(END,mood_entry)
    messagebox.showinfo("Saved!","Your mood has been saved.")
    

feel = Label(window,text="How are you feeling today?",font=("Arial",16)).pack(pady=10)
mood_select = StringVar(value="Select your mood")

md = ["Happy 😊", "Sad 😢", "Excited 🤩", "Angry 😠", "Relaxed 😌", "Stressed 😩", "Neutral 😐"]
m_menu = OptionMenu(window,mood_select,*md)
m_menu.pack(pady=5)

save_btn = Button(window,text="Save",fg="Red",font=("Times New Roman",20),command=save_mood)
save_btn.pack(pady=10)

mood_listbox = Listbox(window,width=40,height=10)
mood_listbox.pack(pady=5)

window.mainloop()