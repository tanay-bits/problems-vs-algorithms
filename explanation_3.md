Once the input list is sorted, it is only a matter of extracting the highest elements (from the back of the sorted list) one by one
and putting them in the first and second output numbers alternately, building up each output number from left to right. Since the
outputs are numbers (not lists of digits), we also have to multiply the extracted digit with the appropriate power of 10 (which we
get from dividing the original length of the input by two).

Considering `n` to be the length of the input list, popping and placing all the digits one by one from the sorted array takes `O(n)`
time.

The more expensive step is sorting the input list, which I do via Heap Sort. This involves building a Max Heap from the input list
and then extracting the max element one by one and putting it at the end, maintaining the max-heap property. Both of these steps
call the `heapify` function which takes `O(log n)` time to ensure max-heap property (due to binary tree traversal). And since
`heapify` is called iteratively for each element of the input list, the overall time complexity of Heap Sort is `O(n log n)`.

Since `O(n log n)` > `O(n)`, the overall time complexity of this solution is `O(n log n)`.
