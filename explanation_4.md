Since the array is made up of only three possible values (0, 1, 2), it is possible to sort the array in a single traversal by
going over each element from start to end, and placing the element in its correct bucket (the 0's bucket which is the left most
one, the 1's bucket which is the middle one, and the 2's bucket which is the right most one). We do this by keeping track of the
next available left spot to place a 0, and the next available right spot to place a 2. If we encounter a 1, we simply move on,
otherwise we swap the 0 or 2 with the appropriate next index for their buckets.

This is an `O(n)` solution and only requires a single traversal.
