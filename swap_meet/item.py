##Wave 2##
import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        return "Item"

###Wave 3###
# 1.Stringify instance of Item class
# 2. this method returns a string representation of the Item instance.
# 3. Returns a string in the format: "An object of type <category> with id <id>."
    def __str__(self):
        # return the required sentence
        return f"An object of type {self.get_category()} with id {self.id}."


        #####Wave 5#####
    def condition_description(self):
        if self.condition == 0:
            return "heavily used"
        elif self.condition == 1:
            return "very used"
        elif self.condition == 2:
            return "used"
        elif self.condition == 3:
            return "good"
        elif self.condition == 4:
            return "very good"
        elif self.condition == 5:
            return "mint condition"