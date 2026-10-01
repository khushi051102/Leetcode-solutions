class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        arr = nums[:]
        return self.mergeSort(arr, 0, len(arr) - 1)

    def mergeSort(self, arr, low, high):
        if low >= high:
            return 0
        mid = (low + high) // 2
        count = self.mergeSort(arr, low, mid)
        count += self.mergeSort(arr, mid + 1, high)
        count += self.countPairs(arr, low, mid, high)  
        self.merge(arr, low, mid, high)                
        return count

    def countPairs(self, arr, low, mid, high):
        count = 0
        j = mid + 1
        for i in range(low, mid + 1):
            while j <= high and arr[i] > 2 * arr[j]:
                j += 1
            count += j - (mid + 1)
        return count

    def merge(self, arr, low, mid, high):
        temp = []
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        temp.extend(arr[i:mid + 1])
        temp.extend(arr[j:high + 1])
        arr[low:high + 1] = temp