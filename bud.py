import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

# Save to CSV
def save_entry():
    date = datetime.now().strftime('%Y-%m-%d')
    category = category_var.get()
    amount = amount_entry.get()
    note = note_entry.get()

    if not amount.strip().isdigit():
        messagebox.showerror("Invalid Input", "Amount must be a number.")
        return

    # Save to CSV
    with open('budget_data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])

    messagebox.showinfo("Saved", f"{category} entry saved successfully.")
    amount_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)
    load_data()

# Load data to display
def load_data():
    for row in tree.get_children():
        tree.delete(row)

    total_income = 0
    total_expense = 0

    try:
        with open('budget_data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                tree.insert('', tk.END, values=row)
                if row[1] == "Income":
                    total_income += int(row[2])
                else:
                    total_expense += int(row[2])
    except FileNotFoundError:
        pass

    income_label.config(text=f"Total Income: ₹{total_income}")
    expense_label.config(text=f"Total Expense: ₹{total_expense}")
    balance_label.config(text=f"Balance: ₹{total_income - total_expense}")

# GUI Setup
root = tk.Tk()
root.title("Student Budget Manager")
root.geometry("700x500")
root.config(bg="#eaf4f4")

# Input Fields
tk.Label(root, text="Category").place(x=20, y=20)
category_var = tk.StringVar(value="Expense")
ttk.Combobox(root, textvariable=category_var, values=["Income", "Expense"]).place(x=100, y=20)

tk.Label(root, text="Amount (₹)").place(x=20, y=60)
amount_entry = tk.Entry(root)
amount_entry.place(x=100, y=60)

tk.Label(root, text="Note").place(x=20, y=100)
note_entry = tk.Entry(root, width=40)
note_entry.place(x=100, y=100)

tk.Button(root, text="Add Entry", command=save_entry, bg="green", fg="white").place(x=100, y=140)

# Treeview for table
tree = ttk.Treeview(root, columns=("Date", "Category", "Amount", "Note"), show='headings', height=10)
for col in ("Date", "Category", "Amount", "Note"):
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.place(x=20, y=180)

# Summary Labels
income_label = tk.Label(root, text="Total Income: ₹0", font=("Arial", 10, "bold"), fg="green", bg="#eaf4f4")
income_label.place(x=20, y=430)

expense_label = tk.Label(root, text="Total Expense: ₹0", font=("Arial", 10, "bold"), fg="red", bg="#eaf4f4")
expense_label.place(x=200, y=430)

balance_label = tk.Label(root, text="Balance: ₹0", font=("Arial", 10, "bold"), fg="blue", bg="#eaf4f4")
balance_label.place(x=400, y=430)

# Load existing data
load_data()

root.mainloop()