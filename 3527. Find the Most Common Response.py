def findCommonResponse(self, responses) -> str:
        freq = {}

        for response in responses:
            for message in set(response):
                if message not in freq:
                    freq[message] = 0

                freq[message] += 1

        return min(freq.keys(), key=lambda key: (-freq[key], key))