def maxarea(height):
    res = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res

height = [int(x) for x in input().split()]
a = maxarea(height)
print(a)
