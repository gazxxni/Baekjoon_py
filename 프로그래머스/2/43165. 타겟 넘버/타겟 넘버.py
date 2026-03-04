def solution(numbers, target):
    def dfs(index, cur_sum):
        if index == len(numbers):
            if cur_sum == target:
                return 1
            else:
                return 0
            
        return dfs(index + 1, cur_sum + numbers[index]) + dfs(index + 1, cur_sum - numbers[index])
    
    
    return dfs(0, 0)