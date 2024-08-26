import tkinter as tk
from tkinter import ttk, messagebox
import utils
from PIL import Image, ImageTk

class AlwaysOnTopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Always On Top")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', background='#4a7abc', foreground='white', font=('Arial', 10, 'bold'))
        self.style.map('TButton', background=[('active', '#3a5a8c')])
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))

        self.setup_ui()
        self.refresh_window_list()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.pack(fill=tk.BOTH, expand=True)


        # Window list
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)

        list_label = ttk.Label(list_frame, text="Select a window:", anchor="w")
        list_label.pack(fill=tk.X, pady=(0, 5))

        self.window_listbox = tk.Listbox(list_frame, width=50, font=('Arial', 10), bg='white', selectbackground='#4a7abc')
        self.window_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.window_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.window_listbox.config(yscrollcommand=scrollbar.set)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=(20, 0))

        self.pin_button = ttk.Button(button_frame, text="Pin", command=self.pin_window, width=10)
        self.pin_button.pack(side=tk.LEFT, padx=5)

        self.unpin_button = ttk.Button(button_frame, text="Unpin", command=self.unpin_window, width=10)
        self.unpin_button.pack(side=tk.LEFT, padx=5)

        self.refresh_button = ttk.Button(button_frame, text="Refresh", command=self.refresh_window_list, width=10)
        self.refresh_button.pack(side=tk.LEFT, padx=5)

        # Status label
        self.status_label = ttk.Label(main_frame, text="", anchor="center", foreground="#4a7abc")
        self.status_label.pack(pady=(20, 0))

    def refresh_window_list(self):
        self.window_listbox.delete(0, tk.END)
        windows = utils.list_windows()
        for window in windows:
            self.window_listbox.insert(tk.END, window.title)

    def pin_window(self):
        selected_index = self.window_listbox.curselection()
        if selected_index:
            window_title = self.window_listbox.get(selected_index)
            utils.pin_window(window_title)
            self.status_label.config(text=f"Window '{window_title}' pinned successfully.")
        else:
            messagebox.showwarning("No Selection", "Please select a window to pin.")

    def unpin_window(self):
        selected_index = self.window_listbox.curselection()
        if selected_index:
            window_title = self.window_listbox.get(selected_index)
            utils.unpin_window(window_title)
            self.status_label.config(text=f"Window '{window_title}' unpinned successfully.")
        else:
            messagebox.showwarning("No Selection", "Please select a window to unpin.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlwaysOnTopApp(root)
    root.mainloop()