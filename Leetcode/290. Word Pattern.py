def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern)!=len(s): 
            return False
        group={}
        for i in range(len(pattern)):
            if pattern[i] in group and group[pattern[i]][0]!=s[i]:
                return False
            if [s[i]] in group.values() and pattern[i] not in group:
                return False
            group[pattern[i]]=[s[i]]
        return True