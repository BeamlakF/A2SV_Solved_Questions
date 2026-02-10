def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings
        return sorted(s) == sorted(t)