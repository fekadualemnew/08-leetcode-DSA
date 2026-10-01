class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = []

        for i in range(1 , n + 1):
            players.append(i)
        
        while len(players) > 1:
            for i in range(k - 1):
                num = players.pop(0)
                players.append(num)
            players.pop(0)
        return players[0]

            
      
            