import tkinter as tk
from PIL import Image, ImageTk


class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Multimodal AI Interactive Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        # Image display
        self.img_label = tk.Label(self.root, bg="white")
        self.img_label.pack()

        # Text display
        self.text_label = tk.Label(
            self.root,
            text="Welcome to Multimodal AI Assistant",
            font=("Helvetica", 16),
            bg="white",
            fg="black",
        )
        self.text_label.pack()

        # Add controls
        self.add_controls()

    def update_image(self, image):
        """Update the image displayed in the GUI."""
        photo = ImageTk.PhotoImage(image=Image.fromarray(image))
        self.img_label.config(image=photo)
        self.img_label.image = photo

    def update_text(self, text):
        """Update the text displayed in the GUI."""
        self.text_label.config(text=text)

    def add_controls(self):
        """Add control buttons to the GUI."""
        self.start_button = tk.Button(
            self.root, text="Start", command=self.start_action, bg="lightgreen"
        )
        self.start_button.pack()

        self.stop_button = tk.Button(
            self.root, text="Stop", command=self.stop_action, bg="red"
        )
        self.stop_button.pack()

        self.theme_button = tk.Button(
            self.root, text="Switch Theme", command=self.toggle_theme, bg="lightblue"
        )
        self.theme_button.pack()

    def start_action(self):
        """Placeholder for start action."""
        self.update_text("Process started!")

    def stop_action(self):
        """Placeholder for stop action."""
        self.update_text("Process stopped!")

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        if self.root.cget("bg") == "white":
            self.root.configure(bg="black")
            self.text_label.configure(bg="black", fg="white")
        else:
            self.root.configure(bg="white")
            self.text_label.configure(bg="white", fg="black")
