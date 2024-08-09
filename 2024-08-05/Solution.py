class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count=0
        n=len(arr)
        str=[]
        for i in range(n):
            count=0
            for j in range(n):
                if(arr[i]==arr[j]):
                    count=count+1
            if(count==1):
                str.append(arr[i])
        if(len(str)>=k):
            return str[k-1]
        else:
            return ""