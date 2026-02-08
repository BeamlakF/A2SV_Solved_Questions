def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 ==0  and n % n == 0:
            return n
        elif n% 2 !=0:
            return n*2 