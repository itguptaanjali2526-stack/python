import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. LIST
# ==========================================

plants = ["Rose", "Tulsi", "Money Plant", "Aloe Vera", "Jasmine"]

prices = [150, 80, 200, 120, 100]

stock = [10, 15, 8, 12, 10]


# ==========================================
# 2. FUNCTIONS
# ==========================================

# Display plants
def display_plants():

    output.delete("1.0", tk.END)

    for i in range(len(plants)):

        output.insert(
            tk.END,
            f"{i + 1}. {plants[i]}   "
            f"Price: ₹{prices[i]}   "
            f"Stock: {stock[i]}\n"
        )


# Search plant
def search_plant():

    name = search_entry.get()

    output.delete("1.0", tk.END)

    found = False

    for i in range(len(plants)):

        # 3. IF-ELSE + 4. STRING
        if name.lower() == plants[i].lower():

            output.insert(
                tk.END,
                "🌸 PLANT FOUND\n\n"
                f"Plant Name : {plants[i]}\n"
                f"Price      : ₹{prices[i]}\n"
                f"Stock      : {stock[i]}"
            )

            found = True

    if found == False:

        output.insert(
            tk.END,
            "❌ Plant not found!"
        )


# Buy plant
def buy_plant():

    customer = customer_entry.get()
    plant_name = buy_entry.get()
    quantity_text = quantity_entry.get()

    # IF-ELSE
    if customer == "" or plant_name == "" or quantity_text == "":

        messagebox.showwarning(
            "Warning",
            "Please enter all details!"
        )

        return

    # Check quantity
    if not quantity_text.isdigit():

        messagebox.showerror(
            "Error",
            "Quantity must be a number!"
        )

        return

    quantity = int(quantity_text)

    found = False

    for i in range(len(plants)):

        # STRING comparison
        if plant_name.lower() == plants[i].lower():

            found = True

            # IF-ELSE
            if quantity <= 0:

                messagebox.showerror(
                    "Error",
                    "Quantity must be greater than 0!"
                )

            elif quantity > stock[i]:

                messagebox.showerror(
                    "Error",
                    "Not enough stock available!"
                )

            else:

                total = prices[i] * quantity

                stock[i] = stock[i] - quantity

                messagebox.showinfo(
                    "Purchase Successful",
                    f"🌸 Customer: {customer}\n"
                    f"🌱 Plant: {plants[i]}\n"
                    f"Quantity: {quantity}\n"
                    f"Total Bill: ₹{total}"
                )

                display_plants()

            break

    if found == False:

        messagebox.showerror(
            "Error",
            "Plant not found!"
        )


# Clear fields
def clear_fields():

    customer_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)
    buy_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

    output.delete("1.0", tk.END)


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("🌸 Plant Nursery Management System")

root.geometry("850x650")

root.resizable(False, False)

# Pink Pastel Background
root.configure(
    bg="#FCE4EC"
)


# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    root,
    text="🌸 PLANT NURSERY MANAGEMENT SYSTEM 🌸",
    font=("Arial", 23, "bold"),
    bg="#E8A0BF",
    fg="white",
    pady=15
)

title.pack(
    fill="x",
    pady=10
)


subtitle = tk.Label(
    root,
    text="Simple Plant Management System",
    font=("Arial", 11, "italic"),
    bg="#FCE4EC",
    fg="#6D3B4B"
)

subtitle.pack(
    pady=5
)


# ==========================================
# PLANT DISPLAY
# ==========================================

plant_frame = tk.LabelFrame(
    root,
    text="🌷 Available Plants",
    font=("Arial", 13, "bold"),
    bg="#F8BBD0",
    fg="#6D3B4B"
)

plant_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


output = tk.Text(
    plant_frame,
    height=8,
    width=80,
    font=("Arial", 12),
    bg="#FFF5F8",
    fg="#6D3B4B"
)

output.pack(
    padx=10,
    pady=10
)


# ==========================================
# SEARCH
# ==========================================

