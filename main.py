# main.py

import customtkinter as tk
from gui import AppGUI
from logic import AppLogic

if __name__ == "__main__":
    root = tk.CTk()
    app_logic = AppLogic()
    app_gui = AppGUI(root, app_logic)
    root.mainloop()