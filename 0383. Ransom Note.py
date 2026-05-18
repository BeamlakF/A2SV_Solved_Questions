def canConstruct(self, ransomNote, magazine):
       
        count_magazine = {}
       
        for char in magazine:
            count_magazine[char] = count_magazine.get(char, 0) + 1
        
       
        for char in ransomNote:
            if count_magazine.get(char, 0) == 0:  
                return False
            count_magazine[char] -= 1  
        
        return True