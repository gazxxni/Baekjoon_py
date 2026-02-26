from collections import Counter

def solution(nums):
    answer = len(nums) // 2
    cnt = Counter(nums)
    answer = min(answer, len(cnt))
    return answer