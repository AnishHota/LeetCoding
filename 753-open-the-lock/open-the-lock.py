class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        path = ['0','0','0','0']
        if ''.join(path) in deadends:
            return -1

        def bfs(path, visited):
            q = deque()
            q.append(path)
            visited.add(''.join(path))
            moves = -1
            while q:
                moves+=1
                for _ in range(len(q)):
                    temp_path = q.popleft()
                    if ''.join(temp_path) == target:
                        return moves
                    else:
                        for i in range(4):
                            for d in [-1,1]:
                                new_path = temp_path[::]
                                new_path[i]=str((int(temp_path[i])+d)%10)
                                new_path_s = ''.join(new_path)
                                if new_path_s not in deadends and new_path_s not in visited:
                                    q.append(new_path)
                                    visited.add(new_path_s)
            
            return -1
        
        return bfs(path,set())
            
        

                
                


            

        