search_frame = tk.LabelFrame(
    root,
    text="🔍 Search Plant",
    font=("Arial", 12, "bold"),
    bg="#F8BBD0",
    fg="#6D3B4B"
)

search_frame.pack(
    fill="x",
    padx=30,
    pady=5
)


search_entry = tk.Entry(
    search_frame,
    width=30,
    font=("Arial", 11),
    bg="#FFF5F8"
)

search_entry.pack(
    side="left",
    padx=15,
    pady=10
)


tk.Button(
    search_frame,
    text="🔍 Search",
    command=search_plant,
    bg="#D88AA5",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15
).pack(
    side="left"
)


# ==========================================
# CUSTOMER + BUY
# ==========================================

buy_frame = tk.LabelFrame(
    root,
    text="🛒 Customer Purchase",
    font=("Arial", 12, "bold"),
    bg="#F8BBD0",
    fg="#6D3B4B"
)

buy_frame.pack(
    fill="x",
    padx=30,
    pady=8
)


# Customer Name

tk.Label(
    buy_frame,
    text="Customer:",
    bg="#F8BBD0",
    fg="#6D3B4B",
    font=("Arial", 10, "bold")
).grid(
    row=0,
    column=0,
    padx=8,
    pady=10
)


customer_entry = tk.Entry(
    buy_frame,
    width=18,
    bg="#FFF5F8"
)

customer_entry.grid(
    row=0,
    column=1,
    padx=5
)


# Plant Name

tk.Label(
    buy_frame,
    text="Plant:",
    bg="#F8BBD0",
    fg="#6D3B4B",
    font=("Arial", 10, "bold")
).grid(
    row=0,
    column=2,
    padx=8
)


buy_entry = tk.Entry(
    buy_frame,
    width=18,
    bg="#FFF5F8"
)

buy_entry.grid(
    row=0,
    column=3,
    padx=5
)


# Quantity

tk.Label(
    buy_frame,
    text="Quantity:",
    bg="#F8BBD0",
    fg="#6D3B4B",
    font=("Arial", 10, "bold")
).grid(
    row=0,
    column=4,
    padx=8
)


quantity_entry = tk.Entry(
    buy_frame,
    width=8,
    bg="#FFF5F8"
)

quantity_entry.grid(
    row=0,
    column=5,
    padx=5
)


# Buy Button

tk.Button(
    buy_frame,
    text="🛒 Buy",
    command=buy_plant,
    bg="#D88AA5",
    fg="white",
    font=("Arial", 10, "bold"),
    width=12
).grid(
    row=0,
    column=6,
    padx=10
)


# ==========================================
# BUTTONS
# ==========================================

button_frame = tk.Frame(
    root,
    bg="#FCE4EC"
)

button_frame.pack(
    pady=15
)


# Display

tk.Button(
    button_frame,
    text="🌸 Display Plants",
    command=display_plants,
    bg="#D88AA5",
    fg="white",
    font=("Arial", 10, "bold"),
    width=17
).grid(
    row=0,
    column=0,
    padx=7
)


# Clear

tk.Button(
    button_frame,
    text="🧹 Clear",
    command=clear_fields,
    bg="#BFA5AE",
    fg="white",
    font=("Arial", 10, "bold"),
    width=17
).grid(
    row=0,
    column=1,
    padx=7
)


# Exit

tk.Button(
    button_frame,
    text="❌ Exit",
    command=root.destroy,
    bg="#9E7B86",
    fg="white",
    font=("Arial", 10, "bold"),
    width=17
).grid(
    row=0,
    column=2,
    padx=7
)


# ==========================================
# FOOTER
# ==========================================

footer = tk.Label(
    root,
    text="🌷 Welcome to Pink Blossom Nursery 🌷",
    font=("Arial", 10, "italic"),
    bg="#FCE4EC",
    fg="#6D3B4B"
)

footer.pack(
    pady=5
)


# ==========================================
# START PROGRAM
# ==========================================

display_plants()

root.mainloop()
