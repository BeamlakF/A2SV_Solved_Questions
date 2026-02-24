class Solution:
    def findLongestWord(self, s: str, dictionary) -> str:
        output =""
        for word in dictionary:
            i = 0
            j = 0
        
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == len(word):
                if len(word) > len(output):
                    output = word
                elif len(word) == len(output) and word < output:
                    output = word
        return output
        # I think I need two pointers, or else I will have to iterate in both of the data strs, so I will do i for s and j for word
        #now if Shall I make this pointers at the start and end or next to each other, I am not reversing, so let's do through s and try to match the characters to the ones I find in s, but how do i do that?
        # I can check if s[i] == word[j] are equal, and then move i and j...but then for the loop not to be out of index, I have to limit them, so I will use while loop to say till i reaches here and j reaches here,

          # But then what? I need an returnable new string , go back and initalize
          # If I can find the whole word in s, do i return it...how do i write that? so if j reached the final char in word that is at len(word)
          # then word becomes output
          # But then that returned only ale, it didn't consider my pookie apple so maybe len(word) > len (output)

         