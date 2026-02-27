from collections import Counter

def solution(nums):
    answer = 0
    new_num = Counter(nums)
    
    
    return min(len(new_num), len(nums) // 2)