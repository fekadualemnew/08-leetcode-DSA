class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = deque()

        for i in range(1 , n + 1):
            players.append(i)
        
        while len(players) > 1:
            for i in range(k - 1):
                num = players.popleft()
                players.append(num)
            players.popleft()
        return players[0]

            
      
            