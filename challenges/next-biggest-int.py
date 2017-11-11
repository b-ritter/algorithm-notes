
def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """

    d = {val: idx for idx, val in enumerate(nums)}
    s = []
    len_nums = len(nums)
    for i in findNums:
        val = -1
        idx = d.get(i) + 1
        if idx < len_nums:
            for j in nums[idx:]:
                if j > i:
                    val = j
                    break
        s.append(val)
    return s

solution = nextGreaterElement([2,3,50],[1,3,2,4,50])
# should be [4,4,-1]
print(solution)