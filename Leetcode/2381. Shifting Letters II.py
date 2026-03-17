def shiftingLetters(self, s: str, shifts) -> str:
        n = len(s)
        sign = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                sign[start] += 1
                sign[end + 1] -= 1
            else:
                sign[start] -= 1
                sign[end + 1] += 1
        
        all_shifts = [0] * n
        current = 0
        for i in range(n):
            current += sign[i]
            all_shifts[i] = current

        result = []
        for i, char in enumerate(s):
            original_pos = ord(char) - ord('a')
            new_pos = (original_pos + all_shifts[i]) % 26
            new_char = chr(new_pos + ord('a'))
            result.append(new_char)
        
        return ''.join(result)