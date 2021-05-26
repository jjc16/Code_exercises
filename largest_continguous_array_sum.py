''' Problem

Write an efficient program to find the sum of contiguous 
subarray within a one-dimensional array of numbers which 
has the largest sum. For any solution you write, what is 
the space and time complexity.

Example: [-2, -3, 4, -1, -2, 1, 5, -3] Ans: 7
'''

def find_subarray(arr):

    if len(arr) == 1:
        return arr[0]
    if len(arr) == 0:
        return []

    out = []
    for ii in range(1, len(arr)):
        for jj in range(ii-1):
            tmp = sum(arr[jj:ii])
            out.append(tmp)
    return max(out)


