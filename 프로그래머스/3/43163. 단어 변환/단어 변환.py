from collections import deque

def solution(begin, target, words):
    def bfs(t, start):
        q = deque([(t, start)])
        visited = set()
        visited.add(start)
        
        while q:
            cur_t, cur_word = q.popleft()
            
            if cur_word == target:
                return cur_t
            
            for word in words:
                diff = [a for a, b in zip(cur_word, word) if a != b]
                if len(diff) == 1 and word not in visited:
                    visited.add(word)
                    q.append((cur_t+1, word))
        
        return 0
    
    return bfs(0, begin) 

