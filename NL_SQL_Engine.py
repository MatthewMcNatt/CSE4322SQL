#code for sql engine goes here

"""
Create schema takes in a list of strings,
each representing an entity that schema will represent.
The entity description must have the entity name,
and a natural language description of all fields to be
created. No fields not in the description will be generated
except an ID field if model cannot identify a suitable key.
"""
def create_schema(entities):
    return("NOT IMPLEMENTED") 

"""
Assess schema takes in an set of sql commands
that would generate a schema for a database in string form.
It returns a natural language description of 
any erros the model detects.  
"""
def assess_schema(schema):
    return("NOT IMPLEMENTED") 

"""
Generate Query takes in an set of sql commands
that would generate a schema for a database in string form
as well as a natural language description of a query to write.
It returns a query in RAW SQL format.  
"""
#code for sql engine goes here
def generate_query(schema, prompt):
    return("NOT IMPLEMENTED") 
