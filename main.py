import os
import sys
def resource_path(relative_path):
    """Get absolute path to resource, works for PyInstaller and normal Python."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from search import search_word
from add_word import open_add_window
from edit_word import open_edit_window
from delete_word import open_delete_window
from speak import speak
# -------------------- FUNCTIONS -------------------- #
last_meaning = ""
def search():
    global last_meaning

    word = entry.get()

    meaning = search_word(word, direction.get())

    # Save the last meaning for the Speak button
    last_meaning = meaning

    if meaning == "Word not found":
        meaning_label.config(text=meaning, fg="red")
        status_label.config(text=f"'{word}' was not found.")
    else:
        meaning_label.config(text=meaning, fg="green")
        status_label.config(text=f"Found: {word}")
def speak_word():
    speak(last_meaning)
def speak_word():

    if last_meaning == "" or last_meaning == "Word not found":
        messagebox.showwarning(
            "Warning",
            "Please search for a valid word first."
        )
        return

    speak(last_meaning)
def search_enter(event):
    search_button.config(bg="#1D4ED8")

def search_leave(event):
    search_button.config(bg="#2563EB")
def clear():
    entry.delete(0, END)
    meaning_label.config(
        text="Search for a word to see its meaning.",
        fg="black"
    )
    status_label.config(
        text="Ready | Total Words: 10"
    )
    entry.focus()

def exit_app():
    root.destroy()
def change_direction(*args):
    if direction.get() == "Manipuri → English":
        word_label.config(text="Enter a Manipuri Word")
    else:
        word_label.config(text="Enter an English Word")

    clear()

# -------------------- MAIN WINDOW -------------------- #

root = Tk()
# Load Background Image
bg_image = Image.open(resource_path("assets/background.png"))
bg_image = bg_image.resize((1200, 700))

background = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=background)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# Left Panel
left_panel = Frame(
    root,
    bg="white",
    width=430,
    height=620,
    bd=0
)
header = Frame(
    left_panel,
    bg="white"
)
search_frame = Frame(
    left_panel,
    bg="white"
)

search_frame.pack(pady=10)
header.pack(fill="x", pady=20)
left_panel.place(x=40, y=40)
root.title("English - Manipuri Dictionary")
root.geometry("1200x700")
root.resizable(False, False)
root.configure(bg="white")


# -------------------- TITLE -------------------- #

title = Label(
    left_panel,
    text="📖 English ↔ Manipuri\nDictionary",
    font=("Segoe UI", 24, "bold"),
    bg="white",
    fg="#1E3A5F",
    justify="center"
)
title.pack(in_=header)
subtitle = Label(
    left_panel,
    text="Your bridge between two languages",
    font=("Segoe UI", 11),
    bg="white",
    fg="gray"
)

subtitle.pack(in_=header)
subtitle = Label(
    root,
    text="Fast • Simple • Easy to Use",
    font=("Arial", 11),
    bg="white",
    fg="gray"
)
subtitle.pack(in_=header)

direction = StringVar()
direction.set("Manipuri → English")

direction_menu = OptionMenu(
    root,
    direction,
    "Manipuri → English",
    "English → Manipuri"
)

direction_menu.config(font=("Arial", 12))
direction_menu.pack(pady=10)
direction.trace_add("write", change_direction)
# -------------------- INPUT SECTION -------------------- #

word_label = Label(
    search_frame,
    text="Enter a Manipuri Word",
    font=("Arial", 14),
    bg="white"
)
word_label.pack(pady=10)

entry = Entry(
    search_frame,
    font=("Segoe UI", 14),
    width=28,
    justify="center",
    bd=2,
    relief="solid"
)
entry.pack(pady=10)

entry.focus()
entry.bind("<Return>", lambda event: search())


# -------------------- SEARCH BUTTON -------------------- #

search_button = Button(
    search_frame,
    text="🔍 Search",
    font=("Segoe UI", 12, "bold"),
    bg="#2563EB",
    fg="white",
    padx=20,
    pady=5,
    command=search
)
search_button.pack(pady=15)
search_button.bind("<Enter>", search_enter)
search_button.bind("<Leave>", search_leave)

# -------------------- RESULT SECTION -------------------- #

meaning_title = Label(
    left_panel,
    text="Meaning",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#2C3E50"
)
meaning_title.pack(pady=(20, 5))

meaning_label = Label(
    left_panel,
    text="Search for a word to see its meaning.",
    font=("Segoe UI", 13),
    bg="#F4F6F7",
    fg="black",
    width=35,
    height=5,
    relief="solid",
    wraplength=450,
    justify="center"
)
meaning_label.pack()


# -------------------- BUTTONS -------------------- #

button_frame = Frame(left_panel, bg="white")
button_frame.pack(pady=20)
add_button = Button(
    button_frame,
    text="Add Word",
    font=("Segoe UI", 11, "bold"),
    bg="#22C55E",
    fg="white",
    width=10,
    command=open_add_window
)
add_button.pack(side=LEFT, padx=10)
clear_button = Button(
    button_frame,
    text="Clear",
    font=("Segoe UI", 11, "bold"),
    bg="#F59E0B",
    fg="white",
    width=10,
    command=clear
)
clear_button.pack(side=LEFT, padx=10)
edit_button = Button(
    button_frame,
    text="Edit Word",
    font=("Segoe UI", 11, "bold"),
    bg="#9B59B6",
    fg="white",
    width=10,
    command=open_edit_window
)

edit_button.pack(side=LEFT, padx=10)
exit_button = Button(
    button_frame,
    text="Exit",
    font=("Segoe UI", 11, "bold"),
    bg="#374151",
    fg="white",
    width=10,
    command=exit_app
)
exit_button.pack(side=LEFT, padx=10)

delete_button = Button(
    button_frame,
    text="🗑 Delete",
    font=("Segoe UI", 11, "bold"),
    bg="#EF4444",
    fg="white",
    width=10,
    command=open_delete_window
)

delete_button.pack(side=LEFT, padx=10)
# -------------------- FOOTER -------------------- #
speak_button = Button(
    button_frame,
    text="🔊 Speak",
    font=("Segoe UI", 11, "bold"),
    bg="#3B82F6",
    fg="white",
    width=10,
    command=speak_word
)

speak_button.pack(side=LEFT, padx=10)
footer = Label(
    left_panel,
    text="Developed by Kuldeep Singha",
    font=("Arial", 10),
    bg="white",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=10)


# -------------------- RUN APPLICATION -------------------- #
status_label = Label(
    root,
    text="Ready | Total Words: 10",
    font=("Arial", 10),
    bg="#D6EAF8",
    fg="black",
    anchor="w"
)

status_label.pack(side=BOTTOM, fill=X)
root.mainloop()