class Solution(object):
   def maxArea(self, height):
      low = 0
      high = len(height) - 1
      ans = 0
      while low < high:
         if height[low]<height[high]:
            min_height = height[low]
            min_height_index = low
         else:
            min_height = height[high]
            min_height_index = high
         ans = max(((high - low) ) * min_height,ans)
         if low+1==min_height_index+1:
            low+=1
         else:
            high-=1
      return ans
ob1 = Solution()
print(ob1.maxArea([1,8,6,2,5,4,8,3,7]))
