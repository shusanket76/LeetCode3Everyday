class Solution:
    def successfulPairs(
        self, spells, potions, success: int):
        potions.sort()
        res = []
        for x in spells:
            l = 0
            add = True
            r = len(potions) - 1
            while l <= r:
                mid = (l + r) // 2
                if (potions[mid] * x) >= success:
                    r = mid - 1

                else:
                    l = mid + 1
            if add:

                res.append(len(potions) - l)
        return res
