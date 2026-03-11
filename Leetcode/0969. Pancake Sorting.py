def pancakeSort(self, arr):
        output = []
        n = len(arr)
        
        for size in range(n, 1, -1):
            
            max_index = arr.index(size)
            
            if max_index == size - 1:
                continue
            
            if max_index != 0:
                output.append(max_index + 1)
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
            
            output.append(size)
            arr[:size] = reversed(arr[:size])
        
        return output