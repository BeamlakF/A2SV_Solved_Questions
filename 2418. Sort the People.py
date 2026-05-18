def sortPeople(self, names, heights):
        n = len(names)
        
        for i in range(n):
            for j in range(n - i - 1):
                if heights[j] < heights[j + 1]: 
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
        
        return names

#Using Bubble sort

#Now using Selection Sort
def sortPeople(self, names, heights):
        n = len(names)
        
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if heights[i] < heights[j]:
                    min_idx = j 

                    heights[i], heights[min_idx] = heights[min_idx], heights[i]
                    names[i], names[min_idx] = names[min_idx], names[i]
        
        return names

# Using insertion sort

