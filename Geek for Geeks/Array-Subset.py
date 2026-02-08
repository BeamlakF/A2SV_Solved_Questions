def findUnion(self, a, b):        
        new = set()
        
        for x in a:
            new.add(x)
        for x in b: 
            new.add(x)
        
        return new