import json
from tkinter import *
from tkinter import messagebox
from utils import resource_path

def open_add_window():

    window = Toplevel()
    window.title("Add New Word")
    window.geometry("400x280")
    window.configure(bg="white")
    window.resizable(False, False)

    def save_word():
        word = word_entry.get().strip().title()
        meaning = meaning_entry.get().strip().title()

        if word == "" or meaning == "":
            messagebox.showerror("Error", "Please fill in both fields.")
            return

        with open(resource_path("dictionary.json"), "r") as file:
            dictionary = json.load(file)

        if word in dictionary:
            messagebox.showwarning(
                "Already Exists",
                "This word already exists in the dictionary."
            )
            return

        dictionary[word] = meaning

        with open(resource_path("dictionary.json"), "w") as file:
            json.dump(dictionary, file, indent=4)

        messagebox.showinfo(
            "Success",
            "Word added successfully!"
        )

        window.destroy()

    title = Label(
        window,
        text="Add New Word",
        font=("Arial", 18, "bold"),
        bg="white"
    )
    title.pack(pady=15)

    word_label = Label(
        window,
        text="Word",
        font=("Arial", 12),
        bg="white"
    )
    word_label.pack()

    word_entry = Entry(
        window,
        font=("Arial", 12),
        width=30
    )
    word_entry.pack(pady=5)

    meaning_label = Label(
        window,
        text="Meaning",
        font=("Arial", 12),
        bg="white"
    )
    meaning_label.pack()

    meaning_entry = Entry(
        window,
        font=("Arial", 12),
        width=30
    )
    meaning_entry.pack(pady=5)

    save_button = Button(
        window,
        text="Save",
        font=("Arial", 12, "bold"),
        bg="#27AE60",
        fg="white",
        width=12,
        command=save_word
    )
    save_button.pack(pady=15)

    cancel_button = Button(
        window,
        text="Cancel",
        font=("Arial", 12, "bold"),
        bg="#E74C3C",
        fg="white",
        width=12,
        command=window.destroy
    )
    cancel_button.pack()