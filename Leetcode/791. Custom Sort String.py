from collections import Counter


def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        output = []

        for char in order:
            if char in count:
                output.append(char*count[char])
                del count[char]

        for char in count:
            output.append(char * count[char])

        return "".join(output)
        