import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class SmartMomPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Mom Planner")
        self.root.geometry("400x500")
        self.notes = []

        # Background color animation variables
        self.bg_colors = ["#f0f8ff", "#d1e7ff", "#a3c9ff", "#75abff", "#478dff", "#1a6fff"]
        self.bg_index = 0
        self.animate_background()

        # Title
        tk.Label(root, text="Smart Mom Planner", font=("Arial", 16, "bold")).pack(pady=10)

        # Child info
        tk.Label(root, text="Child's Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)
        self.name_entry.bind("<KeyRelease>", self.update_funny_name)

        # Funny name display label
        self.funny_name_label = tk.Label(root, text="", font=("Comic Sans MS", 14, "bold"))
        self.funny_name_label.pack(pady=5)
        self.funny_name_color_index = 0
        self.animate_funny_name_color()

        tk.Label(root, text="Child's Age:").pack()
        self.age_entry = tk.Entry(root)
        self.age_entry.pack(pady=5)

        # Daily routine
        tk.Label(root, text="\n🕒 Daily Routine", font=("Arial", 12, "bold")).pack()
        tk.Label(root, text="- Breakfast: 8:00 AM\n- Nap: 12:00 PM\n- Lunch: 1:30 PM\n- Playtime: 4:00 PM\n- Dinner: 7:00 PM\n- Bedtime: 9:00 PM").pack()

        # Notes section
        tk.Label(root, text="\n📝 Add Note").pack()
        self.note_entry = tk.Entry(root, width=30)
        self.note_entry.pack(pady=5)
        tk.Button(root, text="Add Note", command=self.add_note).pack()

        # Notes display
        self.notes_box = tk.Listbox(root, width=50)
        self.notes_box.pack(pady=10)

        # Start reminder loop
        self.reminder_loop()

    def animate_background(self):
        self.root.configure(bg=self.bg_colors[self.bg_index])
        self.bg_index = (self.bg_index + 1) % len(self.bg_colors)
        self.root.after(1000, self.animate_background)  # Change color every 1 second

    def update_funny_name(self, event=None):
        name = self.name_entry.get()
        # Create a funny version by alternating uppercase and lowercase letters
        funny_name = "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(name))
        self.funny_name_label.config(text=funny_name)

    def animate_funny_name_color(self):
        colors = ["#e74c3c", "#f39c12", "#27ae60", "#2980b9", "#8e44ad", "#c0392b"]
        self.funny_name_label.config(fg=colors[self.funny_name_color_index])
        self.funny_name_color_index = (self.funny_name_color_index + 1) % len(colors)
        self.root.after(500, self.animate_funny_name_color)  # Change color every 0.5 seconds

    def add_note(self):
        note = self.note_entry.get()
        if note:
            timestamp = datetime.now().strftime("%H:%M")
            full_note = f"[{timestamp}] {note}"
            self.notes.append(full_note)
            self.notes_box.insert(tk.END, full_note)
            self.note_entry.delete(0, tk.END)

    def reminder_loop(self):
        now = datetime.now().strftime("%H:%M")
        if now in ["08:00", "12:00", "13:30", "16:00", "19:00", "21:00"]:
            messagebox.showinfo("Reminder", f"It's time for a routine activity! ({now})")
        # Recheck every 60 seconds
        self.root.after(60000, self.reminder_loop)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartMomPlanner(root)
    root.mainloop()
