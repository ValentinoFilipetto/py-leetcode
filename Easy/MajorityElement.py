from typing import List

# Time complexity: O(n)
# Space complexity: O(n)


class LinearSpaceSolution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        n = len(nums)

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

            if hash_map[num] > n / 2:
                return num


# Time complexity: O(n)
# Space complexity: O(1)
# aka "Boyer–Moore majority vote algorithm"
# idea: Because this majority element occurs more than n/2 (floor value) times,
# even if other elements will 'vote against it', it will win.


class ConstantSpaceSolution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, 0

        for num in nums:
            if count == 0:
                res = num

            count += 1 if num == res else -1

        return res
