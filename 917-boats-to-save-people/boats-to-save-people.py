class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        n = len(people)
 
        i = 0
        j = n - 1
        count = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                count += 1
                i += 1
                j -= 1
            elif people[j] <= limit:
                count += 1
                j -= 1
        return count