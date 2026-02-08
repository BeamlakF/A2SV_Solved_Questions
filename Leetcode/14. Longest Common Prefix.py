def longestCommonPrefix(self,strs):
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while prefix and not s.startswith(prefix):
                prefix = prefix[:-1]

        return prefix