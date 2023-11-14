#GUI CODE
import threading
import time
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
testFrame = ttk.Frame(notebook)

notebook.add(createSchemaFrame, text="Create Schema")
notebook.add(assessSchemaFrame, text="Assess Schema")
notebook.add(generateQueryFrame, text="Generate Query")
notebook.add(testFrame, text="Testing REMOVE LATER")


# Pack the notebook to make it visible
notebook.pack(fill='both', expand=True)


"""TODO: add code for the create schema use case """
label1 = ttk.Label(createSchemaFrame, text="ADD GUI ELEMENTS HERE")
label1.pack(padx=10, pady=10)
#create_schema("test")

"""TODO: add code for the assess schema use case """
label2 = ttk.Label(assessSchemaFrame, text="ADD GUI ELEMENTS HERE")
label2.pack(padx=10, pady=10)
#assess_schema("test")

"""TODO: add code for the generate query use case """
label3 = ttk.Label(generateQueryFrame, text="ADD GUI ELEMENTS HERE")
label3.pack(padx=10, pady=10)
#generate_query("test", "test")

#test code
def on_button_click():

    r = Loading_task(lambda:async_hello_world(2))

label4 = ttk.Label(testFrame, text="TESTING")
label4.pack(padx=10, pady=10)
testASYNCButton = tk.Button(testFrame, text="Click me!", command=on_button_click)
testASYNCButton.pack(padx=20, pady=20)

# The Async loading function

def Loading_task(async_task):
    loading_dialog = tk.Toplevel(root)
    loading_dialog.title("Loading...")

    progressbar = ttk.Progressbar(loading_dialog, mode="indeterminate")
    progressbar.pack(padx=20, pady=20)
    progressbar.start()

    # Run your asynchronous task in a separate thread
    threading.Thread(target=run_async_task, args=(loading_dialog, progressbar, async_task)).start()

def stop_progressbar(progressbar, loading_dialog):
    progressbar.stop()
    loading_dialog.destroy()

def run_async_task(loading_dialog, progressbar, async_task):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    result = loop.run_until_complete(async_task())
    # Close the loading dialog when the task is complete
    print(result)
    root.after(0, stop_progressbar, progressbar, loading_dialog)

root.mainloop()