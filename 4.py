from typing import List

# def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float: 
#     i = 0
#     totalLength = len(nums1) + len(nums2)
#     end = totalLength//2
#     j = k = 0
#     temp = []
#     while i <= end and j<= len(nums1)-1 and k<= len(nums2)-1:
#         if nums1[j] < nums2[k]:
#             temp.append(nums1[j]) 
#             j += 1
#         else:
#             temp.append(nums2[k]) 
#             k += 1
#         i+=1
#     while(i<= end and j > len(nums1) -1):
#         temp.append(nums2[k])
#         i += 1
#         k+=1
#     while(i<=end and k> len(nums2)-1):
#         temp.append(nums1[j]) 
#         i+=1
#         j+=1
#     if totalLength%2 == 0:
#         return (temp[end] + temp[end-1])/2
#     else:
#         return temp[end]


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float: 
    def getNoK(k):
        cur1, cur2 = k//2-1, k//2-1
        while True:
            if cur1 == len(nums1):
                return nums2[k - len(nums1) - 1]
            if cur2 == len(nums2):
                return nums1[k - len(nums2) - 1]
            
            if k == 1:
                return min(nums1[cur1], nums2[cur2])
            
            if nums1[cur1] > nums2[cur2]:
                add = (k - (cur2 + 1))//2
                cur1 = add
                cur2 += add
            elif nums1[cur1] < nums2[cur2]:
                add = (k - cur1 - 1)//2
                cur1 += add
                cur2 = add
            else:
                if k%2 == 0:
                    return nums1[cur1]
                else:
                    return nums1[cur1+1] if nums1[cur1+1] < nums2[cur2+1] else nums2[cur2+1]
    getNoK(10)


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    def getKthElement(k):
        """
        - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
        - 这里的 "/" 表示整除
        - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
        - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
        - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
        - 这样 pivot 本身最大也只能是第 k-1 小的元素
        - 如果 pivot = pivot1, 那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
        - 如果 pivot = pivot2, 那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
        - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
        """
        
        index1, index2 = 0, 0
        while True:
            # 特殊情况
            if index1 == m:
                return nums2[index2 + k - 1]
            if index2 == n:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])

            # 正常情况
            newIndex1 = min(index1 + k // 2 - 1, m - 1)
            newIndex2 = min(index2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
            if pivot1 <= pivot2:
                k -= newIndex1 - index1 + 1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2 - index2 + 1
                index2 = newIndex2 + 1
        
    m, n = len(nums1), len(nums2)
    totalLength = m + n
    if totalLength % 2 == 1:
        return getKthElement((totalLength + 1) // 2)
    else:
        return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2



def getNoK(nums1, nums2, k):
    start1, start2 = 0, 0
    len1, len2 = len(nums1), len(nums2)
    while True:
        if start1 == len1:
            return nums2[k - len1 - 1]
        if start2 == len2:
            return nums1[k - len2 - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        end1 = min(start1 + k//2 - 1, len1)
        end2 = min(start2 + k//2 - 1, len2)
        if nums1[end1] <= nums2[end2]:
            k -= end1 - start1 + 1
            start1 = end1 + 1
            # start2 = start2
        else:
            k -= end2 - start2 + 1
            start2 = end2 + 1
            # start1 = start1









if __name__ == "__main__":
    a = [1,2,3,9,10,16,22,24]
    b = [3,4,7,8,17,20,29,38,51,79,84,200]
    # print(findMedianSortedArrays(a, b))
    print(getNoK(a, b, 10))
