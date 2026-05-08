class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n=len(sandwiches)
        q=deque(students)
        res=n
        for sandwich in sandwiches:
            ctn=0
            while ctn<len(q) and q[0]!=sandwich:
                cur=q.popleft()
                q.append(cur)
                ctn+=1
            if q and q[0] == sandwich:
                q.popleft()
                res-=1
            else:
                break
        return res