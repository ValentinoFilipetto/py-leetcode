from typing import List

# time complexity = O(N)
# space complexity = O(1)


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_of_elements = 0
        sum_of_partition = 0
        counter = 3
        partition_counter = 0

        for num in arr:
            sum_of_elements += num

        if sum_of_elements % 3 != 0:
            return False

        sum_of_partition = sum_of_elements / 3

        for num in arr:
            partition_counter += num

            if partition_counter == sum_of_partition and counter > 0:
                counter -= 1
                partition_counter = 0

        if counter == 0:
            return True
        else:
            return False
