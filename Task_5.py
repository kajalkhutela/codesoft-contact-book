import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

filename = "contacts.csv"

# Initialize CSV file if not exists
if not os.path.exists(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Address"])

# Functions
def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email, address])

    messagebox.showinfo("Success", "Contact added!")
    clear_fields()
    view_contacts()

def view_contacts():
    tree.delete(*tree.get_children())
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            tree.insert("", tk.END, values=row)

def search_contact():
    query = search_var.get().lower()
    tree.delete(*tree.get_children())
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if query in row[0].lower() or query in row[1]:
                tree.insert("", tk.END, values=row)

def select_contact(event):
    selected = tree.focus()
    values = tree.item(selected, 'values')
    if values:
        name_var.set(values[0])
        phone_var.set(values[1])
        email_var.set(values[2])
        address_var.set(values[3])

def update_contact():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Error", "Select a contact to update")
        return

    old_values = tree.item(selected, 'values')
    new_values = [name_var.get(), phone_var.get(), email_var.get(), address_var.get()]

    rows = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row == list(old_values):
                writer.writerow(new_values)
            else:
                writer.writerow(row)

    messagebox.showinfo("Success", "Contact updated!")
    clear_fields()
    view_contacts()

def delete_contact():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Error", "Select a contact to delete")
        return

    values = tree.item(selected, 'values')
    rows = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row != list(values):
                writer.writerow(row)

    messagebox.showinfo("Deleted", "Contact deleted!")
    clear_fields()
    view_contacts()

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")
    search_var.set("")

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("800x520")
root.resizable(False, False)
root.configure(bg="#f0f4f7")

# Styling
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
    font=("Segoe UI", 10, "bold"),
    padding=6,
    background="#007acc",
    foreground="white")
style.map("TButton", background=[("active", "#005f99")])

style.configure("Treeview",
    font=("Segoe UI", 10),
    rowheight=25,
    background="white",
    fieldbackground="white",
    foreground="black")
style.configure("Treeview.Heading",
    font=("Segoe UI", 11, "bold"),
    background="#007acc",
    foreground="white")
style.map("Treeview", background=[("selected", "#cce6ff")])

# Variables
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

# Input Frame
frame = tk.LabelFrame(root, text=" Contact Details ", padx=10, pady=10, bg="#f0f4f7", font=("Segoe UI", 11, "bold"))
frame.pack(padx=10, pady=10, fill="x")

tk.Label(frame, text="Name:", bg="#f0f4f7", font=("Segoe UI", 10)).grid(row=0, column=0)
tk.Entry(frame, textvariable=name_var, width=30, font=("Segoe UI", 10)).grid(row=0, column=1, padx=10)

tk.Label(frame, text="Phone:", bg="#f0f4f7", font=("Segoe UI", 10)).grid(row=0, column=2)
tk.Entry(frame, textvariable=phone_var, width=30, font=("Segoe UI", 10)).grid(row=0, column=3, padx=10)

tk.Label(frame, text="Email:", bg="#f0f4f7", font=("Segoe UI", 10)).grid(row=1, column=0)
tk.Entry(frame, textvariable=email_var, width=30, font=("Segoe UI", 10)).grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Address:", bg="#f0f4f7", font=("Segoe UI", 10)).grid(row=1, column=2)
tk.Entry(frame, textvariable=address_var, width=30, font=("Segoe UI", 10)).grid(row=1, column=3, padx=10, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=5)

ttk.Button(btn_frame, text="Add", width=12, command=add_contact).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Update", width=12, command=update_contact).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Delete", width=12, command=delete_contact).grid(row=0, column=2, padx=5)
ttk.Button(btn_frame, text="Clear", width=12, command=clear_fields).grid(row=0, column=3, padx=5)

# Search
search_frame = tk.Frame(root, bg="#f0f4f7")
search_frame.pack(pady=5)

tk.Entry(search_frame, textvariable=search_var, width=40, font=("Segoe UI", 10)).grid(row=0, column=0, padx=5)
ttk.Button(search_frame, text="Search", command=search_contact).grid(row=0, column=1)

# Treeview
tree_frame = tk.Frame(root)
tree_frame.pack(padx=10, pady=10, fill="both", expand=True)

tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.pack(side="right", fill="y")

tree = ttk.Treeview(tree_frame, columns=("Name", "Phone", "Email", "Address"), show='headings', yscrollcommand=tree_scroll.set)
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")
tree.heading("Address", text="Address")

tree.column("Name", width=150)
tree.column("Phone", width=120)
tree.column("Email", width=180)
tree.column("Address", width=250)

tree.bind("<ButtonRelease-1>", select_contact)
tree.pack(fill="both", expand=True)
tree_scroll.config(command=tree.yview)

# Load existing contacts
view_contacts()

# Start GUI
root.mainloop()

