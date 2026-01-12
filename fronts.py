import tkinter
from tkinter import font

root = tkinter.Tk()
root.title("Installed Fonts and Styles")

# Scrollable area
canvas = tkinter.Canvas(root)
scrollbar = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tkinter.Frame(canvas)

canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=frame, anchor="nw")

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_configure)
canvas.bind_all("<Mousewheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

# Get font families
families = sorted(font.families())

separator = tkinter.Label(frame, text="─" * 80, fg="gray")
separator.pack(pady=(10, 10))

# List fonts without styles
fonts_label = tkinter.Label(frame, text="Installed fonts:", font=("Arial", 14, "bold"), fg="blue")
fonts_label.pack(anchor="w", pady=(0, 5))

for family in families:
    family_label = tkinter.Label(frame, text=f"{family}", font=(family, 12))
    family_label.pack(anchor="w")

root.mainloop()
