Intuition
The problem involves finding the largest rectangle that can be formed in a histogram of different heights. The approach is to iteratively process the histogram's bars while keeping track of the maximum area found so far.

Approach
Initialize a variable maxArea to store the maximum area found, and a stack to keep track of the indices and heights of the histogram bars.

Iterate through the histogram using an enumeration to access both the index and height of each bar.

For each bar, calculate the width of the potential rectangle by subtracting the starting index (retrieved from the stack) from the current index.

While the stack is not empty and the height of the current bar is less than the height of the bar at the top of the stack, pop elements from the stack to calculate the area of rectangles that can be formed.

Update maxArea with the maximum of its current value and the area calculated in step 4.

Push the current bar's index and height onto the stack to continue processing.

After processing all bars, there may still be bars left in the stack. For each remaining bar in the stack, calculate the area using the height of the bar and the difference between the current index and the index at the top of the stack.

Return maxArea as the result, which represents the largest rectangle area.

Complexity
Time complexity: O(n), where n is the number of bars in the histogram. We process each bar once.
Space complexity: O(n), as the stack can contain up to n elements in the worst case when the bars are in increasing order (monotonic).



Code
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for index , height in enumerate(heights):
            start = index
            
            while start and stack[-1][1] > height:
                i , h = stack.pop()
                maxArea = max(maxArea , (index-i)*h)
                start = i
            stack.append((start , height))

        for index , height in stack:
            maxArea = max(maxArea , (len(heights)-index)*height)

        return maxArea    
l=[int(s) for s in input().split()]
obj=Solution()
print(obj.largestRectangleArea(l))
