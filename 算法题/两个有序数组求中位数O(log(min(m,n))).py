def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    n = len(nums1)
    m = len(nums2)
    mid = (n + m + 1) // 2
    if n < m:
        n, m = m, n
        nums1, nums2 = nums2, nums1
    max_i, min_i = m, 0
    while min_i <= max_i:
        i = (max_i + min_i) // 2
        j = mid - i
        if i > 0 and nums2[i - 1] > nums1[j]:
            max_i = i - 1
        elif i < m and nums2[i] < nums1[j - 1]:
            min_i = i + 1
        else:
            if i == 0:
                re_l = nums1[j - 1]
            elif j == 0:
                re_l = nums2[i - 1]
            else:
                re_l = max(nums2[i - 1], nums1[j - 1])
            if (n + m) % 2 == 1:
                return re_l
            if i == m:
                re_r = nums1[j]
            elif j == n:
                re_r = nums2[i]
            else:
                re_r = min(nums2[i], nums1[j])
            return (re_l + re_r) / 2.0