As we go over each element of the input array, we compare the element to the min and max element so far, and update the min or max
if the current element is less than or greater than the existing min or max. This way we get the min and max from an unsorted array
in a single traversal, in `O(n)`.
