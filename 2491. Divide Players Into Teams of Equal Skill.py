def dividePlayers(self, skill) -> int:
        skillsort = sorted(skill)
        n = len(skillsort)
        right = n - 1
        left = 0
        sum_comparer = skillsort[right] + skillsort[left]
        chemistry = 0

        while left < right:
            if skillsort[left] + skillsort[right] != sum_comparer:
                return -1

            chemistry += skillsort[left] * skillsort[right]
            left +=1
            right -=1

        return chemistry




        