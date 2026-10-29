class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        total_coins = 0
        n = len(piles) // 3
        
        for i in range(len(piles) - 2, n - 1, -2):
            total_coins += piles[i]
            
        return total_coins

        