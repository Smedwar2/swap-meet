class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []

        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return None

    ##Wave 2##
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    ###wave 3###
    #1. Swap my_item with their_item between self and other_vendor and return true
    #2. False if either inventory is missing the respective item.
    #3. Remove my_item from self and add their_item, and vice versa for other_vendor.
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    ####wave 4####
    #1. If one of the vendors has no item, we can not swap, so we return False.
    #2. Grab the first item from the inventory
    #3. Grab the first item from the other vendor's inventory.
    #4. Use swap_items() to trade two items.
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False 
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_item, their_item)
