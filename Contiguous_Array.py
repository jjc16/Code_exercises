tst1 = [1,1,2,3,4,5,7,9]
tst2 = [2,5,6,7,10]
tst3 = [2]
tst4 = []

tst5 = [1,2,1,2,1,2,3,3,4,4,5]
tst6 = [1,1,3,3,5,5]
tst7 = [2,3]

def cont_array(arr):
    '''Find length of largest contiguous increasing array in input list '''

    if len(arr) == 1:
        return 1
    if len(arr) == 0:
        return []

    ii = 0
    max_array = 0
    curr_array = 0
    start_cursor = ii
    end_cursor = ii+1

    while ii < len(arr)-1:
        if arr[end_cursor] - arr[start_cursor] == end_cursor - start_cursor:
            end_cursor += 1
            curr_array += 1
            ii += 1
        else:
            ii += 1
            start_cursor = ii
            end_cursor = ii+1
            curr_array = 0
        if curr_array > max_array:
            max_array = curr_array

    return max_array+1
    