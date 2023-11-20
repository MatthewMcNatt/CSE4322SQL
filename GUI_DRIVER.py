#GUI CODE
import threading
import time
import tkinter as tk
from tkinter import ttk, filedialog
from NL_SQL_Engine import * 
from entity import *

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


'''
--------------------------------------------------------------
-------------------CREATE SCHEMA ~ VARIABLES------------------
--------------------------------------------------------------
'''

#list of all entities thus far appended
entities = []
DBname = None
response = None

'''
------------------------------------------------------------
-------------------CREATE SCHEMA ~ METHODS------------------
------------------------------------------------------------
'''

#create an entity
def add_entity():
    #extract information from entry boxes
    entity_name = entity_name_entry.get()
    entity_description = entity_description_entry.get()

    #add the entity to the list as string
    user_defined_entity = Entity(entity_name, entity_description)
    entities.append(user_defined_entity)
    
    for e in entities:
        print(e.toString() + "\n")

    update_entity_display()

#empty contents of the list to start over
def restart():
    global entities
    entities = []
    display_entities.delete(1.0, tk.END)
    display_schema.delete(1.0, tk.END)

#list all entities in entity display box
def update_entity_display():
    # Clear the existing content in the Text widget
    display_entities.delete(1.0, tk.END)

    # Iterate through entities and insert them into the Text widget
    for index, e in enumerate(entities, start=1):
        entity_info = f"{index}. {e.name}\n   {e.description}\n\n"
        display_entities.insert(tk.END, entity_info)

#update display schema to include ChatGPT response
def update_schema_display():
    # Clear the existing content in the Text widget
    display_schema.delete(1.0, tk.END)

    display_schema.insert(tk.END, response)

#create schema draft via SQL_Engine
def generate():
    
    #access/update dbname global variable
    global DBname
    DBname = database_name_entry.get()

    #generate queries via sql engine
    global response
    response = create_schema(entities, DBname)

    #update display
    update_schema_display()

def export():
    # Open a file in write mode (creates the file if it doesn't exist)
    global DBname
    filename = DBname + ".sql"
    with open(filename, 'w') as file:
        # Print a string to the file
        print(response, file=file)

#user input database attributes: name & entities

'''
------------------------------------------------------------
---------------CREATE SCHEMA ~ DEFINE WIDGETS---------------
------------------------------------------------------------
'''

#Labels
entity_name_label = ttk.Label(createSchemaFrame, text="Entity Name:")
entity_description_label = ttk.Label(createSchemaFrame, text="Entity Description:")
database_name_label = ttk.Label(createSchemaFrame, text="Database Name:")
entity_display_label = ttk.Label(createSchemaFrame, text="Current Entities:")
schema_display_label = ttk.Label(createSchemaFrame, text="Current Schema:")

#Entry boxes
entity_name_entry = ttk.Entry(createSchemaFrame, width=20)
entity_description_entry = ttk.Entry(createSchemaFrame, width=40)
database_name_entry = ttk.Entry(createSchemaFrame, width=20)

#Buttons
add_entity_button = ttk.Button(createSchemaFrame, text="Add new entity", command=add_entity)
restart_button = ttk.Button(createSchemaFrame, text="Restart", command=restart)
generate_button = ttk.Button(createSchemaFrame, text="Generate", command=generate)
export_button = ttk.Button(createSchemaFrame, text="Export (.sql)", command=export)

#Text Boxes
display_entities = tk.Text(createSchemaFrame, height=70, width=55, wrap=tk.WORD)
display_schema = tk.Text(createSchemaFrame, height=70, width=55, wrap=tk.WORD)

#Scroll Bars
entities_scrollbar = ttk.Scrollbar(createSchemaFrame, command=display_entities.yview)
display_entities.config(yscrollcommand=entities_scrollbar.set)
schema_scrollbar = ttk.Scrollbar(createSchemaFrame, command=display_schema.yview)
display_schema.config(yscrollcommand=schema_scrollbar.set)

'''
---------------------------------------------------------
---------------CREATE SCHEMA ~ GRID LAYOUT---------------
---------------------------------------------------------
'''

#Show Labels
entity_name_label.grid(row=0, column=0, padx=50, pady=0, sticky="w")
entity_description_label.grid(row=2, column=0, padx=50, pady=0, sticky="w")
database_name_label.grid(row=6, column=0, padx=50, pady=0, sticky="w")
entity_display_label.grid(row=0, column=1, padx=5, pady=0, sticky="w")
schema_display_label.grid(row=0, column=3, padx=5, pady=0, sticky="w")

#Show Entry Boxes
entity_name_entry.grid(row=1, column=0, padx=50, pady=0, sticky="w")
entity_description_entry.grid(row=3, column=0, padx=50, pady=0, sticky="w")
database_name_entry.grid(row=7, column=0, padx=50, pady=0, sticky="w")

#Show Buttons
add_entity_button.grid(row=4, column=0, padx=50, pady=0, sticky="w")
restart_button.grid(row=5, column=0, padx=50, pady=0, sticky="w")
generate_button.grid(row=8, column=0, padx=50, pady=0, sticky="w")
export_button.grid(row=9, column=0, padx=50, pady=0, sticky="w")

#Display Text Boxes
display_entities.grid(row=1, column=1, rowspan=11, padx=10, pady=10, sticky="nsew")
display_schema.grid(row=1, column=3, rowspan=11, padx=10, pady=10, sticky="nsew")

