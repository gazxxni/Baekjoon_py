def solution(numbers, target):
    def dfs(idx, cur_sum):
        if idx == len(numbers):
            if cur_sum == target:
                return 1
            else:
                return 0
            
        return dfs(idx + 1, cur_sum + numbers[idx]) + dfs(idx + 1, cur_sum - numbers[idx])
        
        
        
    return dfs(0, 0)