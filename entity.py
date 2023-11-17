# Define the entity class
class Entity:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def toString(self):
        return str("{ name: " + self.name + ", description: " + self.description + " }")