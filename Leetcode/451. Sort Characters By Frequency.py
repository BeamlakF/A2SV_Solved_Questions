def frequencySort(self, s: str) -> str:
        count ={}
        output = 0
        for char in s:
            if char not in count:
                count[char] =1
            else:
                count[char] +=1

        sorted_chars = sorted(count, key=count.get, reverse=True)
        
        result = ""
        for char in sorted_chars:
            result += char * count[char]
        
        return result



