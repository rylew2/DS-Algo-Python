def largestRectangleArea( heights) -> int:
    if not heights: return 0
    if len(heights) == 1: return heights[0]
    stack = [-1]
    maxarea = 0
    for i in range(len(heights)):
        print('stack={} maxarea={}'.format(stack, maxarea))
        while (stack[-1] != -1 and heights[stack[-1]] >= heights[i]):
            computedMax = heights[stack.pop()] * (i - stack[-1] - 1)
            print('computed area = {} maxarea={}'.format(computedMax, maxarea))
            print(stack)
            maxarea = max(maxarea, computedMax)
        stack.append(i)

    print(i)
    while stack[-1] != -1:
        maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))

    return maxarea

l = [2,1,5,6,2,3]
largestRectangleArea(l)