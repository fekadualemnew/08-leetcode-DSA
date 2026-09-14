class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = {} 

        for winner, loser in matches:
            if winner not in lost:
                lost[winner] = 0

            if loser not in lost:
                lost[loser] = 1
            else:
                lost[loser] += 1
        
        victory = []
        lost1 = []

        for key, value in lost.items():
            if value == 0:
                victory.append(key)
            elif value == 1:
                lost1.append(key)
        
        return [sorted(victory), sorted(lost1)]