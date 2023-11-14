#GUI CODE
import threading
import time
import tkinter as tk
from tkinter import ttk
from NL_SQL_Engine import * 

CREATE_SCHEMA_RESULTS="EMPTY"
CREATE_QUERY_RESULTS="EMPTY"
ASSESS_SCHEMA_RESULTS="EMPTY"

CREATE_SCHEMA_ID = 1
CREATE_QUERY_ID= 2
ASSESS_SCHEMA_ID= 3




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

#EXAMPLE ASYNC
def on_button_click():
    Loading_task(lambda:create_schema(entities, 'Hospital DB'), CREATE_SCHEMA_ID)

label4 = ttk.Label(testFrame, text="TESTING")
label5 = ttk.Label(testFrame, text=CREATE_SCHEMA_RESULTS)
label4.pack(padx=10, pady=10)
label5.pack(padx=10, pady=10)
testASYNCButton = tk.Button(testFrame, text="Click me!", command=on_button_click)
testASYNCButton.pack(padx=20, pady=20)

"""
The Async loading function
Takes in the task to be done(params already comrpresses in lambda form)
and the id of the task to be done. This is ugly because TINKTER and Threads 
HATE EACH OTHER. If you want to improve it please do but this
is the best we have for now.
""" 
def Loading_task(async_task, ID):
    loading_dialog = tk.Toplevel(root)
    loading_dialog.title("Loading...")

    progressbar = ttk.Progressbar(loading_dialog, mode="indeterminate")
    progressbar.pack(padx=20, pady=20)
    progressbar.start()

    # Run your asynchronous task in a separate thread
    threading.Thread(target=run_async_task, args=(loading_dialog, progressbar, async_task, ID)).start()

def stop_progressbar(progressbar, loading_dialog):
    progressbar.stop()
    loading_dialog.destroy()

def run_async_task(loading_dialog, progressbar, async_task, ID):
    global CREATE_SCHEMA_RESULTS
    global ASSESS_SCHEMA_RESULTS
    global CREATE_QUERY_RESULTS
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    if(ID == CREATE_SCHEMA_ID):
        CREATE_SCHEMA_RESULTS = loop.run_until_complete(async_task())
        #add any state changes to UI here for your use case. 
        #If you want things to execute AFTER its stored it must be here. 
        #FOR EXAMPLE: label5.config(text=CREATE_SCHEMA_RESULTS) updates label 5 in the testing tab
    if(ID == CREATE_QUERY_ID):
        CREATE_QUERY_RESULTS = loop.run_until_complete(async_task())
        #add any state changes to UI here for your use case
    if(ID == ASSESS_SCHEMA_ID):
        ASSESS_SCHEMA_RESULTS = loop.run_until_complete(async_task())
        #add any state changes to UI here for your use case
    # Close the loading dialog when the task is complete
    #label5.config(text=CREATE_SCHEMA_RESULTS)
    root.after(0, stop_progressbar, progressbar, loading_dialog)

root.mainloop()