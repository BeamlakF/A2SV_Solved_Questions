class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def myPower(base, exp):
            if exp == 0:
                return 1

            half = myPower(base, exp//2)

            if exp%2 == 0:
                return (half*half) % MOD

            else:
                return (base *half *half) % MOD

        even = (n +1)//2
        odd = n //2

        evn_parts =myPower(5, even)
        odd_parts = myPower(4, odd)

        return (evn_parts * odd_parts) % MOD
        