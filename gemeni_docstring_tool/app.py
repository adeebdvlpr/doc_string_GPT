# app.py - Contains the App class definition
# app.py
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from custom_crew import CustomCrew
from Capabilities.file_collecting import collect_ts_files, queue_ts_files

class App:
    def __init__(self, master):
        self.master = master
        master.title("Documentation Generator Tool")

        # Apply a theme and color scheme
        self.style = ttk.Style()
        self.style.theme_use('aqua')  # Change theme (you can use other themes like 'clam', 'alt', etc.)
        self.style.configure('.', background='#4b5320')  # Change background color for all widgets

        # Create GUI components using themed widgets (ttk)
        self.label = ttk.Label(master, text="Choose a directory or files:")
        self.label.pack()

        self.text_area = scrolledtext.ScrolledText(master, height=30, width=100)
        self.text_area.pack()

        self.button_frame = ttk.Frame(master)
        self.button_frame.pack()

        self.browse_button = ttk.Button(self.button_frame, text="Browse", command=self.browse_files)
        self.browse_button.pack(side=tk.LEFT)

        self.run_button = ttk.Button(self.button_frame, text="Let 'er rip", command=self.run_application)
        self.run_button.pack(side=tk.LEFT)

        # Add padding and spacing
        self.style.configure('TFrame', padding=10)  # Add padding to all frames
        self.style.configure('TButton', padding=(10, 5))  # Add padding to all buttons
        self.button_frame.pack(pady=10)  # Add vertical spacing around the button frame

    def browse_files(self):
        file_path = filedialog.askdirectory()  # Allow user to select a directory
        self.text_area.insert(tk.END, f"Selected directory: {file_path}\n")
        self.file_path = file_path

    def run_application(self):
        if hasattr(self, 'file_path'):
            file_paths = collect_ts_files(self.file_path)
            file_queue = queue_ts_files(file_paths)
            CustomCrew.process_files(file_queue)
            self.text_area.insert(tk.END, "The application has completed. Your code file now contains proper documentation.\n")
        else:
            self.text_area.insert(tk.END, "Please select a directory first.\n")

    # Start GUI
    def run_gui():
        root = tk.Tk()
        app = App(root)
        root.mainloop()
