class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr)):
            m1=-1
            for j in range(i+1,len(arr)):
                m1=max(m1,arr[j])
            ans.append(m1)
        return ans     