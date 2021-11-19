def kbig(nums, k):
    import heapq
    print(heapq.nlargest(k, nums)[-1])