#Display Scroll Bars
entities_scrollbar.grid(row=1, column=2, rowspan=11, pady=10, sticky="ns")
schema_scrollbar.grid(row=1, column=4, rowspan=11, pady=10, sticky="ns")

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
    
    if(ID == CREATE_SCHEMA_ID):
        CREATE_SCHEMA_RESULTS = async_task()
        #add any state changes to UI here for your use case. 
        #If you want things to execute AFTER its stored it must be here. 
        #FOR EXAMPLE: 
        label5.config(text=CREATE_SCHEMA_RESULTS) #updates label 5 in the testing tab
        print(CREATE_SCHEMA_RESULTS)
    if(ID == CREATE_QUERY_ID):
        CREATE_QUERY_RESULTS = async_task()
        #add any state changes to UI here for your use case
    if(ID == ASSESS_SCHEMA_ID):
        ASSESS_SCHEMA_RESULTS = async_task()
        #add any state changes to UI here for your use case
    # Close the loading dialog when the task is complete
    #label5.config(text=CREATE_SCHEMA_RESULTS)
    root.after(0, stop_progressbar, progressbar, loading_dialog)

def load_schema_file():
    filename = filedialog.askopenfilename(title="Select a file", filetypes=(("SQL files", "*.sql"), ("all files", "*.*")))
    if filename:
        with open(filename, 'r') as file:
            schema_text_box.delete(1.0, tk.END)
            schema_text_box.insert(tk.END, file.read())

# Function to generate query from inputs
def on_generate_query():
    # Debug print to confirm this function is called
    print("Generate Query button clicked.")

    schema = schema_text_box.get("1.0", tk.END).strip()
    query_description = query_description_entry.get().strip()

    # Debug print to check the inputs
    print(f"Schema:\n{schema}")
    print(f"Query Description:\n{query_description}")

    try:
        generated_query = generate_query(schema, query_description)
        print(f"Generated Query:\n{generated_query}")

        display_generated_query.delete(1.0, tk.END)
        display_generated_query.insert(tk.END, generated_query)
    except Exception as e:
        # If there's an error, print it out or show it in a message box
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")


# Generate Query Frame Widgets
schema_text_box = tk.Text(generateQueryFrame, height=10, width=55)
query_description_entry = ttk.Entry(generateQueryFrame, width=55)
generate_query_button = ttk.Button(generateQueryFrame, text="Generate Query", command=on_generate_query)
load_schema_button = ttk.Button(generateQueryFrame, text="Load Schema from File", command=load_schema_file)
display_generated_query = tk.Text(generateQueryFrame, height=10, width=55)

# Layout for Generate Query Frame
schema_text_box.pack(padx=10, pady=10)
load_schema_button.pack(padx=10, pady=10)
query_description_entry.pack(padx=10, pady=10)
generate_query_button.pack(padx=10, pady=10)
display_generated_query.pack(padx=10, pady=10)

# Create a new frame for the Assess SQLite Commands tab
assessCommandsFrame = ttk.Frame(notebook)
notebook.add(assessCommandsFrame, text="Assess SQLite Commands")

'''
------------------------------------------------------------
---------ASSESS SQL COMMANDS ~ METHODS & WIDGETS------------
------------------------------------------------------------
'''
openai.api_key = "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"
def assess_SqlCommands(sql_commands):
    try:
        # Prepare the prompt for ChatGPT input
        prompt = f"Assess the following SQL commands:\n{sql_commands}"

        # Call the OpenAI GPT-3 API
        response = openai.Completion.create(
            model="davinci-002",
            prompt=prompt,
            max_tokens=200
        )

        # Extract the generated text from the API response
        generated_text = response['choices'][0]['text']

        # Return the generated description
        return generated_text

    except Exception as e:
        # Handle API errors
        return f"An error occurred while assessing the SQL commands: {str(e)}"
    
def assess_commands():
    # Get the SQL commands from the text box
    sql_commands = sql_commands_text_box.get("1.0", tk.END).strip()

    # Check if the SQL commands are empty
    if not sql_commands:
        assessment_result = "Please enter valid SQL commands."
    else:
        # Call the assess_SqlCommands function
        assessment_result = assess_SqlCommands(sql_commands)

    # Update the display with the assessment result
    display_assessment_result.delete(1.0, tk.END)
    display_assessment_result.insert(tk.END, assessment_result)

# Label and text box for SQL commands input
sql_commands_label = ttk.Label(assessCommandsFrame, text="Enter SQL Commands:")
sql_commands_text_box = tk.Text(assessCommandsFrame, height=10, width=55, wrap=tk.WORD)

# Button to trigger the assessment
assess_button = ttk.Button(assessCommandsFrame, text="Assess", command=assess_commands)

# Display box for the assessment result
display_assessment_result = tk.Text(assessCommandsFrame, height=10, width=55, wrap=tk.WORD)

# Scrollbar for the text box and display box
sql_commands_scrollbar = ttk.Scrollbar(assessCommandsFrame, command=sql_commands_text_box.yview)
sql_commands_text_box.config(yscrollcommand=sql_commands_scrollbar.set)

assessment_result_scrollbar = ttk.Scrollbar(assessCommandsFrame, command=display_assessment_result.yview)
display_assessment_result.config(yscrollcommand=assessment_result_scrollbar.set)

# Layout for Assess SQLite Commands Frame
sql_commands_label.pack(padx=10, pady=10)
sql_commands_text_box.pack(padx=10, pady=10)
sql_commands_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

assess_button.pack(padx=10, pady=10)

display_assessment_result.pack(padx=10, pady=10)
assessment_result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Main loop
root.mainloop()