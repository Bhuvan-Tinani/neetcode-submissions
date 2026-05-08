class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # ans=[]
        # for i in range(len(arr)):
        #     m1=-1
        #     for j in range(i+1,len(arr)):
        #         m1=max(m1,arr[j])
        #     ans.append(m1)
        # return ans   
        max_right=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i];
            arr[i]=max_right
            max_right=max(max_right,current)
        return arr