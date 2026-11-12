class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        n = len(skill)
        skill.sort()

        i = 0
        j = n - 1
        count = 0
        temp = skill[i] + skill[j]
        while i < j:
            sum = skill[i] + skill[j]
            if sum == temp:
                product = skill[i] * skill[j]
                count += product
                i += 1
                j -= 1
            else:
                return -1
        return count