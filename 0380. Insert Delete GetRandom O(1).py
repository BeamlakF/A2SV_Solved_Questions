import random

def __init__(self):
        # 2. Maps value to its index in self.values for O(1) lookups
        self.val_to_index = {} 
        # 3. Stores the actual values for O(1) random access
        self.values = [] 

def insert(self, val: int) -> bool:
        # 4. Check if value exists in O(1) time
    if val in self.val_to_index: 
            return False # Already exists, return False
        # 5. Store new value index as the current end of the list
    self.val_to_index[val] = len(self.values) 
        # 6. Append value to the list in O(1)
    self.values.append(val) 
    return True # Inserted successfully

def remove(self, val: int) -> bool:
        # 7. Check if value exists in O(1)
    if val not in self.val_to_index: 
        return False # Doesn't exist, return False
        
        # 8. Get index of the value to remove
    index = self.val_to_index[val] 
        # 9. Get the last value in the list
    last_val = self.values[-1] 
        
        # 10. Swap: Move last value to the position of the element to delete
    self.values[index] = last_val 
        # 11. Update the index of the moved last_val in the dictionary
    self.val_to_index[last_val] = index 
        
        # 12. Remove the last element (now a duplicate) in O(1)
    self.values.pop() 
        # 13. Remove the target value from the dictionary
    del self.val_to_index[val] 
    return True # Removed successfully

def getRandom(self) -> int:
        # 14. Return a random element from the list in O(1) time
    return random.choice(self.values)