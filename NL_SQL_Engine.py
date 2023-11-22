#code for sql engine goes here
#Updated for loading bar
from dotenv import load_dotenv
load_dotenv()
import os
import openai

API_KEY=os.getenv('API_KEY')
print('KEY LOADED: '+API_KEY+'\n')
openai.api_key = API_KEY

#class for entity
class entity():
    def __init__(self, field1, field2):
        self.name = field1
        self.description = field2

"""
Create schema takes in a list of strings,
each representing an entity that schema will represent.
The entity description must have the entity name,
and a natural language description of all fields to be
created. No fields not in the description will be generated
except an ID field if model cannot identify a suitable key.
"""
def create_schema(entities, DBname):
    messages = [ {"role": "system", "content":  
              "You are an NL model that only generates sql commands and scripts. "+
              "You will recieve a Natural language description of a database including "+
              "its name as well as natural language descriptions for each of the entities "+
              "in that schema. Create the sql code to create that schema, as well as the create database command using name, and respond only "+
              "with the sql commands to create the schema. Do not include any natural language "+
              "explanation."}]
    prompt = 'Here is the description: '
    prompt += ('\nDBname: '+DBname+'\n')
    for e in entities:
        prompt += (e.name+': '+e.description+'\n') 
        
    messages.append( 
            {"role": "user", "content": prompt}, 
        )
    chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
    response = chat.choices[0].message.content 
    
    print("\n\nPROMPT\n\n"+prompt+"\n\n")
    return(response) 

"""
Assess schema takes in an set of sql commands
that would generate a schema for a database in string form.
It returns a natural language description of 
any errors the model detects.  
"""
def assess_SQLCommands(input):
    messages = [ {"role": "system", "content":  
                "You are a natural language model whose purpose "+
                "is to create understandable, clear and percise messages "+
                "describing syntax issues with provided SQLite commands "+
                "since error messages from the interpreter are unclear and "+
                "unhelpful. If the provided SQLite commands have more than "+
                "three errors, mention only the first three and add the sentance "+
                "\"There are more errors.\". If the input does not look like "+
                "SQLite, respond only with \"FAULTY DATA\""}]
    prompt = 'Here is the sqlite: \n'
    prompt += input
    
    messages.append( 
            {"role": "user", "content": prompt}, 
        )
    chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
    response = chat.choices[0].message.content 
    
    
    print("\n\nPROMPT\n\n"+prompt+"\n\n")
    return(response) 

"""
Generate Query takes in an set of sql commands
that would generate a schema for a database in string form
as well as a natural language description of a query to write.
It returns a query in RAW SQL format.  
"""
#code for sql engine goes here
def generate_query(schema, NLQueryDescription):
    messages = [
        {"role": "system", "content":
            "You are a natural language model that takes in a set " +
            "of SQLite commands building the schema of a database " +
            "as well as a natural language description of a query. " +
            "Your job is to generate the actual SQLite query. " +
            "If the natural language description of the query does not " +
            "match any entities in the schema provided, respond with " +
            "'DATABASE DOES NOT REPRESENT ENTITIES DESCRIBED'."}
    ]

    prompt = 'Here is the schema: \n' + schema + '\nNow here is the query description: \n' + NLQueryDescription
    messages.append({"role": "user", "content": prompt})

    try:
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        response = chat.choices[0].message.content
        # Assuming the response is correct, return it
        return response.strip()  # .strip() removes any leading/trailing whitespace
    except openai.error.OpenAIError as e:
        # Handle API errors here
        return f"An error occurred: {str(e)}"


e1 = entity('nurse', 'An individual with ssn, payrate, start time, endtime and hourly pay at a hospital')
e2 = entity('doctor', 'An individual with particular specialization, salary, tenure and age')

entities = [e1,e2]

badSqlite = r"""
    CREATE TABLE PhoneBookEntry (
	"Name"	TEXT NOT NULL UNIQUE,
	"PhoneNumber"	DWORD NOT NULL UNIQUE
);"""

schema = r"""
CREATE TABLE "PhoneBookEntry" (
	"Name"	TEXT NOT NULL UNIQUE,
	"PhoneNumber"	TEXT NOT NULL UNIQUE
);
"""
NLQueryDescription = "All the phone numbers starting with 817."

#r = create_schema(entities, 'Hospital DB')
#r = assess_SQLCommands(badSqlite)
#r = generate_query(schema, NLQueryDescription)
#print(r)