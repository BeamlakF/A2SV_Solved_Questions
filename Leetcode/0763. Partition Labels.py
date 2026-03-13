from typing import List

def partitionLabels(self, s: str) -> List[int]:
        rightmost = {c: i for i, c in enumerate(s)}# to record the character's last occurence, but we will have to tack where it starts right?
        left =0
        right = 0
        result = []

        for i, letter in enumerate(s):
            right = max(right, rightmost[letter])

            if i == right:
                result.append(right - left + 1)
                left = i + 1 # to start a new partition

        return result


