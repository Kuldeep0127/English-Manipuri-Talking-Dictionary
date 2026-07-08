import json
from tkinter import *
from tkinter import messagebox
from utils import resource_path

# -------------------------------
# Function to delete a word
# -------------------------------
def delete_word(word):
    # Load dictionary
    with open(resource_path("dictionary.json"), "r") as file:
        dictionary = json.load(file)

    word = word.strip().title()

    # Check if word exists
    if word in dictionary:
        del dictionary[word]

        # Save updated dictionary
        with open(resource_path("dictionary.json"), "w") as file:
            json.dump(dictionary, file, indent=4)

        return True

    return False


# -------------------------------
# Delete Word Window
# -------------------------------
def open_delete_window():
    window = Toplevel()

    window.title("Delete Word")
    window.geometry("400x250")
    window.configure(bg="white")
    window.resizable(False, False)

    # Title
    title = Label(
        window,
        text="🗑 Delete Word",
        font=("Segoe UI", 18, "bold"),
        bg="white",
        fg="#E74C3C"
    )
    title.pack(pady=15)

    # Word Label
    word_label = Label(
        window,
        text="Enter Word",
        font=("Segoe UI", 12),
        bg="white"
    )
    word_label.pack()

    # Entry Box
    word_entry = Entry(
        window,
        font=("Segoe UI", 12),
        width=30
    )
    word_entry.pack(pady=8)
    word_entry.focus()

    # Delete Button Function
    def perform_delete():
        word = word_entry.get().strip()

        if word == "":
            messagebox.showerror("Error", "Please enter a word.")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete '{word}'?"
        )

        if not confirm:
            return

        if delete_word(word):
            messagebox.showinfo("Success", "Word deleted successfully!")
            window.destroy()
        else:
            messagebox.showerror("Error", "Word not found.")

    # Delete Button
    delete_btn = Button(
        window,
        text="🗑 Delete",
        font=("Segoe UI", 12, "bold"),
        bg="#E74C3C",
        fg="white",
        width=15,
        command=perform_delete
    )
    delete_btn.pack(pady=20)