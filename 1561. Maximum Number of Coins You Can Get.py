def maxCoins(self, piles) -> int:
        my_coins = 0
        pilesort = sorted(piles, reverse = True)
        n = len(pilesort)
        round = n //3

        index = 1
        for _ in range(round):
            my_coins += pilesort[index]
            index += 2

        return my_coins

        