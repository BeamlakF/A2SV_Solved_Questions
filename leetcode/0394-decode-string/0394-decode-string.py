class Solution:
    def decodeString(self, s: str) -> str:
        def decode(index):
            result = ''
            num = 0

            while index < len(s):
                char = s[index]

                if char.isdigit():
                    num = num*10 + int(char)

                elif char == '[':
                    inner, next_index = decode(index+1)
                    result +=num *inner
                    num = 0
                    index = next_index

                elif char == ']':
                    return result, index

                else:
                    result +=char

                index +=1
            return result, index

        result, _ = decode(0)
        return result

        