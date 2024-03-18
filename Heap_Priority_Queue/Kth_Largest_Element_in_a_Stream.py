# Kth Largest Element in a Stream

'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
'''

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initialize min-heap with the first k elements
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        # keep only the k largest elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # add new element to the min-heap
        heapq.heappush(self.minHeap, val)
        # if heap size exceeds k, remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # return the current kth largest element
        return self.minHeap[0]
