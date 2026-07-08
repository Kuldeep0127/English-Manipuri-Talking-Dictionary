import json
from tkinter import *
from tkinter import messagebox
from utils import resource_path

def open_edit_window():

    window = Toplevel()
    window.title("Edit Word")
    window.geometry("400x320")
    window.configure(bg="white")
    window.resizable(False, False)

    def load_word():
        word = word_entry.get().strip().title()

        with open(resource_path("dictionary.json"), "r") as file:
            dictionary = json.load(file)

        if word in dictionary:
            meaning_entry.delete(0, END)
            meaning_entry.insert(0, dictionary[word])
        else:
            messagebox.showerror("Error", "Word not found.")

    def save_changes():
        word = word_entry.get().strip().title()
        meaning = meaning_entry.get().strip().title()

        with open(resource_path("dictionary.json"), "r") as file:
            dictionary = json.load(file)

        dictionary[word] = meaning

        with open(resource_path("dictionary.json"), "w") as file:
            json.dump(dictionary, file, indent=4)

        messagebox.showinfo("Success", "Word updated successfully!")
        window.destroy()

    Label(
        window,
        text="Edit Word",
        font=("Arial", 18, "bold"),
        bg="white"
    ).pack(pady=15)

    Label(window, text="Word", bg="white").pack()

    word_entry = Entry(window, width=30, font=("Arial", 12))
    word_entry.pack(pady=5)

    Button(
        window,
        text="Load",
        command=load_word,
        bg="#3498DB",
        fg="white"
    ).pack(pady=5)

    Label(window, text="Meaning", bg="white").pack()

    meaning_entry = Entry(window, width=30, font=("Arial", 12))
    meaning_entry.pack(pady=5)

    Button(
        window,
        text="Save Changes",
        command=save_changes,
        bg="#27AE60",
        fg="white"
    ).pack(pady=15)