import tkinter as tk
import time

# Sample sentence
TEXT_TO_TYPE = "The quick brown fox jumps over the lazy dog."

# Start time tracker
start_time = 0

def start_typing():
    global start_time
    start_time = time.time()
    entry.delete(0, tk.END)
    result_label.config(text="")
    entry.config(state='normal')
    entry.focus()

def stop_typing():
    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    typed_text = entry.get()
    entry.config(state='disabled')

    if typed_text == TEXT_TO_TYPE:
        result_label.config(text=f"Correct! Time taken: {total_time} seconds", fg='green')
    else:
        result_label.config(text=f"Incorrect typing.\nTime taken: {total_time} seconds", fg='red')

# GUI setup
root = tk.Tk()
root.title("Speed Typing Test")
root.geometry("800x300")
root.config(bg="lightblue")

# Labels and Entry
instruction = tk.Label(root, text="Type the following sentence as fast as you can:", bg="lightblue", font=("Arial", 14))
instruction.pack(pady=10)

text_label = tk.Label(root, text=TEXT_TO_TYPE, font=("Courier", 16, "bold"), bg="lightblue", wraplength=750)
text_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=80, state='disabled')
entry.pack(pady=10)

# Buttons
start_button = tk.Button(root, text="Start", command=start_typing, font=("Arial", 12), bg="green", fg="white", width=10)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_typing, font=("Arial", 12), bg="red", fg="white", width=10)
stop_button.pack(pady=5)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
result_label.pack(pady=10)

root.mainloop()
