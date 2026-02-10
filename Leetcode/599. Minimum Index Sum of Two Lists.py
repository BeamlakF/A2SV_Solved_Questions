def findRestaurant(self, list1, list2):
        index_map = {s: i for i, s in enumerate(list2)}
        
        min_sum = float('inf')
        result = []
        
        for i, s in enumerate(list1):
            if s in index_map:
                index_sum = i + index_map[s]
                
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [s]
                elif index_sum == min_sum:
                    result.append(s)
        
        return result
