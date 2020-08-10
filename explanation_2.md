If the input were already sorted, we could just perform binary search (`O(log n)`) to find the index of the target. So the main
issue in this problem is to find to pivot about which the input is rotated, after which we can un-rotate the input and perform
regular binary search to find the index.

To find the pivot, we look at the middle element of the input and compare it with the adjacent left and right elements. If these
three elements are not sorted, we have found our pivot. If they are sorted, we need to do the same steps either in the left or the
right subarray recursively. To decide which subarray we should look at, we compare the middle element with the start (left-most)
element. If the pivot were somewhere in the left subarray, the start element would be greater than the middle element. Otherwise the
pivot has to be in the right subarray. This way, we eliminate half of the total elements at every recursive step, making this part
of the algorithm also `O(log n)` time complexity.

Hence the overall time complexity of our solution is `O(log n)`.
