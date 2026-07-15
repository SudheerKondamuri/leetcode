class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            while res and res[-1] > 0 and n < 0:
                if res[-1] < -n:
                    res.pop()
                elif res[-1] == -n:
                    res.pop()
                    break
                else:
                    break
            else :
                res.append(n)
        return res

        