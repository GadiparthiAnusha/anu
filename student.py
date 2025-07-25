import tkinter as tk
from tkinter import messagebox
import csv
import os

# Function to save data to CSV
def save_data():
    name = entry_name.get()
    roll = entry_roll.get()
    age = entry_age.get()
    gender = gender_var.get()
    dept = entry_dept.get()

    if not all([name, roll, age, gender, dept]):
        messagebox.showerror("Error", "All fields are required!")
        return

    with open("students.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if os.stat("students.csv").st_size == 0:
            writer.writerow(["Name", "Roll No", "Age", "Gender", "Department"])
        writer.writerow([name, roll, age, gender, dept])

    messagebox.showinfo("Success", "Data saved successfully!")

    # Clear fields
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_dept.delete(0, tk.END)
    gender_var.set(None)

# GUI Setup
root = tk.Tk()
root.title("Student Bio Data Entry")
root.geometry("400x400")

# Labels and entries
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll No").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Age").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Gender").pack()
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Label(root, text="Department").pack()
entry_dept = tk.Entry(root)
entry_dept.pack()

# Submit button
tk.Button(root, text="Submit", command=save_data).pack(pady=10)

root.mainloop()
