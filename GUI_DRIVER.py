#GUI CODE
import tkinter as tk
from tkinter import ttk
from NL_SQL_Engine import * 

#main windows
root = tk.Tk()
root.geometry("800x400")
root.title("SQL SCAFFOLD")

# Create a custom style for the Notebook tabs
style = ttk.Style()
style.configure("TNotebook.Tab", padding=[30, 5])  # Adjust the padding here

# Create a Notebook (Tabbed interface) with the custom style
notebook = ttk.Notebook(root, style="TNotebook")

# Set up frames and add them to the gui
createSchemaFrame = ttk.Frame(notebook)
assessSchemaFrame = ttk.Frame(notebook)
generateQueryFrame = ttk.Frame(notebook)

notebook.add(createSchemaFrame, text="Create Schema")
notebook.add(assessSchemaFrame, text="Assess Schema")
notebook.add(generateQueryFrame, text="Generate Query")

# Pack the notebook to make it visible
notebook.pack(fill='both', expand=True)


"""TODO: add code for the create schema use case """
label1 = ttk.Label(createSchemaFrame, text="ADD GUI ELEMENTS HERE")
label1.pack(padx=10, pady=10)
create_schema("test")

"""TODO: add code for the assess schema use case """
label2 = ttk.Label(assessSchemaFrame, text="ADD GUI ELEMENTS HERE")
label2.pack(padx=10, pady=10)
assess_schema("test")

"""TODO: add code for the generate query use case """
label3 = ttk.Label(generateQueryFrame, text="ADD GUI ELEMENTS HERE")
label3.pack(padx=10, pady=10)
generate_query("test", "test")

# Start the Tkinter main loop
root.mainloop()