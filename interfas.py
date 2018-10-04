try:
    import Tkinter as Tk
    import tkFileDialog as fileDialog
except ImportError:
    import tkinter as Tk
    fileDialog = Tk.filedialog