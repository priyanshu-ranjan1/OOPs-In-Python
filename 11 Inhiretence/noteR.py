import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font
import os

# --- Golden Silverish Theme ---
# A modern theme with gold and silver accents on a dark background.
COLOR_PALETTE = {
    "background": "#2B2B2B",      # Dark charcoal background
    "foreground": "#D3D3D3",      # Light silver text
    "widget_bg": "#3C3F41",       # Slightly lighter bg for listbox
    "accent_gold": "#DAA520",     # GoldenRod for buttons and highlights
    "accent_silver": "#C0C0C0",   # Silver for cursor/borders
    "text_editor_bg": "#1E1E1E",  # Very dark bg for the text editor
    "list_select_bg": "#DAA520",  # Gold for selected item in the list
    "button_active": "#F0C44D"    # Lighter gold for button hover/press
}

FONT_FAMILY = "Segoe UI"
FONT_NORMAL = (FONT_FAMILY, 11)
FONT_BOLD = (FONT_FAMILY, 12, "bold")
FONT_TITLE = (FONT_FAMILY, 16, "bold")

# --- Main Application Class ---
class NoteRApp:
    """The main class for the noteR application GUI and logic."""
    
    def __init__(self, root, workspace_path):
        self.root = root
        self.workspace_path = workspace_path
        self.current_file_path = None

        self.setup_ui()
        self.populate_notes_list()

    def setup_ui(self):
        """Creates and arranges all the widgets in the main window."""
        self.root.title("noteR")
        self.root.geometry("1100x750")
        self.root.configure(bg=COLOR_PALETTE["background"])
        self.root.minsize(800, 600)

        # --- Main Layout Frames ---
        main_frame = tk.Frame(self.root, bg=COLOR_PALETTE["background"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(1, weight=3) # Editor frame gets more space

        # --- Header ---
        header_frame = tk.Frame(main_frame, bg=COLOR_PALETTE["background"])
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        title_label = tk.Label(
            header_frame, text="noteR", font=FONT_TITLE,
            bg=COLOR_PALETTE["background"], fg=COLOR_PALETTE["accent_gold"]
        )
        title_label.pack(side=tk.LEFT, padx=5)

        # --- Control Buttons ---
        button_style = {
            "font": FONT_BOLD, "bg": COLOR_PALETTE["accent_gold"],
            "fg": COLOR_PALETTE["background"], "activebackground": COLOR_PALETTE["button_active"],
            "activeforeground": COLOR_PALETTE["background"], "relief": tk.FLAT,
            "bd": 0, "padx": 12, "pady": 6
        }
        
        delete_note_btn = tk.Button(header_frame, text="🗑️ Delete", **button_style, command=self.delete_note)
        delete_note_btn.pack(side=tk.RIGHT, padx=5)
        
        save_note_btn = tk.Button(header_frame, text="💾 Save", **button_style, command=self.save_note)
        save_note_btn.pack(side=tk.RIGHT, padx=5)

        new_note_btn = tk.Button(header_frame, text="✨ New Note", **button_style, command=self.new_note)
        new_note_btn.pack(side=tk.RIGHT, padx=5)
        
        # --- Sidebar (Notes List) ---
        sidebar_frame = tk.Frame(main_frame, bg=COLOR_PALETTE["widget_bg"], width=300)
        sidebar_frame.grid(row=1, column=0, sticky="ns", padx=(0, 10))
        sidebar_frame.grid_propagate(False)

        self.notes_listbox = tk.Listbox(
            sidebar_frame, bg=COLOR_PALETTE["widget_bg"], fg=COLOR_PALETTE["foreground"],
            font=FONT_NORMAL, selectbackground=COLOR_PALETTE["list_select_bg"],
            selectforeground=COLOR_PALETTE["background"], borderwidth=0,
            highlightthickness=0, relief=tk.FLAT
        )
        self.notes_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.notes_listbox.bind("<<ListboxSelect>>", self.on_note_select)

        # --- Text Editor ---
        editor_frame = tk.Frame(main_frame, bg=COLOR_PALETTE["text_editor_bg"])
        editor_frame.grid(row=1, column=1, sticky="nsew")

        self.text_editor = tk.Text(
            editor_frame, bg=COLOR_PALETTE["text_editor_bg"], fg=COLOR_PALETTE["foreground"],
            font=FONT_NORMAL, insertbackground=COLOR_PALETTE["accent_silver"], # Cursor color
            selectbackground=COLOR_PALETTE["accent_gold"], selectforeground=COLOR_PALETTE["background"],
            wrap=tk.WORD, undo=True, borderwidth=0, highlightthickness=0
        )
        self.text_editor.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

    def populate_notes_list(self):
        """Clears and re-populates the notes list from the workspace directory."""
        self.notes_listbox.delete(0, tk.END)
        try:
            notes = sorted([f for f in os.listdir(self.workspace_path) if f.endswith(".md")])
            for note in notes:
                self.notes_listbox.insert(tk.END, note)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Directory not found: {self.workspace_path}")
            self.root.destroy()

    def on_note_select(self, event=None):
        """Handles opening a note when it's clicked in the listbox."""
        if not self.notes_listbox.curselection():
            return

        selected_note = self.notes_listbox.get(self.notes_listbox.curselection())
        self.current_file_path = os.path.join(self.workspace_path, selected_note)

        try:
            with open(self.current_file_path, "r", encoding="utf-8") as file:
                content = file.read()
            self.text_editor.delete("1.0", tk.END)
            self.text_editor.insert("1.0", content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open note: {e}")
            self.current_file_path = None

    def new_note(self):
        """Creates a new, empty .md note file."""
        note_name = simpledialog.askstring("New Note", "Enter a name for your new note:", parent=self.root)
        if not note_name:
            return

        note_name = f"{note_name}.md" if not note_name.endswith(".md") else note_name
        new_file_path = os.path.join(self.workspace_path, note_name)

        if os.path.exists(new_file_path):
            messagebox.showwarning("Warning", f"A note named '{note_name}' already exists.")
            return

        try:
            # Create a new file with a default Markdown title
            with open(new_file_path, "w", encoding="utf-8") as file:
                file.write(f"# {note_name.replace('.md', '')}\n\n")
            
            self.populate_notes_list()
            # Automatically select and open the new note
            if note_name in self.notes_listbox.get(0, tk.END):
                idx = self.notes_listbox.get(0, tk.END).index(note_name)
                self.notes_listbox.selection_set(idx)
                self.on_note_select()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to create new note: {e}")

    def save_note(self):
        """Saves the content of the text editor to the current file."""
        if not self.current_file_path:
            messagebox.showwarning("Warning", "No note is open. Please select or create a note.")
            return

        content = self.text_editor.get("1.0", tk.END)
        try:
            with open(self.current_file_path, "w", encoding="utf-8") as file:
                file.write(content)
            messagebox.showinfo("Success", f"Note '{os.path.basename(self.current_file_path)}' saved.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save note: {e}")

    def delete_note(self):
        """Deletes the selected note after confirmation."""
        if not self.notes_listbox.curselection():
            messagebox.showwarning("Warning", "Please select a note to delete.")
            return

        note_name = self.notes_listbox.get(self.notes_listbox.curselection())
        confirm = messagebox.askyesno(
            "Confirm Deletion", f"Are you sure you want to permanently delete '{note_name}'?", icon='warning'
        )

        if confirm:
            file_to_delete = os.path.join(self.workspace_path, note_name)
            try:
                os.remove(file_to_delete)
                self.populate_notes_list()
                self.text_editor.delete("1.0", tk.END)
                self.current_file_path = None
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete note: {e}")

# --- Startup Logic ---
def start_up_dialog(root):
    """Shows a dialog to select or create a notes folder before the app loads."""
    dialog = tk.Toplevel(root)
    dialog.title("Welcome to noteR")
    dialog.geometry("450x220")
    dialog.configure(bg=COLOR_PALETTE["background"])
    dialog.resizable(False, False)

    # Center the dialog on the screen
    x = root.winfo_screenwidth() // 2 - 225
    y = root.winfo_screenheight() // 2 - 110
    dialog.geometry(f"+{x}+{y}")
    
    dialog.protocol("WM_DELETE_WINDOW", root.destroy) # Exit app if this window is closed
    
    workspace = {"path": None} # Use a dictionary to pass the path out

    def select_folder():
        path = filedialog.askdirectory(title="Select a folder to store your notes")
        if path:
            workspace["path"] = path
            dialog.destroy()

    def create_folder():
        path = filedialog.askdirectory(title="Select a parent directory for your new folder")
        if not path: return
        
        folder_name = simpledialog.askstring("New Folder", "Enter name for new notes folder:", parent=dialog)
        if folder_name:
            new_path = os.path.join(path, folder_name)
            try:
                os.makedirs(new_path, exist_ok=True)
                workspace["path"] = new_path
                dialog.destroy()
            except OSError as e:
                messagebox.showerror("Error", f"Could not create folder: {e}", parent=dialog)

    # --- Dialog Widgets ---
    label = tk.Label(
        dialog, text="Choose a workspace for your notes.", font=FONT_BOLD,
        bg=COLOR_PALETTE["background"], fg=COLOR_PALETTE["foreground"], pady=25
    )
    label.pack()

    button_frame = tk.Frame(dialog, bg=COLOR_PALETTE["background"])
    button_frame.pack(pady=10)

    btn_style = {
        "font": FONT_BOLD, "bg": COLOR_PALETTE["accent_gold"], "fg": COLOR_PALETTE["background"],
        "activebackground": COLOR_PALETTE["button_active"], "activeforeground": COLOR_PALETTE["background"],
        "relief": tk.FLAT, "bd": 0, "padx": 15, "pady": 8
    }

    btn_select = tk.Button(button_frame, text="Select Existing Folder", **btn_style, command=select_folder)
    btn_select.pack(side=tk.LEFT, padx=12)
    
    btn_create = tk.Button(button_frame, text="Create New Folder", **btn_style, command=create_folder)
    btn_create.pack(side=tk.LEFT, padx=12)

    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)
    
    return workspace["path"]

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window until the workspace is chosen

    workspace_path = start_up_dialog(root)

    if workspace_path:
        root.deiconify()  # Show the main window now
        app = NoteRApp(root, workspace_path)
        root.mainloop()
    else:
        # If no folder was chosen, the program exits cleanly.
        root.destroy()