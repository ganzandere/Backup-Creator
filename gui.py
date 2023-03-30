import os
from tkinter import filedialog as fd

import customtkinter as ctk

from backup_creator import file_copier
from helpers import get_drive_letters


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("Backup Creator v0.1")
        self.geometry("700x650")
        self.maxsize(700, 650)
        self.minsize(700, 650)

        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.font = ctk.CTkFont("Inter",size=12,weight="bold")
        self.icon = "dk.ico"
        self.iconPath = self.resource_path(f'{os.path.dirname(__file__)}/icons/dk.ico')
        self.iconbitmap(self.iconPath)

        self.destination_frame = ctk.CTkFrame(master=self)
        self.destination_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.destination_letter_label = ctk.CTkLabel(master=self.destination_frame, text="Destination Drive",  font=self.font)
        self.destination_letter_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.destination_letter_optionbox = ctk.CTkOptionMenu(master=self.destination_frame, values=get_drive_letters(), width=60, font=self.font, fg_color="#e53935", button_color="#4c1b1b")
        self.destination_letter_optionbox.grid(row=0, column=1, padx=10, pady=10)

        self.files_frame = ctk.CTkFrame(master=self)
        self.files_frame.grid(row=0, column=0, padx=10, pady=5)

        self.files_entry = ctk.CTkEntry(master=self.files_frame, placeholder_text="Path to .txt file containing files for backup.", width=500,  font=self.font)
        self.files_entry.grid(row=0, column=0, padx=10, pady=10)

        self.files_button = ctk.CTkButton(master=self.files_frame, text="Browse", font=self.font, command=self.browse_callback, fg_color="#4c1b1b")
        self.files_button.grid(row=0, column=1, padx=10, pady=10)

        self.backup_frame = ctk.CTkFrame(master=self)
        self.backup_frame.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.preview_button = ctk.CTkButton(master=self.backup_frame, text="Preview",  font=self.font, command=self.preview_callback, fg_color="#4c1b1b")
        self.preview_button.grid(row=0, column=0, padx=10, pady=10)

        self.backup_button = ctk.CTkButton(master=self.backup_frame, text="Backup",  font=self.font, command=self.backup_callback, fg_color="#e53935")
        self.backup_button.grid(row=0, column=1, padx=10, pady=10)

        self.options = ctk.CTkFrame(master=self)
        self.options.grid(row=4, column=0, padx=10, pady=5, sticky='nsew')

        self.options_entry = ctk.CTkEntry(master=self.options, width=500, font=self.font, placeholder_text="Additional path argument after the destination drive letter.")
        self.options_entry.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        #self.options_checkbox = ctk.CTkCheckBox(master=self.options, text='Insert Path', offvalue=False, onvalue=True)
        #self.options_checkbox.grid(row=0, column=1, padx=10, pady=10, sticky='e')
        self.options_switch = ctk.CTkSwitch(master=self.options, text='Insert Path', offvalue=False, onvalue=True, switch_width=50)
        self.options_switch.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        self.log_frame = ctk.CTkFrame(master=self)
        self.log_frame.grid(row=5, column=0, padx=10, pady=5, sticky='nsew')

        self.log_label = ctk.CTkLabel(master=self.log_frame, text='Log',  font=self.font)
        self.log_label.grid(row=0, column=0, padx=20, pady=5, sticky="w")
        self.log_textbox = ctk.CTkTextbox(master=self.log_frame, width=660, height=400, font=self.font, wrap="none")
        self.log_textbox.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

    def browse_callback(self):
        files = fd.askopenfilename()
        self.files_entry.delete(0, "end")
        self.files_entry.insert(0, files)

    def preview_callback(self):
        self.log_textbox.delete("0.0", "end")
        if self.files_entry.get() != "":
            log = file_copier(self.destination_letter_optionbox.get() + ":", str(self.files_entry.get()), False, self.options_switch.get(), self.options_entry.get())
            for entry in log:
                self.log_textbox.insert("end", entry)

    def backup_callback(self):
        self.log_textbox.delete("0.0", "end")
        if self.files_entry.get() != "":
            log = file_copier(self.destination_letter_optionbox.get() + ":", str(self.files_entry.get()), True, self.options_switch.get(), self.options_entry.get())
            for entry in log:
                self.log_textbox.insert("end", entry)


    # This function can get temp path for your resource file
    # relative_path is your icon file name
    def resource_path(self, relative_path):
    #""" Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
if __name__ == "__main__":
    app = Gui()
    app.mainloop()

